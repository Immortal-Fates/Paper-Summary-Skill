# paper-summary

`paper-summary` 是一个 Codex Skill，用于把论文整理成极简、高信息密度、面向深度复盘的 Typora 友好 Markdown 笔记。它先确立论文的核心问题与顶层框架机制，再系统组织图表、公式、实验逻辑与批判性思考；论文本身始终为唯一事实依据。

## 安装与识别

将本目录放置于 Codex 的用户技能目录下：

```text
${CODEX_HOME:-~/.codex}/skills/paper-summary/
```

目录中包含 `SKILL.md`。Codex 会自动识别本技能；若未立即出现，重启 Codex 会话即可。

## 使用方法

在包含论文链接的 Markdown 笔记中直接调用：

```text
使用 $paper-summary 总结当前笔记中的论文。
```

或显式指定论文链接与输出路径：

```text
使用 $paper-summary 总结 https://arxiv.org/abs/... 并写入 papers/example.md。
```

## 输入要求

- 可访问的论文链接（出版社、DOI、OpenReview、arXiv、会议论文集等）。
- 明确的目标笔记路径或输出位置。
- 若在已有笔记中追加，技能会自动保留原笔记的 frontmatter、标题及已有内容，不随意覆盖。

## 输出结构与规范

默认生成中文为主、小标题标签严格使用标准英文 Title Case（如 `Core Problem`、`Core Framework`、`Key Component` 等）、技术名词保留英文的 Markdown 笔记。每个 bullet point 均受**严格单句（25～45字）**的硬性长度约束，直奔核心因果，拒绝冗长堆叠。

### 1. 论文元数据
置于笔记顶部，标题加粗，作者多于 3 人时自动截断：
```markdown
**<Full Paper Title>**. <Author 1, Author 2, Author 3 | First Author et al.>. **<Venue>**, **<Year>**. [(Paper)](URL) [(Project)](URL) (Citations __N__)
```

### 2. 标准 7 大板块
1. **Takeaway**：严格 1 句纯英文因果洞察句（Insight Punchline），按 `[核心机制] + [技术巧思] → [解决的核心痛点/目标能力]` 结构提炼，严禁使用 `Method = A + B + C` 堆砌专有名词。
2. **Contribution**：紧随 Takeaway 之后，以中文严格单句定性论文的核心学术价值归属（新 challenge、新 solution 或新 research paradigm），且与论文实际证据范围一致。
3. **Motivation**：以中文阐述 `**Core Problem**:`（底层能力鸿沟与痛点）与 `**Why Existing Routes Fail**:`（现有替代方案缺陷），仅标签为英文，内容必须保持中文，不提前剧透具体方案。
4. **Core Mechanism**：
   - **系统/架构类论文**：首句给出 `**Core Framework: <Framework Name>**`（概述闭环并明确点明系统由哪几部分组成），下属按系统模块以 List 形式展开 `**Component: <Component Name>**`；每个模块必须交代表征数据形态（如空间网格、Token 序列）并讲透算子级实现机理（如前向输出与反向梯度复制），严禁“提取高层表征”等空泛套话；复合目标函数必须单句拆解各项分别更新哪些参数模块；
   - **非系统/理论类论文**：弹性平铺 `**Core Formulation: <Name>**` 与 `**Theoretical Property: <Name>**`；
   - 公式紧随对应要点，独立块公式前后必须留空行（严禁与列表行粘连），图表均附带英文方位视觉锚点（如 `**Top: ...**`、`**Left: ...**`）的 `> [!NOTE]` 说明。
5. **Pipeline**：紧跟 Core Mechanism 作为动态运行时流程图，纯 Mermaid 机制与决策流程图（默认 `flowchart LR`），使用统一的高对比度色彩类区分普通处理、判定节点与未来扩展。
6. **Experiment**：以 Mermaid 研究逻辑图开篇（串联“问题发现 → 可学习性 → 模型预测 → 边界分析”），随后单条目提炼各关键实验（严格单句，25～45字），并截取主结果表图片（严禁在单句下方重复堆砌内容一致的纯文本表格）。
7. **Critical Thinking**：纯粹的深度批判与反思，每个子要点严格单句，涵盖 `Pros`（含里程碑论文可选的 `Paradigm Demonstration`）、`Cons`（具象的 `Failure Mode: <Name>`）、`Trade-offs`（性能与代价置换评估）、`Empirical Support`（实验公正性与消融盲区）及 `Future Directions`（下一步瓶颈）。

## 核心设计原则

- **严格自包含**：所有结构与提取规则均内建于 `SKILL.md`，无需任何外部参考仓库。
- **专业术语严格保留英文**：所有模块名、算法名、架构组件与学术专有名词（如 `Encoder`, `Decoder`, `Vector Quantizer`, `Codebook`, `Straight-Through Estimator`, `Posterior Collapse` 等）必须直接使用标准英文，严禁机械翻译为生硬中文（如严禁将 `Vector Quantizer` 译为“离散码本量化器”）。
- **微观机理穿透（Micro-Mechanism Transparency）**：严禁“提取高层表征”、“压缩信息流”等抽象套话；必须写透具体算子技巧（如 STE 梯度直通具体公式）、张量数据形态（如 $H \times W \times D$ 空间网格）与损失项的反事实物理目的（如防止何种具体退化）。
- **直接自主执行（Direct Autonomous Execution）**：收到总结指令后默认仅针对目标论文本身直接执行，严禁停下来主动向用户询问总结范围、衍生工作或内容深度。
- **认知流顺畅（Cognitive Flow）**：顶层方案与定位先行（Takeaway + Contribution） → 问题与机制（Motivation + Core Mechanism + Pipeline） → 验证与批判（Experiment + Critical Thinking）。
- **高信息密度与严格单句**：严禁废话与长篇大论，每个要点强制限制在严格单句（25～45字）内，禁止分号断句拼凑或从句堆叠。
- **本地相对资产**：图表截图统一下载到相对路径 `assets/<note-file-base>.assets/`，确保跨平台与 Typora 本地离线正常渲染。
- **严谨排版**：行内公式严格使用 `$...$`，独立块公式使用 `$$`；层级统一缩进 2 格以适配 Typora 大纲折叠。

更多详细规则以 [SKILL.md](SKILL.md) 为准。
