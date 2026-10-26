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

  ...

* Experiment

  * Claim-bearing testbed or task figure, with part-by-part callout explanation.
  * Concise table purpose and outcome, followed by the table image.

* Pipeline

  ...

* Critical Thinking

  * **Pros**: ...
  * **Cons**: ...
  * **Trade-offs**: ...
  * **Empirical Support**: ...
  * **Future Directions**: ...
```

- `Takeaway` must be written strictly in English. Keep only a compact compositional formula when one clearly captures the method; otherwise use one or two concise sentences. Render the formula as plain text, without backticks, quotation marks, or other wrapping.
- `Motivation`, `Core Mechanism`, `Experiment`, `Pipeline`, and `Critical Thinking` should use the same `* Section Name` (or `- Section Name`) list-item format.
- Indent prose, nested bullets, formulas, figures, and code/mermaid blocks under their parent section (2 spaces) so the list structure remains foldable in Typora.

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
- State the **core problem** as a missing capability: what can the target model or system not do today, and why does that matter?
- Explain why existing routes cannot provide that capability. Typical routes include imitation, offline RL, direct online interaction, additional supervision, or stronger models; choose only routes relevant to the paper.
- State the **paper objective** as the framework or capability the work aims to build.
- Keep this section to 3–4 concise bullets. The nature of the problem may require inference from the Introduction, experiments, and Conclusion; label interpretation when the paper does not state it verbatim.

### Core Mechanism
- Identify the paper's central framework before listing implementation choices. State the capability it creates and the complete operating loop that makes that capability possible.
- Present the central framework first. Then present supporting capabilities or designs as second-level mechanism points. The hierarchy should make clear what is the paper's core claim and what exists to make that claim work.
- Use a named framework when the paper provides one. For a system paper, prefer Chinese labels such as `核心框架：<Framework Name>`, `支撑能力一：<Capability>`, and `支撑能力二：<Capability>` when this hierarchy is genuinely useful; do not force those exact labels onto a paper with another natural organization.
- Do not reduce the section to a flat list of modules, losses, architecture names, or engineering tricks. Explain how each design enables the framework and why it is necessary.
- Do not split points into `What`, `Why`, and `How` subsections.
- Place each figure inside the mechanism point it explains. Use multiple figure callouts when a paper has several claim-bearing visuals, such as task setup, architecture, qualitative mechanism behavior, and training loop. Do not use a fixed one-figure limit.
- Put formulas immediately below the point they explain. Keep only formulas needed to understand the central mechanism or non-obvious objective.
- Do not use `[[Vault Links]]` or other wiki links in mechanism labels.

Default structure:

```markdown
* Core Mechanism

  * **核心框架：<Framework Name>**：说明论文如何从核心问题转向该框架，以及框架的完整闭环。

    ![Framework](assets/NOTES.assets/framework.png)

    > **<图中分区 1>**：说明该分区的作用及其在闭环中的位置。
    >
    > **<图中分区 2>**：说明另一分区的作用及两部分如何衔接。
    >
    > **为什么这是核心框架**：说明其余设计为何服务于该闭环，而不是并列贡献。

  * **支撑能力一：<Capability Name>**：说明框架为何需要该能力，以及设计如何提供该能力。

    ![Mechanism figure](assets/NOTES.assets/mechanism.png)

    > **(a) 图中分区标题**：说明该分区呈现的机制。
    >
    > **(b) 图中分区标题**：说明其意义与证据边界。

  * **支撑能力二：<Capability Name>**：说明另一项必要能力及其设计。
    $$
    \text{Essential formula}
    $$

  * **<衔接或更新机制>**：说明前文组件如何转化为策略或系统更新。
```

### Figure callouts

- Every substantial figure embedded in the note should be followed by a blockquote callout that explains its meaningful regions or panels, not merely its overall caption.
- Start each callout item with a bold, concrete anchor such as `**上方 Rollout stage**`, `**左侧整体平台**`, `**右下 Box Closing**`, or `**(b) Failure Simulation**`.
- Use `>` blockquotes for figure explanation so the image and interpretation remain visually associated.
- Base the explanation on what the figure actually shows. Inspect the figure itself or its source PDF; do not infer panel positions from a caption alone.
- Explain the figure's role in the paper's argument. When a panel is only qualitative, distinguish what it demonstrates from what it does not establish.

### Experiment
- Placed as an independent parallel list item (`* Experiment` or `- Experiment`), directly following `Core Mechanism`.
- Indent prose or nested bullets under `* Experiment` with 2 spaces to maintain Typora list folding.
- Use task or benchmark figures when they materially explain difficulty, coverage, or evaluation conditions. Place each figure under a concise explanation and provide a `>` panel-by-panel callout.
- Include key comparison tables as local screenshots when the table itself is easier to inspect than a prose transcription. Crop only the table, preserving its caption, headers, all methods, and the proposed method's row.
- Do not describe a table like a figure. For a table, write only:
  - what experiment or comparison it performs;
  - the overall result and the most important margin over the strongest relevant baseline;
  - one essential boundary or anomaly when it changes interpretation.
- Put the concise table conclusion before the table image. Do not add `>` callouts for tables.
- Summarize ablations by the causal design driver and measured effect, not by reproducing every number.

### Pipeline
- **Use Mermaid flowchart instead of text lists**: Do NOT write a verbose `1. 2. 3.` numbered text list.
- Present the end-to-end operational process primarily as a clean, compact Mermaid diagram (`flowchart TD` or `flowchart LR`).
- Diagram covers the full lifecycle: Input/Observation -> Model/Decision -> Buffer/Feedback -> Loss/Update -> Target Sync.
- Keep Mermaid node text concise and ASCII/simple Chinese (avoid special punctuation inside node shapes to ensure rendering stability).
- Must be indented under the parent `* Pipeline` (or `- Pipeline`) list item with 2 spaces so it folds properly in Typora.
- Do not add `>` callouts, prose notes, numbered lists, or explanatory paragraphs around or below the diagram. Put required context into the mechanism section or concise Mermaid nodes.
- Example:
  ```markdown
  * Pipeline

    ```mermaid
    flowchart LR
        Obs[Local Obs] --> Net[Agent Net]
        Net --> Act[Action Selection]
        Act --> Env[Environment]
        Env --> Buf[(Replay Buffer)]
        Buf --> Loss[TD Loss & Target]
        Loss --> Update[Parameter Update]
    ```
  ```

### Critical Thinking
- Merge `Pros`, `Cons`, and deep critical evaluation into a single unified `* Critical Thinking` (or `- Critical Thinking`) section.
- Indent all sub-points under `* Critical Thinking` with 2 spaces to maintain Typora list folding.
- Analyze the paper across the following five dimensions using high-density, technically rigorous bullets:

  1. **Pros**:
     - Concrete strengths and verified contributions only (2–3 concise bullets).
     - Focus on proven performance improvements, architectural elegance, or theoretical breakthroughs.

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

Prefer this citation format for new entries:

```markdown
- **Paper Title**. Author1 Author2 et.al. **Venue**, **Year**, ([link](URL)).
```

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
- follow it with a `>` callout covering the meaningful panels or regions
- inspect the rendered figure or its source PDF before writing panel labels

When capturing a table:

- crop only the table and its caption, without unrelated body text
- preserve all rows and columns needed to verify the claim
- place the concise purpose-and-result sentence before the image
- do not use `>` panel callouts for a table

When copying a formula:

- preserve LaTeX faithfully
- use block math for important equations: `$$...$$`
- use inline math only for short symbols in prose
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
- Check that `Motivation` states the missing capability and paper objective, not just prior-work defects.
- Check that `Core Mechanism` starts with the central framework and clearly subordinates implementation designs.
- Check that `Pipeline` is a clean Mermaid flowchart with no `>` callouts or explanatory prose.
- Check that each figure has a panel-level `>` explanation and each table has only a concise purpose-and-result explanation.
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
- every kept figure has a clear explanatory purpose
- every embedded figure has a panel-level `>` explanation
- every embedded result table has a concise purpose-and-result sentence before it
- every kept formula supports the mechanism directly
- all assets are saved locally with relative paths
- formulas sit under the relevant mechanism or pipeline points by default
- all distinct claim-bearing figures and tables that materially improve the note are represented
- `Pipeline` contains only its Mermaid diagram
- the prose summary still stands on its own without the raw paper

## Required asset placement

When saving figures or cropped tables for a note:

- put them under `assets/<note-file-base>.assets/`
- reference them with a relative markdown path matching nearby file style, such as `assets/<note-file-base>.assets/<image-file>` or `./assets/<note-file-base>.assets/<image-file>`

Match the repository's existing local asset pattern.

## Must do

1. Read the target markdown note and extract the paper link.
2. Inspect nearby notes in the same directory for stable formatting conventions; preserve user-specific formatting choices unless the user asks to change them.
3. Verify citation metadata and citation count from the supplied paper page and reliable bibliographic sources, then inject them into the note entry.
4. Verify and write a citation count for every summarized paper entry as `(Citations __N__)`; if no count can be verified after reasonable fallbacks, write `(Citations __unknown__)` and report the attempted sources.
5. Infer the missing capability and paper objective, then state the central framework before its supporting designs.
6. Summarize the paper in Chinese-dominant mixed-language style with an English-only `Takeaway`, following the default section order unless stable nearby conventions require an adaptation.
7. Preserve the paper's most important formulas and place them directly under the relevant mechanism points.
8. Save and embed claim-bearing figures and table crops locally into the matching `assets/<note>.assets/` folder when the source is usable.
9. Explain every embedded figure region by region with `>` callouts and every result table concisely by purpose and outcome.
10. Reread the completed note for insight hierarchy, unsupported claims, redundancy, and formatting compliance.

## Must not do

- Do not use Chinese in the Takeaway section (Takeaway must be strictly in English)
- Do not wrap the Takeaway formula in backticks, quotation marks, or a fenced block
- Do not turn `Motivation` into a list of prior-work defects without stating the missing capability and paper objective
- Do not present implementation tricks as peer contributions when they primarily support one central framework
- Do not use `[[Vault Links]]`, wiki links, or other concept-link syntax
- Do not include a `System Model & Assumptions` subsection
- Do not dump the whole abstract or whole paper into the note
- Do not include formulas that are not central to the method
- Do not move key formulas into a detached section when they belong under a specific mechanism point
- Do not include decorative or redundant figures
- Do not stop at prose-only `Figure Note` entries when a useful figure or table can be saved locally
- Do not describe a table with panel-level callouts; keep table discussion to experiment purpose and outcome
- Do not add `>` callouts, prose, or numbered notes under `Pipeline`
- Do not let Semantic Scholar or a blog override the paper
- Do not hotlink random images if a stable local copy can be saved
- Do not break existing relative paths or nearby note conventions
- Do not rewrite or remove existing frontmatter, title, TOC, or unrelated note scaffolding without a task-specific reason
- Do not overwrite unrelated note content

## Final grounding rule

The final note must still stand on its own if all auxiliary sources are removed.

Auxiliary sources may improve understanding, but the final summary must remain grounded in the paper itself.
