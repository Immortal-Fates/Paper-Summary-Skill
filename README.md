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

默认生成中文为主、小标题标签严格使用标准英文 Title Case（如 `Core Problem`、`Core Framework`、`Key Component` 等）、技术名词保留英文的 Markdown 笔记。每个 bullet point 均受**最多 1～2 句话**的硬性长度约束。

### 1. 论文元数据
置于笔记顶部，标题加粗，作者多于 3 人时自动截断：
```markdown
**<Full Paper Title>**. <Author 1, Author 2, Author 3 | First Author et al.>. **<Venue>**, **<Year>**. [(Paper)](URL) [(Project)](URL) (Citations __N__)
```

### 2. 标准 6 大板块
1. **Takeaway**：纯英文概括，优先采用纯文本组合公式（如 `Method = Framework + Component A + Component B`）或 1–2 句总结，不加引号或代码块包装。
2. **Motivation**：严格包含 `**Core Problem**:`（未解决的能力鸿沟）与 `**Why Existing Routes Fail**:`（现有方案缺陷），不在此处提前剧透或泄露具体方法名称。
3. **Core Mechanism**：
   - **系统/架构类论文**：先给 `**Core Framework: <Framework Name>**`（闭环解释、全局架构图、核心目标函数），下钻嵌套 `**Key Component: <Component Name>**`；
   - **非系统/理论类论文**：弹性平铺 `**Core Formulation: <Name>**` 与 `**Theoretical Property: <Name>**`；
   - 公式紧随对应要点，图表均附带英文方位视觉锚点（如 `**Top: ...**`、`**Left: ...**`）的 `> [!NOTE]` 说明。
4. **Experiment**：以 Mermaid 研究逻辑图开篇（串联“问题发现 → 可学习性 → 模型预测 → 边界分析”），随后单条目提炼各关键实验（1–2 句话），并截取主结果表图片。
5. **Pipeline**：纯 Mermaid 机制与决策流程图（默认 `flowchart LR`），使用统一的高对比度色彩类区分普通处理、判定节点与未来扩展。
6. **Critical Thinking**：系统化深度批判，涵盖 `Contribution`（一句话定性）、`Pros`（含里程碑论文可选的 `Paradigm Demonstration`）、`Cons`（具象的 `Failure Mode: <Name>`）、`Trade-offs`（性能与代价置换评估）、`Empirical Support`（实验公正性与消融盲区）及 `Future Directions`（下一步瓶颈）。

## 核心设计原则

- **严格自包含**：所有结构与提取规则均内建于 `SKILL.md`，无需任何外部参考仓库。
- **高信息密度**：严禁废话与长篇大论，每个要点强制限制在 1–2 句话内。
- **本地相对资产**：图表截图统一下载到相对路径 `assets/<note-file-base>.assets/`，确保跨平台与 Typora 本地离线正常渲染。
- **严谨排版**：行内公式严格使用 `$...$`，独立块公式使用 `$$`；层级统一缩进 2 格以适配 Typora 大纲折叠。

更多详细规则以 [SKILL.md](SKILL.md) 为准。
