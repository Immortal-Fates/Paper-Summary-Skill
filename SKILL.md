---
name: paper-summary
description: Summarize a paper into a concise, insight-led Typora-friendly markdown note with Takeaway, explicit research problem, a core framework before its supporting designs, mechanism figures and formulas, experimental evidence, a Mermaid pipeline, critical thinking, local assets, and verified citation metadata.
---

## What I do

This skill turns a reliable paper link in a markdown note into a repository-native paper summary.

I follow the local paper-reading style already used in this repository, especially the patterns under `AI/ml/DL/CV/Paper-Reading/` and the reading workflow described in `research/Research-Guide/03-Pipeline.md`.

I write concise Chinese-dominant mixed-language summaries in Typora-friendly markdown with strict list nesting. `Takeaway` is English-only and renders a compact compositional formula as plain text. I first identify the paper's actual research problem and central framework, then present supporting mechanisms under that framework instead of as a disconnected list of tricks. Figures sit under the points they explain, experiments prioritize claim-bearing figures and concise table conclusions, `Pipeline` is Mermaid-only, and `Critical Thinking` separates empirical limitations from practical trade-offs.

## Use this skill when

- A markdown note contains a paper link and needs a structured paper summary
- You want the summary in this order: Takeaway, Motivation, Core Mechanism, Experiment, Pipeline (Mermaid), Critical Thinking
- You want the research problem and central framework explained before implementation details
- You want key formulas and useful figures shown directly under the relevant mechanism points
- You want claim-bearing paper figures and tables represented in the note
- You want citation metadata and citation counts verified from reliable bibliographic sources
- You require every summarized paper entry to include a citation count field

## Local repository conventions to follow

- Prefer the style under `AI/ml/DL/CV/Paper-Reading/`
- Prefer the citation style shown in `AI/ml/DL/CV/Paper-Reading/AGENTS.md`
- Keep summaries compact and useful for later review
- Match nearby files before inventing a new structure
- Write explanations mainly in Chinese, but keep technical nouns, module names, benchmark names, and short technical phrases in English when that is clearer (Note: `Takeaway` is strictly English-only)
- Keep Markdown readable in Typora
- Preserve existing frontmatter, title, TOC, and unrelated note content unless the task explicitly asks to restructure them

## Required note structure

Write the summary in Chinese-dominant mixed-language style (with `Takeaway` strictly in English).

Nearby-file structure is the primary rule, but the default language baseline remains Chinese-dominant mixed-language (with English-only `Takeaway`) unless the surrounding directory already has a strong and stable alternative convention.
Use this section order as the default pattern, but adapt to the surrounding file when it already uses a stable local variation such as `Prior` or `Background` instead of `Motivation`.

Place formulas, figures, and their explanations under the specific points they support instead of collecting them into detached galleries.

Use the main summary sections as second-level list items under the note topic, not as Markdown headings:

```markdown
* Takeaway

  Method = T&D Distributed Coordination + Transmission SAC + Distribution MASAC + Complementary Attention + Constraint Violation Penalty

* Motivation

  * **Core problem**: Synthesize what capability the paper wants to create; do not merely list defects in prior work.
  * **Why existing routes are insufficient**: Explain why the current workarounds cannot provide that capability.
  * **Paper objective**: State the concrete framework or capability the paper aims to build.

* Core Mechanism

  * **核心框架：<Framework Name>**：Explain the complete operating loop and why it is the paper's central claim.

    ![Framework](assets/NOTES.assets/framework.png)

    > [!NOTE]
    > **Figure 1. <Original caption or concise overview>.** Explain the meaningful regions and how they form the framework.

    $$
    \text{Core framework objective}
    $$

* Experiment

  * **<Experiment or benchmark name>**：Combine the setup and conclusion for this experiment in one entry.

    ![Principal result table](assets/NOTES.assets/main-results.png)

    > [!NOTE]
    > **Table 1. <Original caption or concise overview>.** State the comparison, key outcome, and any boundary needed to interpret it.

* Pipeline

  ```mermaid
  flowchart LR
      Input[Input] --> Model[Core predictor]
      Model --> Gate{Confidence threshold met?}
      Gate -->|Accepted| Output[Return prediction]
      Gate -->|Fallback| Review[Route to human]
  ```

* Critical Thinking

  * **Pros**: Architectural strengths that are not a recap of experiment results.
  * **Cons**: Concrete failure modes and broken assumptions.
  * **Trade-offs**: What the design sacrifices and whether that cost is justified.
  * **Empirical Support**: Whether the evidence design supports the claims, without restating results.
  * **Future Directions**: The next unresolved bottleneck.
```

- `Takeaway` must be written strictly in English. Keep only a compact compositional formula when one clearly captures the method; otherwise use one or two concise sentences. Render the formula as plain text, without backticks, quotation marks, or other wrapping.
- `Motivation`, `Core Mechanism`, `Experiment`, `Pipeline`, and `Critical Thinking` should use the same `* Section Name` (or `- Section Name`) list-item format.
- Indent every detail under its owning section: prose, formulas, figures, NOTE callouts, and code/Mermaid blocks must belong to the section or child bullet they explain. Use 2 spaces per list level so the structure remains foldable in Typora.
- Never leave Takeaway prose, a framework figure, a formula, an experiment image, or a NOTE callout at the top level merely because the related section uses a list item.

### Takeaway

- **English only**: Write the Takeaway section strictly in English. Do not use Chinese in this section even though the rest of the summary is Chinese-dominant.
- Prefer a compact compositional formula when it captures the paper's central framework and the few enabling designs that make it work. Keep the formula conceptual: do not turn implementation choices, backbone names, data ratios, or experimental details into peer-level terms. Otherwise, summarize the main claim, setting, and significance in one or two English sentences.
- Before writing the formula, identify the sentence or mechanism that best expresses the paper's central insight. The Takeaway must communicate that insight, not merely enumerate the modules in the architecture.
- Render the formula as plain text, without backticks, quotation marks, or a fenced block:
  - Example: Method = T&D Distributed Coordination + Transmission SAC + Distribution MASAC + Complementary Attention + Constraint Violation Penalty
- Do not append a second explanatory sentence when the compositional formula already conveys the takeaway.
- Do not include a `Lineage` line or section.

### Motivation

- Start from the paper's actual goal, not from a list of related-work failures.
- State the **core problem** as an unresolved capability gap: what can the target model or system not do today, and why does that matter?
- Phrase the core problem as a question or a limitation, not as the paper's intended solution. Do not describe an already achieved ability as the problem: `学习能表达多峰动作的策略` and `让未来状态反传指导策略` read as completed claims, not problem statements.
- Apply the completed-outcome test: if the core-problem sentence can stand under the paper's result or contribution without change, it states the solution rather than the gap. Move the intended capability into `论文目标` and keep the problem focused on the missing capability and its constraint.
- Explain why existing routes cannot provide that capability. Typical routes include imitation, offline RL, direct online interaction, additional supervision, or stronger models; choose only routes relevant to the paper.
- State the **paper objective** as the framework or capability the work aims to build.
- Keep this section to 3–4 concise bullets. The nature of the problem may require inference from the Introduction, experiments, and Conclusion; label interpretation when the paper does not state it verbatim.

### Core Mechanism
- Identify the paper's central framework before listing implementation choices. State the capability it creates and the complete operating loop that makes that capability possible.
- Present the central framework first, with its explanation, formula, and figure nested under one `核心框架：<Framework Name>` bullet. Then nest each supporting capability or module (for example V, M, and C) under a `支撑能力` bullet inside that framework. Never place module capabilities as peers of the core-framework bullet.
- Use a named framework when the paper provides one. For a system paper, prefer Chinese labels such as `核心框架：<Framework Name>`, `支撑能力一：<Capability>`, and `支撑能力二：<Capability>` when this hierarchy is genuinely useful; do not force those exact labels onto a paper with another natural organization.
- Do not reduce the section to a flat list of modules, losses, architecture names, or engineering tricks. Explain how each design enables the framework and why it is necessary.
- Do not split points into `What`, `Why`, and `How` subsections.
- Explain the mechanism of every framework module. Embed its original mechanism figure when one exists. When a module has no dedicated figure, use its governing formula or a precise textual explanation instead; do not create a NOTE merely to announce that no figure exists.
- Place each figure inside the mechanism point it explains. Use multiple figures when they explain distinct mechanism points, such as architecture, qualitative behavior, and training loop. Do not use a fixed one-figure limit.
- Put formulas immediately below the point they explain. Keep only formulas needed to understand the central mechanism or non-obvious objective.
- Do not use `[[Vault Links]]` or other wiki links in mechanism labels.

Default structure:

```markdown
* Core Mechanism

  * **核心框架：<Framework Name>**：说明论文如何从核心问题转向该框架，以及框架的完整闭环。

    ![Framework](assets/NOTES.assets/framework.png)

    > [!NOTE]
    > **Figure 1. <Original caption or concise overview>.** 说明图中各分区的作用、闭环的连接关系，以及其余设计为何服务于该闭环。

    $$
    \text{Core framework objective}
    $$

    说明公式如何定义框架闭环，并只定义理解所需的关键符号。

    * **支撑能力一：<Capability Name>**：说明框架为何需要该能力，以及设计如何提供该能力。

      ![Mechanism figure](assets/NOTES.assets/mechanism.png)

      > [!NOTE]
      > **Figure 2. <Original caption or concise overview>.** 说明该图呈现的机制、模块间信息流及其证据边界。

    * **支撑能力二：<Capability Name with no dedicated figure>**：说明另一项必要能力及其设计。

      $$
      \text{Essential formula}
      $$

      说明该公式的输入、输出和机制作用。
```

### Figure and table callouts

- Every embedded image or table must be immediately followed by exactly one `> [!NOTE]` callout at the same indentation level as the image. Do not use a generic `>` blockquote or put the note before the image.
- The first content line of every NOTE must give an overview of what the image or table shows. Reuse the paper's original figure/table caption when possible; otherwise write a concise equivalent. For figures, follow it with a Chinese explanation of the meaningful regions or panels. For tables, follow it with the comparison, outcome, and necessary boundary.
- Use concrete anchors such as `**上方 Rollout stage**`, `**左侧整体平台**`, `**(b) Failure Simulation**`, or `**M row**` for the Chinese explanation after the overview sentence.
- Base the explanation on what the figure actually shows. Inspect the figure itself or its source PDF; do not infer panel positions from a caption alone.
- Explain the figure's role in the paper's argument. When a panel is only qualitative, distinguish what it demonstrates from what it does not establish.
- Keep a no-figure module explanation as normal prose, formula, or text. Do not add a NOTE that only says the paper has no separate mechanism figure.

### Experiment
- Placed as an independent parallel list item (`* Experiment` or `- Experiment`), directly following `Core Mechanism`.
- Indent prose or nested bullets under `* Experiment` with 2 spaces to maintain Typora list folding.
- Use task or benchmark figures when they materially explain difficulty, coverage, or evaluation conditions. Place each figure under its experiment item and follow it with a `> [!NOTE]` overview-and-explanation callout.
- Include the principal result-table images as local screenshots. Crop only the table and caption, preserving headers, all methods needed for comparison, and the proposed method's row. Readable quantitative results must not exist only as prose.
- Merge all discussion of the same experiment into one child bullet. State the setup and conclusion once under that bullet, then place its table image and single NOTE callout; do not create separate conclusion and table entries for the same experiment or repeat CarRacing, VizDoom, or another benchmark as duplicate experiments.
- Summarize ablations by the causal design driver and measured effect, not by reproducing every number.

### Pipeline
- **Use Mermaid flowchart instead of text lists**: Do NOT write a verbose `1. 2. 3.` numbered text list.
- Diagram the paper's actual core mechanism and decision path, not an idealized full system lifecycle. Include a training loop, feedback path, or deployment layer only when the paper implements or evaluates it.
- Default to `flowchart LR` for a long main path so the diagram stays wide and readable in Typora. Use `flowchart TD` when the process is genuinely hierarchical or has many vertical decisions.
- Keep one diagram focused on one core mechanism and its main path legible without zooming in Typora. Node count is not a hard limit; when a graph becomes difficult to scan, typically beyond roughly 16 nodes, merge nodes with the same responsibility or split it into multiple focused diagrams. Retain more nodes when the mechanism genuinely requires them and the layout remains clear.
- Use action-oriented, specific labels. Every decision node needs named branch conditions such as `Accepted` and `Fallback`, not generic `Yes` and `No` when the meaning can be stated directly.
- Group nodes by responsibility or evidence boundary with at most two nested subgraph levels. Use a small NOTE legend when one diagram combines the paper's evaluated method with explicitly labeled future integration; do not let a simple diagram accumulate explanatory prose.
- Keep Mermaid node text concise and ASCII/simple Chinese. Quote node text containing `|`, brackets, parentheses, or other punctuation that Mermaid may reserve; use `<br/>` for intentional line breaks.
- Distinguish data-derived thresholds or calibration regions from per-request runtime checks. A decision node should test the request-level score or membership in the precomputed region, not recompute dataset-wide FPR/FNR for each request.
- Do not invent training, feedback, retraining, graph updates, or enforcement modules merely to make the lifecycle look complete. If the paper does not implement them, omit them or place them in a clearly labeled future-scope subgraph.
- Use high-contrast node classes with explicit `color:` values. Consistent color semantics should distinguish ordinary processing, decisions, inputs/outputs, and future scope; color is supplemental, not the only way to communicate meaning.
- Include an `accTitle` and a concise `accDescr`, especially for diagrams that mix evaluated and proposed components.
- Must be indented under the parent `* Pipeline` (or `- Pipeline`) list item with 2 spaces so it folds properly in Typora.
- A single compact `> [!NOTE]` legend is allowed immediately after the diagram when it prevents scope or threshold ambiguity. Do not add numbered steps or repeat the mechanism narrative around the diagram.
- Validate the Mermaid syntax by rendering it before completion. Also inspect its aspect ratio and node/edge layout when a renderer is available; a valid but excessively tall or sparse diagram is not finished.
- Example:
  ```markdown
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
  ```

### Critical Thinking
- Merge `Pros`, `Cons`, and deep critical evaluation into a single unified `* Critical Thinking` (or `- Critical Thinking`) section.
- Indent all sub-points under `* Critical Thinking` with 2 spaces to maintain Typora list folding.
- Do not recap experiment results already stated in `Experiment`. Discuss strengths, failure modes, trade-offs, evidence boundaries, and future directions instead.
- Analyze the paper across the following five dimensions using high-density, technically rigorous bullets:

  1. **Pros**:
     - Concrete architectural or conceptual strengths only (2–3 concise bullets).
     - Do not repeat benchmark results, quantitative margins, or claims already stated in `Experiment`.
     - State the contribution boundary when the paper contrasts with neighboring work. A milestone contribution may be a novel combination or a scalable demonstration rather than a world-first mechanism; do not turn priority nuance into an unsupported novelty claim.
     - Add a `**Paradigm Demonstration**` bullet only for a milestone paper with verified evidence that later work adopted its core framework, problem formulation, or training loop as a reusable research direction. Explain the demonstrated paradigm and cite the concrete later work; do not infer paradigm status from novelty, popularity, or citation count alone. Omit this bullet for ordinary papers.

  2. **Cons**:
     - Do NOT write vague generic complaints (such as "hyperparameters are difficult to tune" or "discrete only").
     - Focus on concrete failure modes, breakdown conditions, and adversarial settings (2–3 precise, technically rigorous bullets):
       - What theoretical assumptions break down under non-ideal settings?
       - In what specific pathological scenarios, reward structures, or physical conditions does the algorithm fail or suffer severe degradation (e.g. relative overgeneralization in climbing games, bootstrap divergence, synchronization lag, topological fragmentation)?

  3. **Trade-offs**:
     - **What are the trade-offs made? Are the trade-offs made meaningful?**
       - Explicitly identify what the method sacrifices to gain its advantages (e.g., trading inference latency/memory/sample complexity for accuracy; trading decentralized autonomy for central coordination).
       - Critically assess whether these trade-offs are practically meaningful and worthwhile, or merely paper-driven compromises shifting the burden elsewhere.

  4. **Empirical Support**:
     - **Do experiments properly support the claims?**
       - Are baselines fair, representative, and properly tuned?
       - Does the evaluation benchmark realistically reflect the target problem, or is it tested on cherry-picked / synthetic setups?
       - Do ablation studies isolate the true causal drivers, or are performance gains overstated?
       - Assess evidence coverage, fairness, causal isolation, and boundary conditions. Do not restate the experiment outcomes.

  5. **Future Directions**:
     - **How can research go further along this direction?**
       - What is the logical next bottleneck to tackle?
       - How can future work relax restrictive assumptions, address primary failure modes, or advance this paradigm towards real-world application?

- Example structure:
  ```markdown
  * Critical Thinking

    * **Pros**:
      * [优势要点 1]
      * [优势要点 2]
      * **Paradigm Demonstration**：[仅里程碑论文保留；说明论文示范的范式，以及后续采用该范式的具体工作]
    * **Cons**:
      * **[劣势/失效要点 1]**：说明特定病态场景、理论假设破裂或性能断崖条件。
      * **[劣势/失效要点 2]**：说明维度扩展瓶颈或非理想物理约束下的退化机制。
    * **Trade-offs**:
      * [指出核心 trade-offs 并评估该置换在实际场景中是否合理且有意义]
    * **Empirical Support**:
      * [评估实验是否充分支撑论文 claims、baselines 是否扎实、是否存在消融盲区]
    * **Future Directions**:
      * [指出沿该方向进一步深入推进的真正突破口或关键解法]
  ```

## Formula and figure placement
- Place formulas directly under the mechanism point they explain
- Place figures directly under the explanation they support
- Use a separate `Math Formula` or `Figure Notes` section only when the nearby file already has a stable structure that requires it
- Do not create detached formula dumps or image galleries

## Citation style

Every summarized paper's metadata line must start with the full paper title in bold. Then give authors, venue, year, stable links, and the citation count. Never make the author list the first field or replace the title with a shorthand:

```markdown
**World Models**. David Ha, Jürgen Schmidhuber. **arXiv**, **2018**. [(Paper)](URL) [(Project)](URL) (Citations __N__)
```

Use the exact published title, preserving capitalization and punctuation. The complete title line above takes precedence over nearby notes that begin with authors.

Always append a citation count field for every summarized paper entry. The preferred local style is:

```markdown
[(Paper)](URL) [(S2)](URL) [(Code)](URL) (Citations __N__)
```

`(Citations __N__)` is mandatory, not optional. Replace `[(Paper)](...)` with a more specific label such as `[(Arxiv)](...)`, `[(DOI)](...)`, `[(Publisher)](...)`, or `[(OpenReview)](...)` when appropriate. If the citation count comes from Semantic Scholar, include the `[(S2)](...)` link when available. If Semantic Scholar is rate-limited or unavailable, use a reasonable fallback such as OpenAlex, Google Scholar snippets, Crossref, DBLP-connected pages, publisher pages, or another stable bibliographic/search source, then still write `(Citations __N__)`. Do not fabricate an `[(S2)](...)` link when the count did not come from Semantic Scholar.

Only if no citation count can be verified after reasonable fallback attempts, write `(Citations __unknown__)` in the entry and mention the failed sources in the final report. Do not omit the citation field.

For ordinary metadata fields, if a field cannot be verified after trying reasonable sources, omit that field rather than guessing; mention the gap briefly in the final report. Citation count is the exception: always include `(Citations __N__)` when verified, or `(Citations __unknown__)` if it truly cannot be verified.

## Source priority and fallback workflow

Use sources in this priority order:

1. The paper itself:
   - publisher or proceedings page
   - DOI landing page
   - OpenReview, ACL Anthology, CVF, DBLP, or another official repository page
   - arXiv abstract page, HTML, source files, or PDF
   - PDF or supplementary material linked from the paper page
2. Paper-adjacent primary materials:
   - official project page
   - official code repository
   - official appendix or supplementary material
3. High-quality auxiliary sources:
   - Semantic Scholar
   - author or lab posts
   - official project blogs
   - reputable technical explainers or videos
4. Everything else

The paper remains the sole ground truth for:

- contribution claims
- objective and method
- equations
- datasets and metrics
- reported results
- limitations and conclusions

Auxiliary sources may help interpretation, but must never override the paper.

## Allowed use of Semantic Scholar

Semantic Scholar is allowed as an auxiliary research tool.

Use it for:

- verifying title, authors, venue, year, and identifiers
- checking citation count as a rough context signal
- finding references, citations, and related papers
- quick relevance triage through metadata
- discovering neighboring work worth linking

Do not use Semantic Scholar as the primary basis for:

- the final summary
- the method explanation
- equations
- exact result claims
- limitations
- nuanced comparisons

Treat these Semantic Scholar signals as secondary only:

- TLDR
- auto-generated summaries
- inferred topics
- fields of study
- ranking or recommendation signals
- citation intent labels

If the note mentions Semantic Scholar-derived information, label it explicitly, for example:

- Semantic Scholar lists ...
- Semantic Scholar shows a citation count of ...
- Semantic Scholar recommends ...

## Allowed use of blogs and explainers

Blogs, videos, and explainer posts are allowed only after reading the paper.

Use them only to:

- improve intuition
- clarify a difficult mechanism
- explain a figure more accessibly
- infer likely implementation interpretation when the paper is terse
- collect better terminology for describing the method clearly

Prefer these auxiliary sources:

- posts by the paper authors
- the authors' lab or project site
- official project blogs
- reputable research organizations
- reputable engineering organizations
- strong technical explainers with named authors and references

Reject these sources:

- anonymous posts
- SEO-style content farms
- ad-driven summary pages
- sources with no author or no date
- sources with no traceable link to the paper
- sources whose claims cannot be checked against the paper

If a blog adds interpretation that is not explicit in the paper, label it as external context or intuition, not as part of the paper's stated claims.

## Strict workflow for selecting figures and formulas

Follow this workflow in order. Do not skip steps.

### Step 1: Identify the paper source

Start from the paper link in the target markdown note. The link may point to a publisher, proceedings, DOI, OpenReview, arXiv, institutional repository, or another reliable paper host.

When the supplied page links to HTML, source files, a PDF, or supplementary material, prefer the representation that preserves the paper's section structure, formulas, figures, and metadata most reliably. Use the publisher or official proceedings version when it is available; use an accessible preprint or repository copy when the official version is inaccessible or incomplete.

Do not rely on third-party summaries as the primary source.

### Step 2: Read before extracting

Before copying anything, read enough of the paper to identify:

- the capability the paper is trying to create, inferred from the Introduction, method, experiments, and Conclusion
- the paper's central framework or claim
- the relationship between that framework and its supporting designs
- the minimal end-to-end pipeline
- the equations without which the method is hard to understand
- the figures and tables that carry the paper's argument
- which details are implementation tricks versus load-bearing parts of the framework

Do not extract formulas or figures before understanding their role.

### Step 3: Figure selection and fetching rules

Only keep figures that satisfy at least one of these purposes:

- explain the overall architecture
- show the method pipeline
- clarify a key module or algorithm step
- show the task or evaluation setting when it explains the difficulty or scope
- demonstrate a central qualitative mechanism, such as controllable rollouts, failure detection, or counterfactual behavior
- summarize the main quantitative result when the result is central to the claim

There is no fixed one-figure rule. Include every figure that independently explains a core framework component or provides unique claim-bearing evidence. A paper may need several mechanism figures, a task figure, and a main-result table screenshot.

Do not keep:

- teaser images
- qualitative examples without clear explanatory value
- redundant ablation plots
- repeated tables or near-duplicate diagrams
- decorative or promotional figures

Default fetching rule:

- If the paper contains multiple distinct figures that reveal the core framework, a key mechanism, or unique evidence, fetch and embed each useful one locally instead of only mentioning it in prose.
- Prefer a compact set with no redundant images; the number is determined by explanatory value, not a fixed cap.
- Crop a table screenshot from the paper when the numerical comparison is central to the claim.
- Only skip figure fetching when the paper truly has no high-value figure, the figure is unreadable from available sources, or the user explicitly asks for a text-only summary.
- If you skip fetching, say briefly why.

### Step 4: Formula selection rules

Only keep formulas that are essential to understanding the paper.

Math delimiters are mandatory:

- Use inline math with `$...$` everywhere in prose.
- Put display math on its own lines between `$$` delimiters:
  ```markdown
  $$
  L = L_{\mathrm{task}} + \lambda L_{\mathrm{reg}}
  $$
  ```
- Never use LaTeX backslash-parenthesis or backslash-bracket delimiters for math, including inside summaries, explanations, or prose copied from another source.
- Use standard LaTeX commands such as `\boldsymbol{...}` and `\mathbf{...}`; do not use custom `\b`-prefixed macros.

Eligible formulas usually include:

- the core objective function
- the main update rule
- the scoring, matching, attention, or energy function
- the final loss if it defines the method
- one theorem statement only if the paper is primarily theoretical

Do not include:

- routine background formulas from prior work unless reused critically
- every intermediate derivation
- long proof steps
- notation-heavy expansions that do not change understanding
- appendix-only equations unless they are central

Hard limits:

- Include only formulas with a distinct explanatory role; no fixed count.
- More than three block formulas is acceptable when several irreducible objectives or stages genuinely require them.
- prefer one core formula plus one auxiliary formula over a long chain of equations

### Step 5: Extraction quality rules

When copying a figure:

- save it locally under `assets/<note-file-base>.assets/`
- use a stable descriptive filename when possible
- embed it with a relative markdown path
- extract the figure from the current paper's source or PDF; do not reuse a similarly named image from another note or an existing assets directory without checking that it depicts the same paper and the same claim
- place it under the mechanism point it explains
- immediately follow it with exactly one `> [!NOTE]` whose first content line gives the figure overview and whose Chinese explanation covers the meaningful panels or regions
- inspect the rendered figure or its source PDF before writing panel labels

When capturing a table:

- crop only the table and its caption, without unrelated body text
- preserve all rows and columns needed to verify the claim
- put setup and conclusion inside the table's single experiment bullet, then embed the principal table image
- immediately follow the image with exactly one `> [!NOTE]`; its first content line gives the table overview, followed by the comparison, outcome, and any essential boundary
- do not add an extra table-conclusion bullet or describe table cells as visual panels

When copying a formula:

- preserve LaTeX faithfully
- use `$...$` for inline math and standalone `$$` blocks for important equations
- never use LaTeX backslash-parenthesis or backslash-bracket delimiters
- after each important formula, add a short explanation of what it means
- define only the non-obvious symbols, not every symbol mechanically

### Step 6: Relevance test before keeping an item

For each candidate figure, table, or formula, ask:

- Does this help explain the takeaway?
- Does this clarify the research problem, core framework, a key mechanism, or experimental evidence?
- Would removing it make the note meaningfully worse?

If the answer is no to all three, do not include it.

### Step 7: Summarization-first rule

Write the research-problem and framework explanation first.
Then add figures, tables, and formulas where they provide evidence or eliminate a genuine explanatory gap.

The note must remain useful even if all figures are removed.
Figures and formulas support the argument, not replace it. Include multiple figures when each contributes unique understanding.

### Step 8: Repository-style constraints

Match local repository style:

- keep the note compact
- prefer explanation over transcription
- do not turn the note into a full paper dump
- preserve Typora-friendly markdown
- keep local assets near the note
- follow nearby `Paper-Reading` examples before inventing a new layout

### Step 9: Final conciseness review

After completing the summary, reread the entire note once as a compact review note:

- Remove repeated statements between `Takeaway`, `Motivation`, `Core Mechanism`, and `Pipeline`.
- Keep only problems, frameworks, mechanisms, formulas, figures, tables, and critical thinking points that materially improve understanding.
- Check that `Takeaway` is strictly English and uses either a plain-text compositional formula or one or two sentences, with no code ticks, quotes, wrapping, or `Lineage` section.
- Check that `Motivation` states the unresolved capability gap and paper objective, not just prior-work defects or the paper's achieved result.
- Check that the core-problem sentence does not read as a completed claim. Move an intended ability into the paper objective when removing it makes the problem statement still valid.
- Check that `Core Mechanism` starts with the central framework, nests its figure/formula below it, and puts supporting modules under `支撑能力` rather than as peer items.
- Check that `Pipeline` describes the paper's actual mechanism, keeps a readable LR main path where appropriate, and does not imply unevaluated modules were implemented or validated.
- Check that every framework module has a mechanism explanation and an original figure or formula/text where a figure is unavailable.
- Check that each image/table is immediately followed by exactly one `> [!NOTE]`, with an overview first and no orphan no-figure NOTES.
- Check that the same experiment appears once, the principal result tables are embedded, and `Critical Thinking` does not recap experiment results.
- Check that inline math uses `$...$`, display math uses standalone `$$` blocks, and no alternative LaTeX delimiter remains.
- Remove unsupported details, unnecessary notation, long derivations, and low-value background.
- Confirm that the note remains understandable without the figures or auxiliary sources.

## PDF-only fallback workflow

If HTML or source files are unavailable or poor, use this strict PDF-first fallback:

1. Read in this order:
   - title
   - abstract
   - introduction
   - conclusion or discussion
2. Write a provisional summary before deeper extraction:
   - missing capability and paper objective
   - central framework and its supporting components
   - main result
   - stated limitation
3. Scan all figures and tables before reading methods in detail.
4. Keep only claim-bearing visuals:
   - the central framework or pipeline
   - distinct mechanism figures that explain how the framework works
   - task or testbed figures needed to understand difficulty and scope
   - the main result table or figure, plus a key ablation only when it changes the conclusion
5. Read only the body paragraphs needed to explain the kept visuals.
6. Extract equations only after the core claims and kept visuals are already known.
7. Keep only equations that are essential:
   - one core objective or definition
   - one update, inference, or scoring equation if necessary
   - one nonstandard metric or constraint only if results depend on it
8. For every important claim, record:
   - claim
   - evidence location
   - limitation or boundary
9. Paraphrase by default:
   - never paste the full abstract
   - never dump long captions
   - never copy long derivations
   - never copy proof-heavy blocks into the note
10. If PDF parsing quality is poor, keep only high-confidence claims supported by multiple parts of the paper.

## Figure and formula checklist

Before finishing, verify:

- a final conciseness review was completed after drafting
- the number of figures and formulas follows explanatory need, with no redundant items
- every kept figure or table has a clear explanatory purpose and an immediately following `> [!NOTE]`
- the first content line of each NOTE gives an overview and reuses the original paper caption where practical
- every embedded figure has a panel-level Chinese explanation after its overview
- every embedded result table has one NOTE covering comparison, outcome, and essential boundary
- the principal result-table image is embedded and readable, not only summarized in prose
- each framework module has a mechanism explanation; missing dedicated figures are covered by formulas or text, not empty NOTES
- every kept formula supports the mechanism directly
- all assets are saved locally with relative paths
- formulas sit under the relevant mechanism points, nested beneath the owning list item
- inline math uses `$...$`, display math uses standalone `$$` blocks, and no alternative LaTeX delimiter remains
- all distinct claim-bearing figures and tables that materially improve the note are represented
- the same experiment is not split into duplicate entries or repeated across benchmarks
- `Critical Thinking` does not restate experiment outcomes
- `Pipeline` is a validated Mermaid diagram with specific actions and named branches; any immediately following NOTE is a compact scope legend rather than repeated prose
- the prose summary still stands on its own without the raw paper

## Required asset placement

When saving figures or cropped tables for a note:

- put them under `assets/<note-file-base>.assets/`
- reference them with a relative markdown path matching nearby file style, such as `assets/<note-file-base>.assets/<image-file>` or `./assets/<note-file-base>.assets/<image-file>`

Match the repository's existing local asset pattern.

## Must do

1. Read the target markdown note and extract the paper link.
2. Inspect nearby notes in the same directory for stable formatting conventions; preserve user-specific formatting choices unless the user asks to change them.
3. Verify citation metadata and citation count from the supplied paper page and reliable bibliographic sources, then write a metadata line that starts with the full paper title in bold, followed by authors, venue, year, links, and citation count.
4. Verify and write a citation count for every summarized paper entry as `(Citations __N__)`; if no count can be verified after reasonable fallbacks, write `(Citations __unknown__)` and report the attempted sources.
5. Infer the missing capability and paper objective, then state the central framework before its supporting designs.
6. Put the framework figure and formula under `核心框架` and nest every module capability under `支撑能力`; explain each module with a figure, formula, or precise text.
7. Summarize the paper in Chinese-dominant mixed-language style with an English-only `Takeaway`, indenting every image, formula, NOTE, and Mermaid block under its owning list item.
8. Preserve the paper's most important formulas with `$...$` inline math and standalone `$$` display blocks directly under the relevant mechanism points.
9. Save and embed claim-bearing mechanism figures and the principal result-table images locally into the matching `assets/<note>.assets/` folder when the source is usable.
10. Immediately follow every image or table with exactly one `> [!NOTE]`; start with an overview, then give the figure or table explanation without duplicating experiments.
11. For a milestone paper only, add `Paradigm Demonstration` under `Critical Thinking` after verifying that later work adopted its framework, problem formulation, or training loop; omit it when that evidence is absent.
12. Reread the completed note, run the completion validation below, and inspect the title, images, formulas, and tables in Typora.

## Must not do

- Do not use Chinese in the Takeaway section (Takeaway must be strictly in English)
- Do not wrap the Takeaway formula in backticks, quotation marks, or a fenced block
- Do not turn `Motivation` into a list of prior-work defects without stating the missing capability and paper objective
- Do not present implementation tricks as peer contributions when they primarily support one central framework
- Do not use `[[Vault Links]]`, wiki links, or other concept-link syntax
- Do not include a `System Model & Assumptions` subsection
- Do not dump the whole abstract or whole paper into the note
- Do not begin the metadata line with an author list or omit the full bold paper title
- Do not include formulas that are not central to the method
- Do not use LaTeX backslash-parenthesis or backslash-bracket delimiters for math
- Do not move key formulas into a detached section when they belong under a specific mechanism point
- Do not include decorative or redundant figures
- Do not leave a framework figure, formula, NOTE, or Mermaid block outside its owning list hierarchy
- Do not omit a module's mechanism explanation or add a NOTE only to say no dedicated figure exists
- Do not stop at prose-only `Figure Note` entries when a useful figure or table can be saved locally
- Do not embed an image or table without its immediately following NOTE
- Do not split one experiment into duplicate conclusion/table entries or repeat the same benchmark as separate experiments
- Do not recap experiment results in `Critical Thinking`
- Do not label an ordinary paper as a paradigm or add `Paradigm Demonstration` based only on novelty, popularity, or citation count
- Do not present a field-changing claim without a verified concrete successor or adoption example
- Do not add numbered steps or extended prose under `Pipeline`; one compact NOTE legend is allowed when it resolves a real scope or threshold ambiguity
- Do not let Semantic Scholar or a blog override the paper
- Do not hotlink random images if a stable local copy can be saved
- Do not break existing relative paths or nearby note conventions
- Do not rewrite or remove existing frontmatter, title, TOC, or unrelated note scaffolding without a task-specific reason
- Do not overwrite unrelated note content

## Completion validation

Do not report completion until all checks pass:

1. The metadata line begins with the exact full title in bold and includes authors, venue, year, verified links, and the citation field.
2. The core problem states an unresolved capability gap, names its relevant constraints, and passes the completed-outcome test; the proposed capability appears in the paper objective or mechanism instead.
3. Any novelty or priority claim names its scope and is supported by the paper or verified later work; do not claim a broader first than the evidence allows.
4. `Core Mechanism` nests the framework figure/formula and `支撑能力` modules correctly; no module is a peer of `核心框架`.
5. Every framework module has a mechanism explanation, and no empty no-figure NOTE exists.
6. Every image and table is immediately followed by exactly one correctly indented `> [!NOTE]`, with an overview as its first content line.
7. Every local asset path resolves to an existing file under the paper's `assets/` directory.
8. The principal result-table images are present; each experiment appears once and is not duplicated.
9. Inline math uses `$...$`, display math uses standalone `$$` blocks, and no alternative LaTeX delimiter remains.
10. `Critical Thinking` contains no recap of experiment results.
11. `Paradigm Demonstration` appears only for a verified milestone paper and names concrete later work that adopted the paradigm; ordinary papers omit it.
12. Render the Pipeline Mermaid source successfully and inspect its composition, then open the completed note in Typora and visibly confirm that the full title, images, NOTE callouts, inline/display formulas, result tables, and Mermaid diagram render correctly and remain nested under their sections.

## Final grounding rule

The final note must still stand on its own if all auxiliary sources are removed.

Auxiliary sources may improve understanding, but the final summary must remain grounded in the paper itself.
