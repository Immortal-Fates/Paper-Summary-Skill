#!/usr/bin/env python3
import argparse
import io
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import urllib.request
from pathlib import Path
from PIL import Image, ImageChops
import pypdf

def trim_image(im, padding=10, threshold=15):
    rgb = im.convert("RGB")
    bg = Image.new("RGB", im.size, (255, 255, 255))
    diff = ImageChops.difference(rgb, bg)
    gray = diff.convert("L")
    mask = gray.point(lambda p: 255 if p > threshold else 0)
    bbox = mask.getbbox()
    if bbox:
        x1 = max(0, bbox[0] - padding)
        y1 = max(0, bbox[1] - padding)
        x2 = min(im.width, bbox[2] + padding)
        y2 = min(im.height, bbox[3] + padding)
        return im.crop((x1, y1, x2, y2))
    return im

def parse_pct_values(pct_str):
    parts = [float(x.strip()) for x in re.split(r"[,\s]+", pct_str.strip()) if x.strip()]
    if len(parts) != 4:
        raise ValueError("Expected 4 values for --pct: top,left,bottom,right")
    # Normalize 0-100 percentage to 0.0-1.0 ratio
    if any(p > 1.0 for p in parts):
        parts = [p / 100.0 for p in parts]
    return parts

def render_pdf_page(pdf_path, page_num, output_path, dpi=200):
    pdf_path = str(Path(pdf_path).resolve())
    output_path = Path(output_path).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_prefix = str(Path(tmp_dir) / "page")
        cmd = [
            "pdftoppm",
            "-png",
            "-r", str(dpi),
            "-f", str(page_num),
            "-l", str(page_num),
            pdf_path,
            tmp_prefix
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode != 0:
            raise RuntimeError(f"pdftoppm failed: {res.stderr.strip()}")

        generated = sorted(Path(tmp_dir).glob("page-*.png"))
        if not generated:
            raise FileNotFoundError(f"pdftoppm did not produce a page image for page {page_num}")
        shutil.copy2(generated[0], output_path)
    return output_path

def crop_image(input_image_path, output_path, pct=None, box=None, box_wh=None, trim=False, padding=10):
    im = Image.open(input_image_path)
    w, h = im.size

    if pct:
        top_r, left_r, bot_r, right_r = parse_pct_values(pct)
        x1 = int(round(left_r * w))
        y1 = int(round(top_r * h))
        x2 = int(round(right_r * w))
        y2 = int(round(bot_r * h))
        crop_box = (max(0, x1), max(0, y1), min(w, x2), min(h, y2))
    elif box:
        parts = [int(round(float(x.strip()))) for x in re.split(r"[,\s]+", box.strip()) if x.strip()]
        if len(parts) != 4:
            raise ValueError("Expected 4 values for --box: x1,y1,x2,y2")
        crop_box = (parts[0], parts[1], parts[2], parts[3])
    elif box_wh:
        parts = [int(round(float(x.strip()))) for x in re.split(r"[,\s]+", box_wh.strip()) if x.strip()]
        if len(parts) != 4:
            raise ValueError("Expected 4 values for --box-wh: x,y,w,h")
        crop_box = (parts[0], parts[1], parts[0] + parts[2], parts[1] + parts[3])
    else:
        crop_box = (0, 0, w, h)

    cropped = im.crop(crop_box)
    if trim:
        cropped = trim_image(cropped, padding=padding)

    out_p = Path(output_path).resolve()
    out_p.parent.mkdir(parents=True, exist_ok=True)
    cropped.save(out_p)
    return out_p

def find_in_pdf(pdf_path, query):
    reader = pypdf.PdfReader(pdf_path)
    q_lower = query.lower()
    matches = []
    for idx, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        if q_lower in text.lower():
            matching_lines = [
                line.strip() for line in text.splitlines() if q_lower in line.lower()
            ]
            matches.append((idx, matching_lines[:3]))
    return matches

def extract_raw_images(pdf_path, output_dir, page_num=None):
    out_dir = Path(output_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    prefix = str(out_dir / "img")

    cmd = ["pdfimages", "-png"]
    if page_num:
        cmd.extend(["-f", str(page_num), "-l", str(page_num)])
    cmd.extend([str(Path(pdf_path).resolve()), prefix])

    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"pdfimages failed: {res.stderr.strip()}")
    return sorted(out_dir.glob("img-*.png"))

def fetch_arxiv_assets(arxiv_id_or_url, output_dir):
    out_dir = Path(output_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    match = re.search(r"(\d{4}\.\d{4,5}(v\d+)?|[a-z\-]+/\d{7})", arxiv_id_or_url)
    if not match:
        raise ValueError(f"Cannot parse arXiv identifier from {arxiv_id_or_url}")
    arxiv_id = match.group(1)

    url = f"https://arxiv.org/e-print/{arxiv_id}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = resp.read()

    extracted_files = []
    if data.startswith(b"%PDF"):
        pdf_file = out_dir / f"{arxiv_id}.pdf"
        pdf_file.write_bytes(data)
        extracted_files.append(pdf_file)
    else:
        try:
            with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tar:
                image_extensions = {".png", ".jpg", ".jpeg", ".pdf", ".eps"}
                for member in tar.getmembers():
                    ext = Path(member.name).suffix.lower()
                    if ext in image_extensions:
                        f = tar.extractfile(member)
                        if f is None:
                            continue
                        clean_name = Path(member.name).name
                        dest_path = out_dir / clean_name
                        dest_path.write_bytes(f.read())

                        # Convert vector PDF figures to PNG
                        if ext == ".pdf":
                            png_dest = dest_path.with_suffix(".png")
                            try:
                                render_pdf_page(dest_path, 1, png_dest, dpi=200)
                                extracted_files.append(png_dest)
                            except Exception:
                                extracted_files.append(dest_path)
                        else:
                            extracted_files.append(dest_path)
        except Exception as e:
            fallback_pdf = out_dir / f"{arxiv_id}.pdf"
            fallback_pdf.write_bytes(data)
            extracted_files.append(fallback_pdf)
    return extracted_files

def main():
    parser = argparse.ArgumentParser(description="Extract and crop paper assets (figures, tables, algorithms).")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # render
    p_render = subparsers.add_parser("render", help="Render a single PDF page to PNG.")
    p_render.add_argument("--pdf", required=True, help="Path to PDF file.")
    p_render.add_argument("--page", type=int, default=1, help="1-based page number.")
    p_render.add_argument("--dpi", type=int, default=200, help="Rendering DPI (default: 200).")
    p_render.add_argument("--output", required=True, help="Destination PNG path.")

    # crop
    p_crop = subparsers.add_parser("crop", help="Crop a bounding box from an image or directly from a PDF page.")
    p_crop.add_argument("--image", help="Input image path.")
    p_crop.add_argument("--pdf", help="Input PDF path (used when --image is not provided).")
    p_crop.add_argument("--page", type=int, default=1, help="1-based page number if using --pdf.")
    p_crop.add_argument("--dpi", type=int, default=200, help="DPI if using --pdf.")
    p_crop.add_argument("--pct", help="Crop box as percentages: top,left,bottom,right (e.g. 10,5,45,95).")
    p_crop.add_argument("--box", help="Crop box as pixels: x1,y1,x2,y2.")
    p_crop.add_argument("--box-wh", help="Crop box as pixels: x,y,w,h.")
    p_crop.add_argument("--trim", action="store_true", help="Auto-trim surrounding whitespace margins.")
    p_crop.add_argument("--padding", type=int, default=10, help="Pixel padding around trimmed content.")
    p_crop.add_argument("--output", required=True, help="Destination PNG path.")

    # find
    p_find = subparsers.add_parser("find", help="Search PDF pages for query string (e.g. 'Algorithm 1').")
    p_find.add_argument("--pdf", required=True, help="Path to PDF file.")
    p_find.add_argument("--query", required=True, help="Search term (case-insensitive).")

    # extract-raw
    p_raw = subparsers.add_parser("extract-raw", help="Extract embedded raster images from PDF via pdfimages.")
    p_raw.add_argument("--pdf", required=True, help="Path to PDF file.")
    p_raw.add_argument("--page", type=int, help="Optional 1-based page number filter.")
    p_raw.add_argument("--output-dir", required=True, help="Directory to save extracted images.")

    # arxiv
    p_arxiv = subparsers.add_parser("arxiv", help="Extract figures from arXiv source tarball or download paper.")
    p_arxiv.add_argument("--id", required=True, help="arXiv ID or URL.")
    p_arxiv.add_argument("--output-dir", required=True, help="Directory to save extracted figures.")

    # info
    p_info = subparsers.add_parser("info", help="Inspect PDF page count or image dimensions.")
    p_info.add_argument("--pdf", help="Path to PDF file.")
    p_info.add_argument("--image", help="Path to image file.")

    args = parser.parse_args()

    if args.command == "render":
        out = render_pdf_page(args.pdf, args.page, args.output, dpi=args.dpi)
        print(f"Rendered page {args.page} to {out}")

    elif args.command == "crop":
        if args.image:
            img_path = args.image
            out = crop_image(img_path, args.output, pct=args.pct, box=args.box, box_wh=args.box_wh, trim=args.trim, padding=args.padding)
        elif args.pdf:
            with tempfile.TemporaryDirectory() as tmp_dir:
                tmp_render = Path(tmp_dir) / "page.png"
                render_pdf_page(args.pdf, args.page, tmp_render, dpi=args.dpi)
                out = crop_image(tmp_render, args.output, pct=args.pct, box=args.box, box_wh=args.box_wh, trim=args.trim, padding=args.padding)
        else:
            parser.error("Either --image or --pdf must be provided for crop.")
        print(f"Cropped asset saved to {out}")

    elif args.command == "find":
        matches = find_in_pdf(args.pdf, args.query)
        if not matches:
            print(f"No occurrences found for '{args.query}'")
        else:
            for page_num, snippets in matches:
                print(f"Page {page_num}:")
                for s in snippets:
                    print(f"  - {s}")

    elif args.command == "extract-raw":
        images = extract_raw_images(args.pdf, args.output_dir, page_num=args.page)
        print(f"Extracted {len(images)} raw images to {args.output_dir}")

    elif args.command == "arxiv":
        assets = fetch_arxiv_assets(args.id, args.output_dir)
        print(f"Retrieved {len(assets)} assets to {args.output_dir}")

    elif args.command == "info":
        if args.pdf:
            reader = pypdf.PdfReader(args.pdf)
            print(f"PDF: {args.pdf}, Pages: {len(reader.pages)}")
        if args.image:
            im = Image.open(args.image)
            print(f"Image: {args.image}, Dimensions: {im.size[0]}x{im.size[1]} (WxH)")

if __name__ == "__main__":
    main()
