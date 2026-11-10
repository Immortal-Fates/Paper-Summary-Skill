---
name: paper-summary
description: Summarize a paper into a concise, insight-led Typora-friendly markdown note with Takeaway, explicit research problem, a core framework before its supporting designs, mechanism figures and formulas, experimental evidence, a Mermaid pipeline, critical thinking, local assets, and verified citation metadata.
---

## What I do

This skill turns a reliable paper link into a structured, insight-led paper summary in Typora-friendly markdown.

Summaries are written in Chinese-dominant mixed-language style, except `Takeaway` which is strictly English-only. Explanations first identify the unresolved research problem, then present the central framework or core formulation, followed by supporting mechanisms with nested figures and formulas, experimental logic and evidence tables, a Mermaid pipeline, and deep critical evaluation.

## Core conventions

- **Strict 1-sentence per point rule**: Every bullet point across `Motivation`, `Core Mechanism`, `Experiment`, and `Critical Thinking` must be strictly limited to **exactly 1 concise sentence** (严格单句，中文约 25–45 字，直接陈述本质因果，严禁分号拼接、复合从句或无信息量套话).
- **English captions with Chinese explanations**: All bullet captions must be in English Title Case (e.g. `**Core Problem**:`, `**Core Framework**:`, `**Key Component**:`, `**Failure Mode**:`); the explanatory prose remains concise Chinese-dominant mixed-language.
- **Typora list hierarchy**: Main summary sections are list items (`* Section Name` or `- Section Name`) under the note topic. All child content (prose, formulas, images, `> [!NOTE]` callouts, and Mermaid diagrams) must be indented by 2 spaces under its owning bullet to fold correctly in Typora.
- **Preserve existing scaffolding**: If editing an existing note file, preserve existing frontmatter, title, TOC, and unrelated note content.

## Note template and section order

Follow this exact section order:
1. `Takeaway`
2. `Motivation`
3. `Core Mechanism`
4. `Experiment`
5. `Pipeline`
6. `Critical Thinking`

```markdown
**<Full Paper Title>**. <Author 1, Author 2, Author 3 | First Author et al.>. **<Venue>**, **<Year>**. [(Paper)](URL) [(Project)](URL) (Citations __N__)

* Takeaway

  Method = Primary Framework + Enabling Module A + Enabling Module B + Key Loss

* Motivation

  * **Core Problem**：以中文单句（25–45字）直击底层能力鸿沟与核心痛点；严禁描述论文已达成的方案。
  * **Why Existing Routes Fail**：以中文单句（25–45字）说明现有替代路线为何在机理上无法提供该能力。

* Core Mechanism

  * **Core Framework: <Framework Name>**：说明论文如何从核心问题转向该框架，以及框架的完整闭环。

    ![Framework](assets/<note-file-base>.assets/framework.png)

    > [!NOTE]
    > **Figure 1. <Original caption or concise overview>.** **Top: Rollout Stage** 说明各分区作用；**Left: Architecture** 说明闭环连接关系。

    $$
    \text{Core framework objective}
    $$

    说明公式如何定义框架闭环，并只定义关键符号。

    * **Key Component: <Component Name>**：说明框架为何需要该能力，以及设计如何提供该能力。

      ![Mechanism figure](assets/<note-file-base>.assets/mechanism.png)

      > [!NOTE]
      > **Figure 2. <Original caption or concise overview>.** 说明该图呈现的机制与信息流。

    * **Key Component: <Component Name>**：说明另一项必要能力及其关键公式或设计。

      $$
      \text{Essential formula}
      $$

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

  * **<Experiment or Benchmark Name>**：以单句总结实验设置与核心定量结论（25–45字），随后放置主要结果表截图。

    ![Principal result table](assets/<note-file-base>.assets/main-results.png)

    > [!NOTE]
    > **Table 1. <Original caption or concise overview>.** 说明对比基线、关键提升幅度及解释边界。

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

* Critical Thinking

  * **Contribution**: 严格单句判断论文核心价值归属（新 challenge、新 solution 或新 research paradigm），且与论文实际证据范围一致。
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
- **Strictly English**: Plain-text compositional formula (`Method = Framework + Component A + Component B`) or 1–2 concise English sentences.
- Never wrap in backticks, quotes, or code fences. No Chinese allowed in this section.

### Motivation
- **Content strictly in Chinese**: Only the bold captions (`**Core Problem**:`, `**Why Existing Routes Fail**:`) are in English Title Case. The explanation body must be written in concise **Chinese-dominant** prose. Never write English paragraphs in Motivation.
- Strictly 2 concise bullets, each strictly **1 single sentence** (25–45 characters):
  - `**Core Problem**`: State the unresolved capability gap as a single sharp sentence in Chinese. Apply the completed-outcome test: if the sentence reads as an accomplished method, move that capability to `Core Mechanism`.
  - `**Why Existing Routes Fail**` (or `**Limitation of Existing Work**`): Explain in a single sentence why existing alternatives (imitation, offline RL, extra supervision, scaling, etc.) cannot provide that capability.
- Do NOT introduce the proposed framework name, solution, or architecture here; keep motivation pure.

### Core Mechanism
- Start immediately with the central framework or method, connecting from the capability gap in `Motivation`. Every bullet must be strictly **1 single sentence** (25–45 characters).
- **System / Multi-module papers**:
  - Nest explanation, core objective formula, and overview figure under `**Core Framework: <Framework Name>**`.
  - Nest supporting modules under `**Key Component: <Component Name>**` (or `**Supporting Capability: <Capability Name>**`) inside the core framework bullet. Never make modules peer bullets with the core framework.
- **Non-system / Single-mechanism or Theoretical papers**:
  - Do NOT force the `Core Framework` / `Key Component` hierarchy.
  - Use a clean flat list: `**Core Formulation: <Name>**` (or `**Core Mechanism: <Name>**`) for the primary objective/algorithm, followed by `**Theoretical Property: <Name>**` (or `**Key Derivation: <Name>**`).
- Embed figures and formulas directly below the specific bullet they explain. Do not create separate "Math" or "Figure" sections.

### Experiment
- Open with a compact Mermaid research-logic overview diagram showing the study evidence chain (`Problem -> Learnability -> Predictability -> Analysis/Boundaries`).
- Merge all discussion of the same experiment/benchmark into one child bullet (strictly 1 single sentence combining setup and quantitative conclusion).
- Follow each experiment bullet with the principal cropped result table screenshot and its single `> [!NOTE]` callout. Never duplicate the same experiment across benchmarks.

### Pipeline
- **Mermaid flowchart only**: Do NOT write numbered text lists.
- Default to `flowchart LR` for readable horizontal layout in Typora; use `flowchart TD` only if strictly hierarchical.
- Diagram the actual evaluated mechanism, not idealized lifecycles. Use action-oriented labels and named branches (`Accepted`, `Fallback`, not bare `Yes`/`No`).
- Distinguish evaluated modules from proposed/future integration using explicit `classDef` styles.

### Critical Thinking
- Merge all critical insights into this single section across 6 dimensions (each bullet strictly 1 concise sentence):
  1. `**Contribution**`: Exactly 1 sentence classifying the value as a new challenge, new solution, or new paradigm within verified evidence bounds.
  2. `**Pros**`: Architectural/methodological strengths. Include `**Paradigm Demonstration**` only for verified milestone papers with cited successors.
  3. `**Cons**`: Concrete failure modes under `**Failure Mode: <Name>**:` (breakdown conditions, pathological cases, synchronization/sample divergence).
  4. `**Trade-offs**`: What was sacrificed (latency, compute, autonomy) and whether the exchange is practically justified.
  5. `**Empirical Support**`: Fairness of baselines, synthetic vs realistic benchmarks, and ablation rigor.
  6. `**Future Directions**`: The logical next bottleneck to resolve.
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
- **Math delimiters**: Strictly `$...$` for inline math; standalone `$$` blocks for display equations. Never use LaTeX `\( ... \)` or `\[ ... \]`.
- **Figure & Table NOTE**: Every embedded image must be immediately followed by exactly one `> [!NOTE]` at the same indentation level. First line must be a concise overview reusing original caption; followed by explanation using English visual anchors (`**Top: ...**`, `**Left: ...**`, `**(b) ...**`, `**Row: ...**`).
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
2. **Strict single-sentence brevity**: Every bullet point across `Motivation`, `Core Mechanism`, `Experiment`, and `Critical Thinking` is strictly **1 single sentence** (25–45 characters, no semicolon chaining, no run-on clauses, high insight density).
3. **Pure motivation**: `Motivation` contains exactly 2 bullets (`Core Problem` and `Why Existing Routes Fail`) without leaking solution/method names.
4. **Direct core mechanism**: `Core Mechanism` starts directly with the central framework (`Core Framework`) and nested components (`Key Component`), or with `Core Formulation` for non-system papers.
5. **Language separation**: Only `Takeaway` is in English. Across all other sections (`Motivation`, `Core Mechanism`, `Experiment`, `Critical Thinking`), only the bold captions/labels are in English Title Case, while all body explanations must be strictly in Chinese-dominant prose (never write English sentences in `Motivation`).
6. **Takeaway**: Strictly English compositional formula or 1–2 sentences, without quotes, code fences, or backticks.
7. **Mermaid diagrams**: `Experiment` begins with the research-logic overview diagram; `Pipeline` is an action-specific flowchart with styled node classes.
8. **Figures, tables & NOTEs**: Every image is saved under `assets/<note-file-base>.assets/`, immediately followed by a `> [!NOTE]` with English visual anchors. Principal result table is visually embedded.
9. **Delimiters**: Math uses only `$...$` and `$$...$$`; no raw wiki-links (`[[...]]`).
10. **Typora foldability**: All child content is indented with 2 spaces under its owning list item.
