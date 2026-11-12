---
name: paper-summary
description: Summarize a paper into a concise, insight-led Typora-friendly markdown note with Takeaway, Contribution, Motivation, Core Mechanism, Mermaid Pipeline, Experiment, and Critical Thinking.
---

## What I do

This skill turns a reliable paper link into a structured, insight-led paper summary in Typora-friendly markdown.

Summaries are written in Chinese-dominant mixed-language style, except `Takeaway` which is strictly English-only. The note opens with an English Takeaway and Chinese Contribution for immediate high-level orientation, defines the unresolved problem in Motivation, establishes the Core Mechanism followed immediately by its runtime Mermaid Pipeline, delivers experimental evidence, and concludes with rigorous Critical Thinking.

## Core conventions

- **Strict 1-sentence per point rule**: Every bullet point across `Contribution`, `Motivation`, `Core Mechanism`, `Experiment`, and `Critical Thinking` must be strictly limited to **exactly 1 concise sentence** (严格单句，中文约 25–45 字，直接陈述本质因果，严禁分号拼接、复合从句或无信息量套话).
- **English captions with Chinese explanations**: All bullet captions must be in English Title Case (e.g. `**Core Problem**:`, `**Core Framework**:`, `**Key Component**:`, `**Failure Mode**:`); the explanatory prose remains concise Chinese-dominant mixed-language.
- **Typora list hierarchy**: Main summary sections are list items (`* Section Name` or `- Section Name`) under the note topic. All child content (prose, formulas, images, `> [!NOTE]` callouts, and Mermaid diagrams) must be indented by 2 spaces under its owning bullet to fold correctly in Typora.
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

  Replaces continuous latent distributions with a discrete learned codebook via straight-through gradient estimation, fundamentally eliminating posterior collapse in VAEs.

* Contribution

  一句话严格定性论文核心学术价值归属（新 challenge、新 solution 或新 research paradigm），且与论文实际证据范围一致。

* Motivation

  * **Core Problem**：以中文单句（25–45字）直击底层能力鸿沟与核心痛点；严禁描述论文已达成的方案。
  * **Why Existing Routes Fail**：以中文单句（25–45字）说明现有替代路线为何在机理上无法提供该能力。

* Core Mechanism

  * **Core Framework: <Framework Name>**：单句概括从核心问题转向该框架的完整闭环，并明确指出系统由哪几个核心部分/阶段组成。

    ![Framework](assets/<note-file-base>.assets/framework.png)

    > [!NOTE]
    > **Figure 1. <Original caption or concise overview>.** **Top: Rollout Stage** 说明各分区作用；**Left: Architecture** 说明闭环连接关系。

    $$
    \text{Core framework objective}
    $$

    说明公式如何定义框架闭环，并只定义关键符号。

    * **Component: <Component Name>**：单句阐述该部分在系统中的数据流与功能职责。
    * **Component: <Component Name & Solved Bottleneck>**：单句阐述该组件设计如何解决该环节的具体技术瓶颈（如不可微反传、维度灾难等）。

      ![Mechanism figure](assets/<note-file-base>.assets/mechanism.png)

      > [!NOTE]
      > **Figure 2. <Original caption or concise overview>.** 说明该图呈现的局部机制与信息流。

    * **Component: <Component Name>**：单句说明另一核心组成部分的设计巧思与运作机理。

      $$
      \text{Essential formula}
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

  * **<Experiment or Benchmark Name>**：以单句总结实验设置与核心定量结论（25–45字），随后放置主要结果表截图。

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
- **Strictly English single-sentence punchline**: Exactly 1 high-density English sentence articulating the core insight.
- **Causal insight structure**: Follow `[Core Mechanism/Action] + [Technical Innovation] -> [Solved Pain Point / Target Capability]`.
- **Strict prohibition on noun-stacking formulas**: Do NOT write `Method = A + B + C` or chain proper nouns with `+` signs. The takeaway must explain *how* the innovation works and *what fundamental pain point* it resolves, not merely enumerate parts.
- Never wrap in backticks, quotes, or code fences. No Chinese allowed in this section.

### Contribution
- **Strictly 1 concise sentence in Chinese**: Placed directly after `Takeaway` for immediate executive-level orientation.
- Classify the paper's primary value as a new challenge, new solution, or new research paradigm within verified evidence bounds. Never claim broader impact than demonstrated.

### Motivation
- **Content strictly in Chinese**: Only the bold captions (`**Core Problem**:`, `**Why Existing Routes Fail**:`) are in English Title Case. The explanation body must be written in concise **Chinese-dominant** prose. Never write English paragraphs in Motivation.
- Strictly 2 concise bullets, each strictly **1 single sentence** (25–45 characters):
  - `**Core Problem**`: State the unresolved capability gap as a single sharp sentence in Chinese. Apply the completed-outcome test: if the sentence reads as an accomplished method, move that capability to `Core Mechanism`.
  - `**Why Existing Routes Fail**` (or `**Limitation of Existing Work**`): Explain in a single sentence why existing alternatives (imitation, offline RL, extra supervision, scaling, etc.) cannot provide that capability.
- Do NOT introduce the proposed framework name, solution, or architecture here; keep motivation pure.

### Core Mechanism
- Start immediately with the central framework or method, connecting from the capability gap in `Motivation`. Every bullet must be strictly **1 single sentence** (25–45 characters).
- **System / Multi-module papers**:
  - **Framework overview with explicit decomposition**: The opening `**Core Framework: <Framework Name>**` bullet must state the complete operating loop AND explicitly declare what constituent parts/modules/stages make up the system (e.g. "整体由 A、B、C 三部分组成").
  - **Component breakdown as nested list**: Nest each constituent part under `**Component: <Component Name>**` (or `**Stage: <Stage Name>**` for phased pipelines) inside the core framework bullet. Never make components peer bullets with the core framework.
  - **Problem-solution pairing inside components**: Each component bullet must articulate both its functional role in the pipeline and the specific technical bottleneck it resolves (e.g. explain Vector Quantizer and how STE resolves non-differentiable gradient flow directly within the quantizer component; never detach STE as a floating, arbitrary component).
  - Embed overview figure and global objective formula directly under `Core Framework`; embed local mechanism figures and sub-formulas under their corresponding `Component` bullets.
- **Non-system / Single-mechanism or Theoretical papers**:
  - Do NOT force the `Core Framework` / `Component` hierarchy onto single-mechanism, empirical, or purely mathematical papers.
  - Use a clean flat list of bullets: `**Core Formulation: <Name>**` (or `**Core Mechanism: <Name>**`) for the primary objective/algorithm, followed by `**Theoretical Property: <Name>**` (or `**Key Derivation: <Name>**`) for theoretical guarantees, convergence bounds, or analytical properties.
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

### Critical Thinking
- Pure reflection and critical analysis across 5 dimensions (each bullet strictly 1 concise sentence):
  1. `**Pros**`: Architectural/methodological strengths. Include `**Paradigm Demonstration**` only for verified milestone papers with cited successors.
  2. `**Cons**`: Concrete failure modes under `**Failure Mode: <Name>**:` (breakdown conditions, pathological cases, synchronization/sample divergence).
  3. `**Trade-offs**`: What was sacrificed (latency, compute, autonomy) and whether the exchange is practically justified.
  4. `**Empirical Support**`: Fairness of baselines, synthetic vs realistic benchmarks, and ablation rigor.
  5. `**Future Directions**`: The logical next bottleneck to resolve.
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
2. **Strict single-sentence brevity**: Every bullet point across `Contribution`, `Motivation`, `Core Mechanism`, `Experiment`, and `Critical Thinking` is strictly **1 single sentence** (25–45 characters, no semicolon chaining, no run-on clauses, high insight density).
3. **Top-level orientation**: `Takeaway` is immediately followed by `Contribution` (single sentence classifying primary value).
4. **Pure motivation**: `Motivation` contains exactly 2 bullets (`Core Problem` and `Why Existing Routes Fail`) without leaking solution/method names.
5. **Direct core mechanism & Pipeline flow**: `Core Mechanism` starts with `Core Framework` (stating the closed loop and explicitly listing its constituent parts) and nests `Component:` bullets (embedding role and solved technical problem); non-system papers use `Core Formulation` and `Theoretical Property`. Followed immediately by `Pipeline` as runtime execution view before `Experiment`.
6. **Language separation**: Only `Takeaway` is in English. Across all other sections, only the bold captions/labels are in English Title Case, while all body explanations must be strictly in Chinese-dominant prose (never write English sentences in `Motivation`).
7. **Takeaway**: Exactly 1 strictly English causal insight punchline (Mechanism + Innovation -> Solved Bottleneck), without noun-stacking formulas (`Method = A + B + C`), quotes, code fences, or backticks.
8. **Mermaid diagrams**: `Pipeline` is an action-specific flowchart with styled node classes; `Experiment` begins with the research-logic overview diagram.
9. **Figures, tables & NOTEs**: Every image is saved under `assets/<note-file-base>.assets/`, immediately followed by a `> [!NOTE]` with English visual anchors. Principal result table is visually embedded.
10. **Delimiters & foldability**: Math uses only `$...$` and `$$...$$`; all child content is indented with 2 spaces under its owning list item.
