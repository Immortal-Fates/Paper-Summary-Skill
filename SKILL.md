---
name: paper-summary
description: Summarize a paper into a concise, insight-led Typora-friendly markdown note with Takeaway, Contribution, Motivation, Core Mechanism, Pipeline, Experiment, and Critical Thinking.
---

## What I do

This skill transforms a reliable paper link into a structured, insight-led paper summary in Typora-friendly markdown.

Summaries are written in Chinese-dominant mixed-language style across all sections (preserving English technical proper nouns inside concise Chinese prose). The note opens with `Takeaway` and `Contribution` for immediate executive orientation, defines the unresolved problem in `Motivation`, establishes the `Core Mechanism` followed immediately by its runtime `Pipeline` (captured Algorithm diagram or Mermaid), delivers experimental evidence in `Experiment`, and concludes with rigorous `Critical Thinking`.

## Core conventions

- **Source grounding & anti-fabrication**: Every equation, symbol, complexity bound, hardware spec, and numerical claim must come directly from the paper's ground-truth source (`source/` LaTeX or PDF). Never invent synthetic `\underbrace` equations, fake summations, or unverified metrics just to fill a template slot; when the paper states an inequality, scaling bound, or recurrence instead of a multi-term loss, present the paper's actual formulation faithfully.
- **Strict 1-sentence per point rule & no meta-prefixes**: Every bullet point across `Contribution`, `Motivation`, `Core Mechanism`, `Experiment`, and `Critical Thinking` must be strictly limited to **exactly 1 concise sentence** (target ~30–60 Chinese characters, stating underlying causality directly; no semicolon-chained compound sentences or vacuous filler). Never drop essential operators, tensor shapes, or quantitative bounds merely to force a shorter character count, and never leak meta-instruction prefixes into the note (e.g., strictly forbid phrases like `单句说明……：`, `一句话概括……：`, `单句总结……：`).
- **On-demand `>` explanation blocks (Self-contained readability)**: Keep main bullets to 1 crisp sentence for fast scanning, and place an indented plain `>` blockquote underneath **only when a reader unfamiliar with the paper faces a conceptual leap or hidden derivation** (such as *why* memory scales as $2bns^2$ in `Motivation`, how an inequality like $c \ge F/B$, `Online Softmax` rescaling, or backward recomputation works in `Core Mechanism`, or why a failure mode occurs in `Critical Thinking`). Explain in plain, accessible Chinese with simple source-grounded math or analogies, and prefer three high-clarity techniques inside `>` when explaining streaming or multi-step compute:
  1. *Concrete toy-dimension sandbox*: Anchor abstract dimensions on small concrete numbers (explicitly labeled as an illustrative example, e.g., $P=4, s=4096, d=64, c=1024$) so tensor shapes and memory counts are immediately concrete.
  2. *Step-by-step recurrence (`**Step 1**`, `**Step 2**`, ...)*: Break iterative operators and backward recomputation into short labeled steps with `←` update equations (one clean `$$...$$` per step inside `>`) instead of packing multiple recurrences into dense prose or one wide line.
  3. *Buffer allocation & reuse lifecycle*: For memory bounds (e.g., $6bch$), categorize tensors by lifecycle—static resident states, async double-buffers, and on-chip scratchpad buffers overwritten/discarded after each step.
  **Selective `>` scope (do NOT force under every bullet)**: omit `>` on `Takeaway`, `Contribution`, `Experiment` (already paired with `> [!NOTE]`), and routine/off-the-shelf components (`Encoder`, standard `MLP`, etc.). However, **core or novel `Component`s proposed by the paper are NOT exempted as self-explanatory**: unpack them via an indented equation/operator breakdown or a `>` block detailing the input → transformation → output flow and design rationale; always separate a plain `>` block from `> [!NOTE]` so Markdown never merges them.
- **English captions with Chinese explanations**: All bullet captions must be in English Title Case (e.g., `**Core Problem**:`, `**Core Framework**:`, `**Component**:`, `**Failure Mode**:`); the explanatory prose remains concise Chinese-dominant mixed-language.
- **Preserve English for technical proper nouns**: All technical terms, module names, architecture components, algorithms, loss functions, parallelism strategies, benchmark names, and core theoretical constructs (e.g., `Encoder`, `Decoder`, `Vector Quantizer`, `Codebook`, `Straight-Through Estimator (STE)`, `Posterior Collapse`, `Self-Attention`, `FeedForward`, `Online Softmax`, `Tensor / Sequence / Data Parallelism`, `Key-Value Block`, `Causal Mask`, `Full / Mixed Precision`, `Diffusion`, `Latent Space`) must strictly remain in English throughout the text. Never translate them into awkward or localized Chinese phrases (e.g., strictly use "Vector Quantizer", never "离散码本量化器"; use "Encoder / Decoder", never "编码器 / 解码器"; use "Blockwise FeedForward" / "Tensor Parallelism", never "分块前馈网络" / "张量并行").
- **Micro-mechanism transparency**: Ban abstract, vacuous filler phrases (such as "提取高层表征", "压缩信息瓶颈", "通过优化实现目标", "实现无损全局局部累加"). Every mechanism must penetrate to the **paper-faithful operator and physical-boundary level**:
  1. *Concrete operators & execution tricks*: State the exact mathematical operation, rescaling rule, or communication primitive present in the paper (e.g., forward quantization with STE via $z = z_e + \text{sg}[z_q - z_e]$, or `Online Softmax` log-sum-exp rescaling overlapped with P2P `KV` transfer).
  2. *Counterfactual purpose or physical bottleneck*: For multi-term losses, state which parameters each term updates and what degeneration $\text{sg}$/regularizers prevent; for systems/parallelism papers, state the exact bottleneck inequality or threshold (e.g., arithmetic intensity $c \ge F/B$ and minimum per-device length $s = 6c$ required to hide communication).
  3. *Explicit tensor shapes, memory bounds & granularity*: Clearly state data representations or resource footprints (e.g., $H \times W \times D$ feature grids, discrete 1D token sequences, or per-layer activation memory bound $6bch$).
- **Mathematical Transparency & Step-by-Step Derivation Protocol (数学透明度与推导协议，严禁符号堆砌与跳步)**:
  1. *Zero Undefined Symbols Rule (零裸定义符号律)*: 凡在公式中首次出现的关键矩阵、向量或参数（如 $\mathbf{Q}_t$、$\overline{\mathbf{Q}}_t$、$\mathbf{x}$、$\odot$），必须显式给出其张量集合与维度（如 One-Hot 行向量 $\mathbf{x} \in \{0,1\}^K$、行随机方阵 $\mathbf{Q}_t \in [0, 1]^{K \times K}$），解释微观元素定义与物理含义（如 $[\mathbf{Q}_t]_{ij} \triangleq q(x_t=j \mid x_{t-1}=i)$ 表示单步条件跃迁概率），并阐明代数运算对应的物理动作（如“行向量左乘矩阵 $\mathbf{x}_{t-1}\mathbf{Q}_t$ 在代数上正好抽取出第 $i$ 行概率分布”）。
  2. *Mandatory Step-by-Step Derivation Chain (核心后验与递推公式强制分步展开律)*: 严禁将复杂的条件后验、损失上界或更新规则单行一揽子给出（One-line Formula Dump）。凡涉及非显而易见的贝叶斯推导、动态规划递推或变分证明（如 $q(\mathbf{x}_{t-1} \mid \mathbf{x}_t, \mathbf{x}_0)$、DPO 闭式替换、隐式打分方差界），必须在缩进的 `>` 块中写出完整的四步推导链：
     - **Step 1: 第一性原理出发点**（如贝叶斯全概率展开）；
     - **Step 2: 结构化假设化简**（如马尔可夫一阶条件独立性消去变量）；
     - **Step 3: 向量化/算子代数变换**（详细说明为何出现矩阵转置 $\mathbf{Q}^T$、为何出现逐元素 Hadamard 积 $\odot$ 而非普通矩阵乘法）；
     - **Step 4: 归一化分母的物理本质**（说明分母点积标量如何起到全概率归一化常数配分函数的作用）。
  3. *Loss Multiplier & Boundary Grounding (损失加权项与系数的数学起源解析)*: 对于目标函数中的关键系数、时间衰减项或缩放常数（如 LLaDA 目标中的 $1/t$、VRPO 方差界中的 $\frac{1}{4}$），必须交代其数学推导来源（如 $1/t$ 来自连续时间 MDM 调度函数 $\frac{-\dot{\alpha}}{1-\alpha}$；$\frac{1}{4}$ 来自 Sigmoid 导数的全局极大值），并说明在极值边界（$t \to 0$ 或 $t \to 1$）该系数对模型产生了什么物理优化偏置。
  4. *Brevity applies to prose, never to mathematical logic (精炼适用于修辞，绝不容许省略数学逻辑)*: 笔记的“精炼”旨在剔除空洞套话，绝不容许以“篇幅精简”为借口跳过数学推导桥梁。必须保证具备基础线性代数与概率论背景的读者，无需翻阅原论文即可顺畅推通全部公式逻辑。
- **Deterministic Figure Selection via Caption & Citation Protocol (基于 Caption 与章节引用的确定性选图协议，彻底免除肉眼盲猜)**:
  1. *Automated Caption & Label Inventory (图表全量清单扫描)*: 选图前必须使用 `python3 scripts/extract_assets.py scan-figures --source <dir|file>` 自动提取全量图表清单（提取图号、文件路径、Label、Caption、定义与首次引用的 Section）。
  2. *Section Citation Priority (方法章节引用最高优先级)*: 在方法论章节（`\section{Method}`、`\section{Approach}`、`\section{Architecture}`）中首次被 `\ref{fig:...}` 引用的总览图拥有绝对最高优先级，必须直接作为 `Core Framework` 的配图（例如 LLaDA 在 Approach 开篇引用的 `Fig.~\ref{fig:overview}` 对应 `imgs/overview.pdf`，而非前言的实验对比图）。
  3. *Caption Keyword Whitelist & Hard Blacklist (关键词白名单与绝对黑名单)*:
     - **Core Framework 白名单**: Caption 含有 `Overview`, `Architecture`, `Framework`, `Pipeline`, `Diagram`, `Workflow`, `Generator`, `Sampling Process`, `Training Process`；
     - **Core Framework 绝对黑名单 (Hard Ban)**: **严禁将 Caption 含有以下词汇的图放入 `Core Mechanism`**: `Benchmark`, `Comparison`, `vs.`, `Accuracy`, `Ablation`, `Scaling Curves`, `Results`, `Evaluation`, `Scatter`, `Loss`。一旦命中黑名单，该图只能放入 `* Experiment`。
  4. *Caption-Forced NOTE Rule (NOTE 标题强绑定)*: `> [!NOTE]` 的第一行粗体概览必须直接复用解析得到的真实 `\caption` 原文（如 `**Figure 2. Overview of LLaDA.**`），消除杜撰，并在结构上杜绝文不对题。
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
**<Full Paper Title>**. <Author 1, Author 2, Author 3 | First Author et al.> (<Affiliation / Research Team>). **<Venue>**, **<Year>**. [(Paper)](URL) [(Project)](URL) (Citations __N__)

* Takeaway

  通过 Straight-Through Estimator (STE) 将连续 Latent Space 分布替换为离散可学习的 Codebook，从根本上消除了 VAE 中的 Posterior Collapse。

* Contribution

  <用 1 句高站位中文直接定性论文在技术树与学科领域中的核心学术定位与宏观贡献（若为里程碑论文，直接指明其开创/确立的全新 Research Paradigm 或根本性突破；普通论文则定性其解决的关键 Challenge 或提供的核心 Solution，避免矮化为局部实现细节）。>

* Motivation

  * **Core Problem**: <以约 30–60 字中文直击底层能力鸿沟与核心痛点；严禁描述论文已达成的方案。>

    > <按需补充通俗解释、直觉类比或简短公式推导（仅在存在理解门槛或隐藏推导时添加，避免无差别复读）。>
  * **Why Existing Routes Fail**: <以约 30–60 字中文说明现有替代路线为何在机理上无法提供该能力。>

* Core Mechanism

  * **Core Framework: <Framework Name>**: <概括完整闭环，并明确列出系统由哪几部分组成（如 Encoder-Decoder、Learnable Codebook 及 Prior 阶段）。>

    ![Framework](assets/<note-file-base>.assets/framework.png)

    > [!NOTE]
    > **Figure 1. <Original caption or concise overview>.** **Left: Architecture** <说明前向与反向信息流>；**Right: Embedding Space** <说明特征与码字更新>。

    $$
    \mathcal L = \underbrace{-\log p_\theta(x\mid z_q)}_{\mathcal L_{\mathrm{rec}}} + \underbrace{\|\operatorname{sg}[z_e]-z_q\|_2^2}_{\mathcal L_{\mathrm{codebook}}} + \underbrace{\beta\|z_e-\operatorname{sg}[z_q]\|_2^2}_{\mathcal L_{\mathrm{commit}}}
    $$

    第 1 项优化重构质量，第 2 项将 Codebook 码字拉向连续编码输出，第 3 项通过 Commitment loss 防止连续表征在潜空间发散漂移。

    * **Learnable State: <Codebook / Memory>**: <定义参数集合与超参数（如 $\mathcal C=\{e_1,\dots,e_K\}, e_k\in\mathbb R^D$），说明 $K$（词表容量）与 $D$（通道对齐）的物理意义及更新机制。>
    * **Component: <Core / Novel Module With Operator Trick>**: <1 句概括该核心模块在整套闭环中的职责与作用边界。>
      * **Forward Operation**: <给出空间网格坐标 $(i, j)$ 或具体张量的匹配/变换算子（如 $k^*=\arg\min_k \|z_e^{(i,j)}-e_k\|_2^2 \implies z_q^{(i,j)}=e_{k^*}$）。>
      * **Backward Trick (STE)**: <解释直通算子（如 $\operatorname{sg}(x)=x, \partial \operatorname{sg}/\partial x=0 \implies \partial z_q/\partial z_e \approx I$）如何复制梯度绕过不可导阶跃。>
    * **Component: <Core / Novel Module Requiring Explanation>**: <1 句概括该核心模块的输入输出形态与核心计算职责。>

      > <核心/新颖 Component 必须附带机理展开：写清输入 → 算子变换 → 输出的张量/图结构变化、对应公式如何计算，以及为何采用该设计（例如使用沙盘维度或分步递推）。>
    * **Component: <Standard Backbone / Routine Module>**: <常规或标准组件仅保留 1 句职责与接口说明，不强行附带冗余解释块。>
    * **Stage 2: <Autoregressive Prior / Generation>**: <说明冻结离散特征后如何用自回归模型拟合联合概率分布解决 Next-Token 预测。>

      $$
      \underbrace{z\sim p_\psi(z)}_{\text{Prior 采样 Tokens}} \longrightarrow \underbrace{e_z}_{\text{Codebook Lookup}} \longrightarrow \underbrace{\hat x=D_\theta(e_z)}_{\text{Decoder 还原图像}}
      $$

* Pipeline

  <!-- 形式 A：若论文包含 Algorithm 流程图或伪代码框，优先截图截取并附带说明 -->
  ![Algorithm Flowchart](assets/<note-file-base>.assets/algorithm.png)

  > [!NOTE]
  > **Algorithm 1. <Algorithm name or caption>.** **Input / State: ...** <说明初始状态与参数输入>；**Core Loop: ...** <说明核心循环迭代与更新逻辑>；**Output: ...** <说明返回结果与收敛边界>。

  <!-- 形式 B：若论文无现成 Algorithm 截图，使用结构化、高对比度样式的 Mermaid 流程图（所有节点文本必须用双引号包裹，严禁使用未转义的特殊字符） -->
  ```mermaid
  flowchart LR
      Input["Observe Request x0"] --> Model["Core Predictor p_theta"]
      Model --> Gate{"Confidence Threshold Met?"}
      Gate -->|Accepted| Result["Return Prediction"]
      Gate -->|Fallback| Review["Route to Refinement"]

      classDef process fill:#EAF2F8,stroke:#1F618D,stroke-width:2px,color:#102A43
      classDef decision fill:#FFF2CC,stroke:#A16207,stroke-width:2px,color:#3F2A00
      classDef future fill:#FCE8E6,stroke:#C5221F,stroke-width:2px,color:#5F1A17
      class Input,Model process
      class Gate decision
      class Result,Review future
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

  * **<Experiment or Benchmark Name>**: <以精炼单句总结实验设置与核心定量结论（约 30–60 字），随后放置主要结果表截图；严禁在下方复读纯文本表格。>

    ![Principal result table](assets/<note-file-base>.assets/main-results.png)

    > [!NOTE]
    > **Table 1. <Original caption or concise overview>.** <说明对比基线、关键提升幅度及解释边界。>

* Critical Thinking

  * **Pros**:
    * <纯架构与原理优势（严格单句，不复述实验结果）。>
    * **Paradigm Demonstration**: <（仅限里程碑论文）说明示范的范式及后续采纳的具体代表工作。>
  * **Cons**:
    * **Failure Mode: <Name>**: <说明理论假设破裂、病态场景或极端环境下的退化机制。>
  * **Trade-offs**:
    * <指出为了获得性能优势所牺牲的成本（如算力、通信、灵活性），评估该置换在实际中是否合理有益。>
  * **Empirical Support**:
    * <评估评测基线是否公正充足、是否存在消融盲区或评测环境合成化偏差（不复述数值结果）。>
  * **Future Directions**:
    * <指出该方向下一个亟待解决的瓶颈或关键突破口。>
```

## Section specifications

### Takeaway
- **Chinese-dominant mixed-language single-sentence punchline**: Exactly 1 high-density sentence in concise Chinese prose with technical proper nouns preserved in English, articulating the core insight.
- **Causal insight structure**: Follow `[Core Mechanism/Action] + [Technical Innovation] -> [Solved Pain Point / Target Capability]`.
- **Strict prohibition on noun-stacking formulas**: Do NOT write `Method = A + B + C` or chain proper nouns with `+` signs. The takeaway must explain *how* the innovation works and *what fundamental pain point* it resolves.
- Never wrap in backticks, quotes, or code fences. Do NOT write an English-only sentence in this section.

### Contribution
- **Strictly 1 concise high-stature sentence in Chinese**: Placed directly after `Takeaway` for immediate executive-level orientation.
- **Macro-level positioning (宏观定调，确立范式)**: Define the paper's primary value on the global academic tree. For milestone papers, boldly and directly declare the foundational research paradigm it pioneered or established (e.g., 开辟了……新范式 / 打破了……技术垄断 / 确立了……基础理论), establishing its macro stature upfront rather than reducing it to a narrow local implementation; for regular papers, classify its core value (New Challenge, New Solution, or Domain Benchmark) within verified evidence bounds.

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
  - **Core vs. routine `Component` explanation rule**: Keep every `Component` headline to 1 concise sentence, then branch by novelty:
    - *Core / paper-proposed `Component`s* (e.g., a newly designed Graph Convolution, routing operator, attention variant, or decoder module): **must** provide concrete mechanism unpacking directly underneath—either via indented operator sub-bullets (`Forward Operation` / `Backward Trick` when non-differentiable or multi-step gradient tricks exist) or a source-grounded equation + `>` explanation block detailing input → transformation → output (tensor/graph shapes) and why the operator resolves the bottleneck.
    - *Standard / off-the-shelf `Component`s* (e.g., vanilla `ResNet`, standard `MLP`, baseline `Tokenizer`): keep strictly to 1 concise sentence describing its interface role without bloated `>` blocks.
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
- **Algorithm Flowchart Priority & Safe Mermaid Fallback (算法框图优先，安全 Mermaid 兜底)**:
  1. *Priority 1 (Paper Algorithm Capture)*: When the paper contains an explicit Algorithm pseudocode box or flowchart (e.g. `Algorithm 1`), capture that diagram directly as an image asset under `Pipeline` accompanied by its paired `> [!NOTE]` detailing `Input / State`, `Core Loop`, and `Output`.
  2. *Priority 2 (Action-Specific Mermaid Flowchart)*: When the paper lacks a ready-made image asset, draw an action-specific Mermaid flowchart (`flowchart LR` for readable horizontal layout in Typora; `flowchart TD` only if strictly hierarchical).
     - **Strict Mermaid Syntax Safety (严格语法安全律)**: All node label text MUST be explicitly enclosed in double quotes (e.g., `NodeID["Clean Node Text"]`) to prevent parse errors from colons, slashes, or commas; strictly avoid unescaped pipes (`|`) or standalone ampersands (`&`) inside node labels; use `classDef` styles (`process`, `decision`, `future`) with high-contrast palettes. Do NOT write numbered text lists.

### Experiment
- Placed immediately after `Pipeline` to evaluate the mechanism established above.
- Open with a compact Mermaid research-logic overview diagram showing the study evidence chain (`Problem -> Learnability -> Predictability -> Analysis/Boundaries`).
- Merge all discussion of the same experiment/benchmark into one child bullet (strictly 1 single sentence combining setup and quantitative conclusion).
- Follow each experiment bullet with the principal cropped result table screenshot and its single `> [!NOTE]` callout. Never duplicate the same experiment across benchmarks.
- **No text table duplication**: Quantitative conclusions belong strictly in the single experiment bullet. Never dump an unformatted or redundant markdown/ASCII text table below that merely repeats the numbers already stated in the sentence.

### Critical Thinking
- Pure reflection and critical analysis across 5 dimensions (each bullet strictly 1 concise sentence):
  1. `**Pros**`: Architectural/methodological strengths. Include `**Paradigm Demonstration**` only for verified milestone papers as a concrete evidence inventory: cite the specific downstream successor papers, foundation models, or open-source projects that explicitly adopted its core framework, formulation, or training paradigm (serving as post-hoc literature evidence for the macro claim in `Contribution`). Omit this bullet for ordinary papers.
  2. `**Cons**`: Concrete failure modes under `**Failure Mode: <Name>**:` (breakdown conditions, pathological cases, bandwidth/compute-ratio violations, synchronization/sample divergence, or load imbalance such as `Causal Mask` skew).
  3. `**Trade-offs**`: What was sacrificed (latency, compute, communication complexity, batch-size / sequence-length lower bounds, or autonomy) and whether the exchange is practically justified.
  4. `**Empirical Support**`: Fairness of baselines, numerical precision settings (`Full Precision` vs `Mixed Precision`), compute-budget caps, synthetic vs realistic benchmarks, ablation rigor, and separation of main vs appendix/`\ifanonymous` results.
  5. `**Future Directions**`: The logical next bottleneck actually exposed by this work (not generic boilerplate).
- Do NOT recap quantitative experiment results already covered in `Experiment`.

## Formatting and asset rules

### Citation metadata, authors, and research team
- Title line format:
  ```markdown
  **<Full Paper Title>**. <Authors> (<Affiliation / Research Team>). **<Venue>**, **<Year>**. [(Paper)](URL) [(Project)](URL) (Citations __N__)
```
- **Author list constraint**:
  - 1 to 3 authors: list all names (`Author 1, Author 2, Author 3`).
  - More than 3 authors: strictly truncate to first author plus et al.: `First Author et al.`.
- **Mandatory Affiliation / Research Team**: Append the primary research institution, key university/lab, or enterprise research team in parentheses immediately after the author string, e.g., `Shen Nie et al. (RUC & Ant Group)` or `Jacob Austin et al. (Google Research)`. This establishes immediate research lineage, compute tier, and institutional credibility upfront.
- **Mandatory citation count**: Include `(Citations __N__)` verified from Semantic Scholar (`[(S2)](URL)`), OpenAlex, Google Scholar, or Crossref. If truly unresolvable, write `(Citations __unknown__)`. Never omit this field.

### Formulas and callouts
- **Math delimiters & blank lines**: Strictly `$...$` for inline math; standalone `$$` blocks for display equations. Standalone `$$...$$` blocks must have a blank line before and after. Never place a display formula on the same line as a markdown bullet (`*`) or text. Never use LaTeX `\( ... \)` or `\[ ... \]`.
- **Figure & Table NOTE**: Every embedded image must be immediately followed by exactly one `> [!NOTE]` at the same indentation level. First line must be a concise overview reusing original caption; followed by explanation using English visual anchors (`**Top: ...**`, `**Left: ...**`, `**(b) ...**`, `**Row: ...**`) that accurately match each panel's actual visual role.
- **Asset capture & Visual QA**: After cropping/saving any figure, table, or algorithm image, **inspect the saved image directly** before referencing it. Every table screenshot must capture the **caption/header plus all principal data rows** (never leave a header-only or truncated crop); multi-panel figures must keep all cited subfigures intact; algorithm blocks must capture the full algorithm boundary including input, loop body, and output. Every number, hardware spec, and anchor in `> [!NOTE]` and the surrounding prose must be verified against both the visible image pixels and the paper source—never extrapolate or fill numbers from memory.
- **Asset extraction toolchain**: Use the bundled script `scripts/extract_assets.py` for all figure, table, and algorithm extraction:
  1. *Locate targets in PDF*: `python3 scripts/extract_assets.py find --pdf <paper.pdf> --query "Algorithm 1"` (or `"Figure 1"`).
  2. *Render PDF page*: `python3 scripts/extract_assets.py render --pdf <paper.pdf> --page <N> --output /tmp/page_<N>.png`.
  3. *Visual coordinate calibration*: Call `view_image /tmp/page_<N>.png` to visually locate bounding box percentages (`--pct top,left,bottom,right`).
  4. *Crop with auto-trim*: `python3 scripts/extract_assets.py crop --image /tmp/page_<N>.png --pct <top,left,bottom,right> --trim --output assets/<note-file-base>.assets/<filename>.png` (supports direct PDF cropping via `--pdf <paper.pdf> --page <N>`).
  5. *arXiv direct extraction*: For arXiv papers, run `python3 scripts/extract_assets.py arxiv --id <arxiv_id_or_url> --output-dir assets/<note-file-base>.assets/` to unpack original vector/raster assets directly.
  6. *Visual QA*: Execute `view_image` on the cropped image to verify full visual integrity prior to embedding in the note.
- **Asset paths**: Save images locally to `assets/<note-file-base>.assets/<filename>` and reference with relative paths (`assets/<note-file-base>.assets/<filename>` or `./assets/<note-file-base>.assets/<filename>`).

## Source priority and PDF fallback

- **Priority**: Paper official publication (proceedings, DOI, OpenReview, arXiv) is sole ground truth > official project/code repo/appendix > Semantic Scholar / technical blogs as secondary aids for context, intuition, and citation counts.
- **PDF-first fallback**: When HTML/source is poor or unavailable:
  1. Read Title, Abstract, Intro, and Conclusion to establish missing capability, framework, and main claims.
  2. Scan all figures and tables before detailed reading; extract only claim-bearing visuals and their governing equations.
  3. Paraphrase core claims; never copy raw text walls, long derivations, or full abstracts into the note.

## Hard invariants (Completion checklist)

Before completing the summary, verify every invariant:
1. **Metadata line**: Begins with full paper title in bold; author list truncated to `First Author et al.` when > 3 authors; includes mandatory research team / institution in parentheses `(<Affiliation / Team>)`; contains mandatory `(Citations __N__)` or `(Citations __unknown__)`.
2. **Strict single-sentence brevity & zero meta-prefixes**: Every bullet point across `Contribution`, `Motivation`, `Core Mechanism`, `Experiment`, and `Critical Thinking` is strictly **1 single sentence** (target ~30–60 Chinese characters, no semicolon chaining, no run-on clauses, high insight density), without stripping required operators, tensor shapes, or quantitative bounds, and contains zero meta-instruction prefixes (`单句说明……：`, `一句话概括……：`).
3. **Top-level orientation**: `Takeaway` is immediately followed by `Contribution` (single high-stature sentence establishing macro-level academic positioning and paradigm value).
4. **Pure motivation**: `Motivation` contains exactly 2 bullets (`Core Problem` and `Why Existing Routes Fail`) without leaking solution/method names.
5. **Paper-faithful Core Mechanism & Pipeline flow**: Route `Core Mechanism` to the paper's actual type. Only use `\underbrace` multi-term objectives, `Learnable State`, forward/backward `STE` sub-bullets, and chained inference arrows when the paper itself defines those constructs; for systems/parallelism/algorithmic papers, present the paper's real governing thresholds, resource/complexity bounds, and core operators without forcing artificial component splits or fabricating equations. Followed immediately by `Pipeline` before `Experiment`.
6. **Source-grounded micro-mechanism transparency**: Ban abstract hand-waving (e.g., "提取特征", "压缩瓶颈") and formula fabrication. Every equation, operator, tensor shape/memory bound ($H \times W \times D$, $6bch$), and threshold ($c \ge F/B$) must come verbatim or faithfully from the paper source.
7. **Direct autonomous execution**: Immediately execute without scope/depth confirmation prompts.
8. **Language policy**: Every section (including `Takeaway`) uses concise Chinese-dominant prose with English technical proper nouns preserved; only section headings and bold captions/labels are in English Title Case (never write English-only paragraphs or English-only `Takeaway`).
9. **Proper nouns in English**: All technical terms, module names, parallelism strategies, architecture concepts, and benchmark names strictly preserve their standard English terminology; never translate them into localized Chinese (e.g., strictly use "Vector Quantizer", "Encoder / Decoder", "Blockwise FeedForward", "Online Softmax", "Tensor Parallelism").
10. **Takeaway**: Exactly 1 Chinese-dominant mixed-language causal insight punchline (Mechanism + Innovation -> Solved Bottleneck), preserving English technical proper nouns without noun-stacking formulas (`Method = A + B + C`), quotes, code fences, or backticks.
11. **Pipeline & diagrams**: `Pipeline` presents the runtime execution view. When the paper contains an Algorithm flowchart or pseudocode diagram, capture it directly as an image asset with a paired `> [!NOTE]`; otherwise, draw a syntax-safe Mermaid flowchart (`flowchart LR`) with double-quoted labels and styled node classes. `Experiment` begins with the research-logic overview diagram. Never generate redundant text tables duplicating bullet sentences.
12. **Figures, tables, Visual QA & NOTEs**: Every image is saved under `assets/<note-file-base>.assets/`, visually inspected after cropping (table screenshots must include header + full data rows; multi-panel figures must be unclipped), and immediately followed by a `> [!NOTE]` whose English visual anchors and numbers match both the image and the paper source.
13. **Delimiters & foldability**: Math uses only `$...$` and standalone `$$...$$` with blank lines before/after (never glued to bullet lines); all child content is indented with 2 spaces under its owning list item.
14. **Selective `>` & core-Component explanation layer**: Every core/novel `Component` in `Core Mechanism` must carry an indented operator/equation breakdown or `>` explanation block (input → transformation → output and design rationale), while routine/off-the-shelf components stay 1 sentence; for `Motivation` and `Critical Thinking`, add `>` blocks on demand when conceptual leaps or hidden derivations exist (using toy-dimension examples, `**Step N**` `←` step-by-step recurrences, and buffer lifecycles where helpful). Omit `>` on `Takeaway`, `Contribution`, and `Experiment` (use `> [!NOTE]` there), and keep plain `>` separated from `> [!NOTE]`.
15. **Mathematical transparency & derivation invariant**: Every primary equation, matrix, or symbol must have explicit dimensions and element-wise physical definitions (Zero Undefined Symbols Rule); non-trivial posterior/update formulas must provide the complete 4-step derivation chain inside `>` (Bayes start -> Markov independence -> vectorized Hadamard product -> normalization denominator); loss coefficients (like $1/t$ or $\frac{1}{4}$) must explain their mathematical origin and boundary behavior.
16. **Deterministic figure selection invariant**: `Core Framework` figure must be derived from method-section `\ref` citation priority or verified via Caption whitelist (`Overview`, `Architecture`, `Framework`); figures with experiment keywords (`Benchmark`, `Comparison`, `Accuracy`, `vs.`, `Results`, `Ablation`, `Scatter`) are strictly banned from `Core Mechanism`; `> [!NOTE]` first line must directly reuse the exact raw caption text.
