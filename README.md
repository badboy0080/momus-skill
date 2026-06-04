<p align="center">
  <img src="assets/momus-skill-hero.png" alt="Momus Skill hero banner" width="100%" />
</p>

# Momus Skill

Momus Skill 是一个面向 IDE coding agent 的提示词输入审查器。它不会替你完成具体编码任务，而是在 agent 开始执行之前，识别那些过于模糊、缺少上下文、容易导致猜测的请求，并把它们重写成更清晰、可验证、可执行的任务提示词。

它的风格不是温吞的表格打分，而是一个带轻微讽刺感的硅基审稿人：指出 prompt 哪里烂，给出可直接采用的改写版本，然后让用户确认是否使用优化后的 prompt。

## 适合什么场景

- 你经常对 Codex、Cursor、Claude Code 等 IDE agent 输入过于笼统的任务。
- 你希望在执行前减少返工、误解和大范围猜测。
- 你想把「帮我修 bug」「优化一下」「做个前端页面」这类请求改写成工程上可落地的任务。
- 你需要一个可复用的 prompt-review skill，而不是每次临时手写审查规则。

## 核心能力

- **选择性触发**：默认只拦截明显低质量、信息不足的 coding-agent 请求，避免每句话都被过度审查。
- **自然讽刺式 critique**：直接指出 prompt 缺少目标、上下文、范围、约束或验证方式。
- **可执行 prompt 重写**：把弱请求改写成包含背景、目标、范围、要求、验证和输出格式的执行提示词。
- **领域标准扩展**：根据任务类型加载对应的 prompt standards，例如软件开发、前端设计、数据分析、文档、演示文稿等。
- **跨 IDE 适配**：提供面向其他 IDE agent 的适配片段，方便迁移到不同工具链。

## 安装

将本目录放入 Codex skills 目录后，Codex 会通过 `SKILL.md` 发现该 skill。

推荐路径：

```text
C:\Users\<you>\.codex\skills\momus-skill\momus-skill
```

目录中必须包含：

```text
SKILL.md
references/
agents/
```

## 使用方式

显式调用 Momus：

```text
使用 $momus-skill 帮我审查这个请求，并改写成更适合 Codex 执行的 prompt：
帮我优化一下这个项目
```

典型输出会包含三部分：

```text
一段带讽刺感但有用的 prompt critique。

一份改写后的可执行 prompt。

一个确认问题，询问是否采用改写版本继续执行。
```

如果用户确认，例如回复「可以」「采用」「yes」「ok」，agent 应使用改写后的 prompt 继续执行任务。

## 触发策略

Momus Skill 不应该默认审查所有输入。它只在以下情况触发：

- 用户显式提到 `Momus Skill`、`$momus-skill` 或要求审查/改写 prompt。
- 用户的 coding、frontend、full-stack、debugging、QA、review、deployment 或 agent-workflow 请求明显过于模糊。
- 任务缺少基本执行信息，继续执行会迫使 agent 猜测目标、范围或验收标准。

它不应该拦截：

- 普通澄清问题。
- 已经足够明确的文件编辑请求。
- 具体的 follow-up 指令。
- 闲聊或非工程任务。

## 示例

弱 prompt：

```text
帮我修复这个 bug
```

Momus 改写后的方向：

```text
请你作为资深软件工程师，先阅读当前仓库并定位 bug 相关代码。

上下文：
- 用户报告项目存在 bug，但尚未提供错误信息。
- 如果仓库中有测试、日志或 issue 线索，请优先使用本地上下文定位问题。

目标：
- 找到 bug 的根因并实现最小修复。

范围：
- 只修改与该 bug 直接相关的文件。
- 不做无关重构或样式整理。

验证：
- 添加或运行能复现该问题的测试。
- 修复后运行相关测试并报告结果。

输出：
- 简要说明根因、修改内容和验证结果。
```

## 项目结构

```text
.
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
└── references/
    ├── ide-adapter-snippets.md
    ├── domain-prompt-standards.md
    └── prompt-standards/
        ├── 00-index.md
        ├── 01-engineering-workflow.md
        ├── 02-software-development.md
        ├── 03-frontend-design.md
        ├── 04-product-business.md
        ├── 05-data-analytics.md
        ├── 06-content-documents.md
        ├── 07-office-artifacts.md
        ├── 08-knowledge-base-expansion.md
        └── 09-superpowers-engineering.md
```

## 设计原则

- **先审查，再执行**：低质量 prompt 会先被重写，而不是直接进入编码。
- **少猜测**：缺失的信息要么从仓库中查找，要么明确标出需要用户补充。
- **最小必要上下文**：根据领域加载最相关的 prompt standards，不一次性吞下整个知识库。
- **有用的锋利感**：讽刺是为了让问题更明显，不是为了攻击用户。
- **执行导向**：最终产物必须能让 coding agent 明确知道要看什么、改什么、如何验证。

## 维护建议

- 新增领域规则时，优先在 `references/prompt-standards/` 下添加独立文件。
- 更新 `references/prompt-standards/00-index.md`，说明新文件的适用场景和选择规则。
- 保持 `SKILL.md` 精简，把可扩展的领域知识放进 `references/`。
- 示例 prompt 要短、准、可执行，避免把 prompt review 写成冗长模板。

## License

未指定。若准备公开发布，建议补充明确的开源许可证。
