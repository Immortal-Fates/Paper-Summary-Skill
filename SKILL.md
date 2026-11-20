---
name: paper-summary
description: Summarize a paper into a concise, insight-led Typora-friendly markdown note with Takeaway, Contribution, Motivation, Core Mechanism, Mermaid Pipeline, Experiment, and Critical Thinking.
---

## What I do

This skill transforms a reliable paper link into a structured, insight-led paper summary in Typora-friendly markdown.

Summaries are written in Chinese-dominant mixed-language style across all sections (preserving English technical proper nouns inside concise Chinese prose). The note opens with `Takeaway` and `Contribution` for immediate executive orientation, defines the unresolved problem in `Motivation`, establishes the `Core Mechanism` followed immediately by its runtime Mermaid `Pipeline`, delivers experimental evidence in `Experiment`, and concludes with rigorous `Critical Thinking`.

## Core conventions

- **Source grounding & anti-fabrication**: Every equation, symbol, complexity bound, hardware spec, and numerical claim must come directly from the paper's ground-truth source (`source/` LaTeX or PDF). Never invent synthetic `\underbrace` equations, fake summations, or unverified metrics just to fill a template slot; when the paper states an inequality, scaling bound, or recurrence instead of a multi-term loss, present the paper's actual formulation faithfully.
- **Strict 1-sentence per point rule**: Every bullet point across `Contribution`, `Motivation`, `Core Mechanism`, `Experiment`, and `Critical Thinking` must be strictly limited to **exactly 1 concise sentence** (target ~30–60 Chinese characters, stating underlying causality directly; no semicolon-chained compound sentences or vacuous filler). Never drop essential operators, tensor shapes, or quantitative bounds merely to force a shorter character count.
- **On-demand `>` explanation blocks (Self-contained readability)**: Keep main bullets to 1 crisp sentence for fast scanning, and place an indented plain `>` blockquote underneath **only when a reader unfamiliar with the paper faces a conceptual leap or hidden derivation** (such as *why* memory scales as $2bns^2$ in `Motivation`, how an inequality like $c \ge F/B$ or `Online Softmax` rescaling works in `Core Mechanism`, or why a failure mode occurs in `Critical Thinking`). Explain in plain, accessible Chinese with simple source-grounded math or analogies. **Do NOT force `>` under every bullet**: omit it on `Takeaway`, `Contribution`, `Experiment` (already paired with `> [!NOTE]`), and self-explanatory bullets; always separate a plain `>` block from `> [!NOTE]` so Markdown never merges them.
- **English captions with Chinese explanations**: All bullet captions must be in English Title Case (e.g., `**Core Problem**:`, `**Core Framework**:`, `**Component**:`, `**Failure Mode**:`); the explanatory prose remains concise Chinese-dominant mixed-language.
- **Preserve English for technical proper nouns**: All technical terms, module names, architecture components, algorithms, loss functions, parallelism strategies, benchmark names, and core theoretical constructs (e.g., `Encoder`, `Decoder`, `Vector Quantizer`, `Codebook`, `Straight-Through Estimator (STE)`, `Posterior Collapse`, `Self-Attention`, `FeedForward`, `Online Softmax`, `Tensor / Sequence / Data Parallelism`, `Key-Value Block`, `Causal Mask`, `Full / Mixed Precision`, `Diffusion`, `Latent Space`) must strictly remain in English throughout the text. Never translate them into awkward or localized Chinese phrases (e.g., strictly use "Vector Quantizer", never "离散码本量化器"; use "Encoder / Decoder", never "编码器 / 解码器"; use "Blockwise FeedForward" / "Tensor Parallelism", never "分块前馈网络" / "张量并行").
- **Micro-mechanism transparency**: Ban abstract, vacuous filler phrases (such as "提取高层表征", "压缩信息瓶颈", "通过优化实现目标", "实现无损全局局部累加"). Every mechanism must penetrate to the **paper-faithful operator and physical-boundary level**:
  1. *Concrete operators & execution tricks*: State the exact mathematical operation, rescaling rule, or communication primitive present in the paper (e.g., forward quantization with STE via $z = z_e + \text{sg}[z_q - z_e]$, or `Online Softmax` log-sum-exp rescaling overlapped with P2P `KV` transfer).
  2. *Counterfactual purpose or physical bottleneck*: For multi-term losses, state which parameters each term updates and what degeneration $\text{sg}$/regularizers prevent; for systems/parallelism papers, state the exact bottleneck inequality or threshold (e.g., arithmetic intensity $c \ge F/B$ and minimum per-device length $s = 6c$ required to hide communication).
  3. *Explicit tensor shapes, memory bounds & granularity*: Clearly state data representations or resource footprints (e.g., $H \times W \times D$ feature grids, discrete 1D token sequences, or per-layer activation memory bound $6bch$).
- **Direct autonomous execution**: Upon receiving a paper link or command, immediately execute reading and generation. Never prompt the user with scope, depth, or extension queries; summary scope is strictly bounded to the target paper itself.
- **Typora list hierarchy**: Main summary sections are list items (`* Section Name` or `- Section Name`) under the note topic. All child content (prose, `>` explanation blocks, formulas, images, `> [!NOTE]` callouts, and Mermaid diagrams) must be indented by 2 spaces under its owning bullet to fold correctly in Typora.
- **Preserve existing scaffolding**: If editing an existing note file, preserve existing frontmatter, title, TOC, and unrelated note content.

## Note template and section order

Follow this exact section order:
1. `Takeaway`
2. `Contribution`
3. `Motivation`
4. `Core Mechanism`
5. `Pipeline`
6. `Experiment`
7. `Critical Thinking`

```markdown
**<Full Paper Title>**. <Author 1, Author 2, Author 3 | First Author et al.>. **<Venue>**, **<Year>**. [(Paper)](URL) [(Project)](URL) (Citations __N__)

* Takeaway

  通过 Straight-Through Estimator (STE) 将连续 Latent Space 分布替换为离散可学习的 Codebook，从根本上消除了 VAE 中的 Posterior Collapse。

* Contribution

  一句话严格定性论文核心学术价值归属（新 challenge、新 solution 或新 research paradigm），且与论文实际证据范围一致。

* Motivation

  * **Core Problem**：以精炼中文单句（约30–60字）直击底层能力鸿沟与核心痛点；严禁描述论文已达成的方案。

    > 按需补充通俗解释、直觉类比或简短公式推导（仅在存在理解门槛或隐藏推导时添加，避免每条无差别复读）。
  * **Why Existing Routes Fail**：以精炼中文单句（约30–60字）说明现有替代路线为何在机理上无法提供该能力。

* Core Mechanism

  * **Core Framework: <Framework Name>**：单句概括完整闭环并明确列出系统由哪几部分组成（如 Encoder-Decoder、Learnable Codebook 及 Prior 阶段）。

    ![Framework](assets/<note-file-base>.assets/framework.png)

    > [!NOTE]
    > **Figure 1. <Original caption or concise overview>.** **Left: Architecture** 说明前向与反向信息流；**Right: Embedding Space** 说明特征与码字更新。

    $$
    \mathcal L = \underbrace{-\log p_\theta(x\mid z_q)}_{\mathcal L_{\mathrm{rec}}} + \underbrace{\|\operatorname{sg}[z_e]-z_q\|_2^2}_{\mathcal L_{\mathrm{codebook}}} + \underbrace{\beta\|z_e-\operatorname{sg}[z_q]\|_2^2}_{\mathcal L_{\mathrm{commit}}}
    $$

    单句说明总损失分工：第 1 项优化重构，第 2 项更新 Codebook 码字，第 3 项以 Commitment loss 防止连续表征在潜空间发散漂移。

    * **Learnable State: <Codebook / Memory>**：明确定义参数集合与超参数（如 $\mathcal C=\{e_1,\dots,e_K\}, e_k\in\mathbb R^D$），说明 $K$（词表容量）与 $D$（通道对齐）的物理意义及更新机制。
    * **Component: <Quantizer / Operator with Trick>**：
      * **Forward Operation**: 给出空间网格坐标 $(i, j)$ 的具体匹配算子（如 $k^*=\arg\min_k \|z_e^{(i,j)}-e_k\|_2^2 \implies z_q^{(i,j)}=e_{k^*}$）。
      * **Backward Trick (STE)**: 解释直通算子（如 $\operatorname{sg}(x)=x, \partial \operatorname{sg}/\partial x=0 \implies \partial z_q/\partial z_e \approx I$）如何无损复制梯度绕过不可导阶跃。
    * **Component: <Decoder / Downstream Modeling>**：单句说明从量化离散网格恢复高维连续信号的解码职责。
    * **Stage 2: <Autoregressive Prior / Generation>**：说明冻结离散特征后如何用自回归模型拟合联合概率分布解决 Next-Token 预测。

      $$
      \underbrace{z\sim p_\psi(z)}_{\text{Prior 采样 Tokens}} \longrightarrow \underbrace{e_z}_{\text{Codebook Lookup}} \longrightarrow \underbrace{\hat x=D_\theta(e_z)}_{\text{Decoder 还原图像}}
      $$

* Pipeline

  ```mermaid
  flowchart LR
      Input[Observe request] --> Model[Core predictor]
      Model --> Gate{Confidence threshold met?}
      Gate -->|Accepted| Result[Return prediction]
      Gate -->|Fallback| Review[Route to human]

      classDef process fill:#EAF2F8,stroke:#1F618D,stroke-width:2px,color:#102A43
      classDef decision fill:#FFF2CC,stroke:#A16207,stroke-width:2px,color:#3F2A00
      classDef future fill:#FCE8E6,stroke:#C5221F,stroke-width:2px,color:#5F1A17
      class Input,Model process
      class Gate decision
      class Review future
```

* Experiment

  ```mermaid
  flowchart LR
      Problem["What failure occurs?<br/>Observed behavior and context"]
      Learn["Is preference learnable?<br/>Consistency and similarity"]
      Predict["Can the model predict it?<br/>Comparison and coverage"]
      Explain["Why does it fail?<br/>Stratified error analysis"]

      Problem -->|"Defines target behavior"| Learn
      Learn -->|"Motivates model signals"| Predict
      Predict -->|"Explains performance limits"| Explain
      Explain -.->|"Revises assumptions"| Learn
  ```

  * **<Experiment or Benchmark Name>**：以精炼单句总结实验设置与核心定量结论（约30–60字），随后放置主要结果表截图（严禁在下方复读纯文本表格）。

    ![Principal result table](assets/<note-file-base>.assets/main-results.png)

    > [!NOTE]
    > **Table 1. <Original caption or concise overview>.** 说明对比基线、关键提升幅度及解释边界。

* Critical Thinking

  * **Pros**:
    * 纯架构与原理优势（严格单句，不复述实验结果）。
    * **Paradigm Demonstration**：（仅限里程碑论文）说明示范的范式及后续采纳的具体代表工作。
  * **Cons**:
    * **Failure Mode: <Name>**：说明理论假设破裂、病态场景或极端环境下的退化机制。
  * **Trade-offs**:
    * 指出为了获得性能优势所牺牲的成本（如算力、通信、灵活性），评估该置换在实际中是否合理有益。
  * **Empirical Support**:
    * 评估评测基线是否公正充足、是否存在消融盲区或评测环境合成化偏差（不复述数值结果）。
  * **Future Directions**:
    * 指出该方向下一个亟待解决的瓶颈或关键突破口。
```

## Section specifications

### Takeaway
- **Chinese-dominant mixed-language single-sentence punchline**: Exactly 1 high-density sentence in concise Chinese prose with technical proper nouns preserved in English, articulating the core insight.
- **Causal insight structure**: Follow `[Core Mechanism/Action] + [Technical Innovation] -> [Solved Pain Point / Target Capability]`.
- **Strict prohibition on noun-stacking formulas**: Do NOT write `Method = A + B + C` or chain proper nouns with `+` signs. The takeaway must explain *how* the innovation works and *what fundamental pain point* it resolves.
- Never wrap in backticks, quotes, or code fences. Do NOT write an English-only sentence in this section.

### Contribution
- **Strictly 1 concise sentence in Chinese**: Placed directly after `Takeaway` for immediate executive-level orientation.
- Classify the paper's primary value as a new challenge, new solution, or new research paradigm within verified evidence bounds. Never claim broader impact than demonstrated.

### Motivation
- **Content strictly in Chinese**: Only the bold captions (`**Core Problem**:`, `**Why Existing Routes Fail**:`) are in English Title Case. The explanation body must be written in concise **Chinese-dominant** prose. Never write English paragraphs in Motivation.
- Strictly 2 concise bullets, each strictly **1 single sentence** (target ~30–60 Chinese characters):
  - `**Core Problem**`: State the unresolved capability gap as a single sharp sentence in Chinese. Apply the completed-outcome test: if the sentence reads as an accomplished method, move that capability to `Core Mechanism`.
  - `**Why Existing Routes Fail**` (or `**Limitation of Existing Work**`): Explain in a single sentence why existing alternatives (imitation, offline RL, extra supervision, scaling, etc.) cannot provide that capability.
- Do NOT introduce the proposed framework name, solution, or architecture here; keep motivation pure.

### Core Mechanism
- Start immediately with the central framework or method, connecting from the capability gap in `Motivation`. Route the internal structure to match the paper's actual nature—**never force neural/VQ-VAE patterns onto distributed systems, parallelism, or theoretical papers**:
- **Pattern A — Neural / Multi-module / Generative papers**:
  - **Framework overview with explicit decomposition**: State the complete operating loop and explicitly declare all constituent modules, states, and stages in the opening `**Core Framework: <Framework Name>**` bullet (e.g., "整体由 Encoder-Decoder、Learnable Codebook 及 Prior 阶段组成").
  - **Self-annotating multi-term objectives (only when the paper defines a multi-term loss)**: Use `\underbrace{...}_{Label}` in LaTeX to bind each actual loss term in the paper (e.g., $\mathcal{L}_{\mathrm{rec}}$, $\mathcal{L}_{\mathrm{codebook}}$, $\mathcal{L}_{\mathrm{commit}}$), followed by 1 sentence explaining parameter update roles and counterfactual stabilization purposes (e.g., why $\text{sg}$ prevents representation drift).
  - **Learnable parameter stores (only when maintained by the model)**: If the model maintains a Codebook, memory bank, or discrete dictionary, define it as `**Learnable State: <Codebook / Memory>**` with notation ($\mathcal C=\{e_1,\ldots,e_K\}, e_k\in\mathbb R^D$), capacity ($K$), dimension ($D$), and update dynamics (loss pulling vs EMA).
  - **Atomic micro-tree breakdown for operators (only when non-differentiable or multi-step forward/backward tricks exist)**: Deconstruct into indented `Forward Operation` (explicit tensor coordinates) and `Backward Trick` (exact gradient identity such as STE).
  - **Inference pipeline closure (only for generative or multi-stage models)**: Explain downstream sampling and conclude with a single-line chained arrow equation ($\text{Prior Sampling} \longrightarrow \text{Lookup} \longrightarrow \text{Decode}$).
- **Pattern B — Systems / Parallelism / Architecture-scheduling papers** (e.g., `Ring Attention`, `FlashAttention`):
  - **Core Mechanism & Schedule**: State the exact partitioning, computation-communication overlap loop, and collaborative operators (e.g., `Online Softmax` statistical rescaling + `Blockwise FeedForward` + P2P `KV` ring primitives) without artificially splitting one unified schedule into 4 redundant `Component` bullets.
  - **Governing Thresholds & Resource Bounds**: Explicitly embed the paper's real analytical inequalities and memory/complexity bounds (e.g., arithmetic intensity condition $4dc^2/F \ge 4cd/B \implies c \ge F/B$, minimum per-device sequence length $s = 6c$, and peak activation footprint $6bch$) instead of inventing `\underbrace` equations.
- **Pattern C — Single-mechanism, Empirical, or Theoretical papers**:
  - Do NOT force the `Core Framework` / `Component` hierarchy onto single-mechanism, empirical, or purely mathematical papers.
  - Use a clean flat list of bullets: `**Core Formulation: <Name>**` (or `**Core Mechanism: <Name>**`) for the primary objective/algorithm, followed by `**Theoretical Property: <Name>**` (or `**Key Derivation: <Name>**`) for theoretical guarantees, convergence bounds, or analytical properties.
- **Technical proper nouns strictly in English**: Component names, parallelism concepts, and algorithm mechanisms (`Encoder`, `Decoder`, `Vector Quantizer`, `Codebook`, `STE`, `Prior`, `Self-Attention`, `FeedForward`, `Online Softmax`, `Tensor / Sequence Parallelism`, `Key-Value Block`, `Causal Mask`) must be written in English. Do NOT translate them into localized Chinese.
- Embed figures and formulas directly below the specific bullet they explain. Do not create separate "Math" or "Figure" sections.

### Pipeline
- Placed immediately after `Core Mechanism` as the runtime/dynamic execution view of the method.
- **Mermaid flowchart only**: Do NOT write numbered text lists.
- Default to `flowchart LR` for readable horizontal layout in Typora; use `flowchart TD` only if strictly hierarchical.
- Diagram the actual evaluated mechanism, not idealized lifecycles. Use action-oriented labels and named branches (`Accepted`, `Fallback`, not bare `Yes`/`No`).
- Distinguish evaluated modules from proposed/future integration using explicit `classDef` styles.

### Experiment
- Placed immediately after `Pipeline` to evaluate the mechanism established above.
- Open with a compact Mermaid research-logic overview diagram showing the study evidence chain (`Problem -> Learnability -> Predictability -> Analysis/Boundaries`).
- Merge all discussion of the same experiment/benchmark into one child bullet (strictly 1 single sentence combining setup and quantitative conclusion).
- Follow each experiment bullet with the principal cropped result table screenshot and its single `> [!NOTE]` callout. Never duplicate the same experiment across benchmarks.
- **No text table duplication**: Quantitative conclusions belong strictly in the single experiment bullet. Never dump an unformatted or redundant markdown/ASCII text table below that merely repeats the numbers already stated in the sentence.

### Critical Thinking
- Pure reflection and critical analysis across 5 dimensions (each bullet strictly 1 concise sentence):
  1. `**Pros**`: Architectural/methodological strengths. Include `**Paradigm Demonstration**` only for verified milestone papers with cited successors.
  2. `**Cons**`: Concrete failure modes under `**Failure Mode: <Name>**:` (breakdown conditions, pathological cases, bandwidth/compute-ratio violations, synchronization/sample divergence, or load imbalance such as `Causal Mask` skew).
  3. `**Trade-offs**`: What was sacrificed (latency, compute, communication complexity, batch-size / sequence-length lower bounds, or autonomy) and whether the exchange is practically justified.
  4. `**Empirical Support**`: Fairness of baselines, numerical precision settings (`Full Precision` vs `Mixed Precision`), compute-budget caps, synthetic vs realistic benchmarks, ablation rigor, and separation of main vs appendix/`\ifanonymous` results.
  5. `**Future Directions**`: The logical next bottleneck actually exposed by this work (not generic boilerplate).
- Do NOT recap quantitative experiment results already covered in `Experiment`.

## Formatting and asset rules

### Citation metadata and author truncation
- Title line format:
  ```markdown
  **<Full Paper Title>**. <Authors>. **<Venue>**, **<Year>**. [(Paper)](URL) [(Project)](URL) (Citations __N__)
```
- **Author list constraint**:
  - 1 to 3 authors: list all names (`Author 1, Author 2, Author 3`).
  - More than 3 authors: strictly truncate to first author plus et al.: `First Author et al.`.
- **Mandatory citation count**: Include `(Citations __N__)` verified from Semantic Scholar (`[(S2)](URL)`), OpenAlex, Google Scholar, or Crossref. If truly unresolvable, write `(Citations __unknown__)`. Never omit this field.

### Formulas and callouts
- **Math delimiters & blank lines**: Strictly `$...$` for inline math; standalone `$$` blocks for display equations. Standalone `$$...$$` blocks must have a blank line before and after. Never place a display formula on the same line as a markdown bullet (`*`) or text. Never use LaTeX `\( ... \)` or `\[ ... \]`.
- **Figure & Table NOTE**: Every embedded image must be immediately followed by exactly one `> [!NOTE]` at the same indentation level. First line must be a concise overview reusing original caption; followed by explanation using English visual anchors (`**Top: ...**`, `**Left: ...**`, `**(b) ...**`, `**Row: ...**`) that accurately match each panel's actual visual role.
- **Asset capture & Visual QA**: After cropping/saving any figure or table image, **inspect the saved image directly** before referencing it. Every table screenshot must capture the **caption/header plus all principal data rows** (never leave a header-only or truncated crop); multi-panel figures must keep all cited subfigures intact. Every number, hardware spec, and anchor in `> [!NOTE]` and the surrounding prose must be verified against both the visible image pixels and the paper source—never extrapolate or fill numbers from memory.
- **Asset paths**: Save images locally to `assets/<note-file-base>.assets/<filename>` and reference with relative paths (`assets/<note-file-base>.assets/<filename>` or `./assets/<note-file-base>.assets/<filename>`).

## Source priority and PDF fallback

- **Priority**: Paper official publication (proceedings, DOI, OpenReview, arXiv) is sole ground truth > official project/code repo/appendix > Semantic Scholar / technical blogs as secondary aids for context, intuition, and citation counts.
- **PDF-first fallback**: When HTML/source is poor or unavailable:
  1. Read Title, Abstract, Intro, and Conclusion to establish missing capability, framework, and main claims.
  2. Scan all figures and tables before detailed reading; extract only claim-bearing visuals and their governing equations.
  3. Paraphrase core claims; never copy raw text walls, long derivations, or full abstracts into the note.

## Hard invariants (Completion checklist)

Before completing the summary, verify every invariant:
1. **Metadata line**: Begins with full paper title in bold; author list truncated to `First Author et al.` when > 3 authors; contains mandatory `(Citations __N__)` or `(Citations __unknown__)`.
2. **Strict single-sentence brevity**: Every bullet point across `Contribution`, `Motivation`, `Core Mechanism`, `Experiment`, and `Critical Thinking` is strictly **1 single sentence** (target ~30–60 Chinese characters, no semicolon chaining, no run-on clauses, high insight density), without stripping required operators, tensor shapes, or quantitative bounds.
3. **Top-level orientation**: `Takeaway` is immediately followed by `Contribution` (single sentence classifying primary value).
4. **Pure motivation**: `Motivation` contains exactly 2 bullets (`Core Problem` and `Why Existing Routes Fail`) without leaking solution/method names.
5. **Paper-faithful Core Mechanism & Pipeline flow**: Route `Core Mechanism` to the paper's actual type. Only use `\underbrace` multi-term objectives, `Learnable State`, forward/backward `STE` sub-bullets, and chained inference arrows when the paper itself defines those constructs; for systems/parallelism/algorithmic papers, present the paper's real governing thresholds, resource/complexity bounds, and core operators without forcing artificial component splits or fabricating equations. Followed immediately by `Pipeline` before `Experiment`.
6. **Source-grounded micro-mechanism transparency**: Ban abstract hand-waving (e.g., "提取特征", "压缩瓶颈") and formula fabrication. Every equation, operator, tensor shape/memory bound ($H \times W \times D$, $6bch$), and threshold ($c \ge F/B$) must come verbatim or faithfully from the paper source.
7. **Direct autonomous execution**: Immediately execute without scope/depth confirmation prompts.
8. **Language policy**: Every section (including `Takeaway`) uses concise Chinese-dominant prose with English technical proper nouns preserved; only section headings and bold captions/labels are in English Title Case (never write English-only paragraphs or English-only `Takeaway`).
9. **Proper nouns in English**: All technical terms, module names, parallelism strategies, architecture concepts, and benchmark names strictly preserve their standard English terminology; never translate them into localized Chinese (e.g., strictly use "Vector Quantizer", "Encoder / Decoder", "Blockwise FeedForward", "Online Softmax", "Tensor Parallelism").
10. **Takeaway**: Exactly 1 Chinese-dominant mixed-language causal insight punchline (Mechanism + Innovation -> Solved Bottleneck), preserving English technical proper nouns without noun-stacking formulas (`Method = A + B + C`), quotes, code fences, or backticks.
11. **Mermaid diagrams & no table duplication**: `Pipeline` is an action-specific flowchart with styled node classes; `Experiment` begins with the research-logic overview diagram. Never generate redundant text tables duplicating bullet sentences.
12. **Figures, tables, Visual QA & NOTEs**: Every image is saved under `assets/<note-file-base>.assets/`, visually inspected after cropping (table screenshots must include header + full data rows; multi-panel figures must be unclipped), and immediately followed by a `> [!NOTE]` whose English visual anchors and numbers match both the image and the paper source.
13. **Delimiters & foldability**: Math uses only `$...$` and standalone `$$...$$` with blank lines before/after (never glued to bullet lines); all child content is indented with 2 spaces under its owning list item.
14. **On-demand `>` explanation layer**: Add concise, source-grounded `>` explanation blocks (plain language + accurate math) under bullets with conceptual leaps or hidden derivations; omit `>` on `Takeaway`, `Contribution`, `Experiment` (use `> [!NOTE]` there), and self-explanatory points, keeping plain `>` separated from `> [!NOTE]`.
