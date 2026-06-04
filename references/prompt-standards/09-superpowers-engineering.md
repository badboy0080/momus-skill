# Superpowers Engineering Prompt Standards

Use for prompts that should follow the installed Superpowers plugin's engineering workflow. Source plugin:

`C:\Users\huyoc\.codex\plugins\cache\openai-curated\superpowers\fef63ecf`

This file is a prompt-quality reference, not a replacement for the Superpowers skills themselves. It tells Momus what information a good user prompt should include before those workflows can run well.

## Workflow Categories

Superpowers decomposes software work into strict stages:

- brainstorming: turn idea into approved design/spec before implementation
- writing-plans: convert approved spec into bite-sized implementation plan
- test-driven-development: write failing test before production code
- systematic-debugging: root cause before fixes
- subagent-driven-development: fresh subagent per task with spec and quality review
- requesting-code-review: review early and before merge
- verification-before-completion: fresh evidence before success claims
- finishing-a-development-branch: tests, environment detection, merge/PR/keep/discard options
- writing-skills: TDD applied to process documentation and skills

## Brainstorming and Design

Required prompt inputs:

- idea or feature outcome
- current project context or repo location
- purpose, constraints, and success criteria
- whether the scope includes multiple independent subsystems
- whether visual companion/mockups/diagrams would help
- expected design artifact location if not default

Rewrite shape:

```text
请使用 Superpowers 风格先做设计，不要直接实现。
目标：[feature/idea]
项目上下文：[repo/current files/docs/recent state]
约束：[technical/product/time/scope constraints]
成功标准：[what makes this work]
范围判断：[single subsystem or needs decomposition]
输出：[2-3 approaches with tradeoffs, recommended design, then approved spec]
硬门槛：设计/规格未确认前不要写代码。
```

Weak prompt smells:

- "直接做" for a new feature with no design.
- multi-subsystem product idea with no decomposition.
- "很简单不用设计" when behavior or architecture changes.

## Writing Plans

Required prompt inputs:

- approved spec or requirements source
- goal and architecture summary
- tech stack
- exact files/modules likely involved
- desired test strategy
- plan location if not default
- execution preference: subagent-driven or inline

Rewrite shape:

```text
请基于已确认的规格写 Superpowers 实施计划。
规格来源：[spec path or requirements]
目标：[one sentence]
架构：[2-3 sentence approach]
技术栈：[stack]
文件结构：[files to create/modify/test]
计划要求：任务拆成 2-5 分钟步骤；每步包含具体代码/命令/预期输出；禁止 TBD/TODO/类似 Task N。
验证：[tests/lint/typecheck/build/manual checks]
输出：[plan path + execution options]
```

Weak prompt smells:

- "写个计划" without spec, files, test strategy, or verification.
- plan request that allows placeholders or vague "add error handling".

## TDD

Required prompt inputs:

- behavior to implement or bug to fix
- test framework and target test file when known
- expected failing condition
- minimal implementation boundary
- verification command
- exceptions if TDD should not apply

Rewrite shape:

```text
请按 TDD 实现 [behavior/fix]。
先写一个最小失败测试并运行，确认它因目标行为缺失而失败。
再写最小实现让测试通过，最后只在绿灯后重构。
目标行为：[behavior]
测试位置/框架：[test file/framework]
验证命令：[command]
约束：不要先写生产代码；不要添加测试未要求的功能。
输出：说明 RED/GREEN/REFACTOR 的命令和结果。
```

Weak prompt smells:

- "顺手加测试" after implementation.
- "这个太简单不用 TDD".
- no expected behavior precise enough to test.

## Systematic Debugging

Required prompt inputs:

- exact symptom, error, log, stack trace, or failing test
- reproduction steps and reliability
- expected vs actual behavior
- recent changes
- environment and component boundaries
- evidence-gathering permission
- regression test or verification command

Rewrite shape:

```text
请按系统化调试处理 [issue]，先找根因，不要猜修。
现象：[error/log/symptom]
复现：[steps/reliability]
期望：[expected]
最近变化：[diff/commits/config/deps]
边界：[components/data flow]
调查要求：读完整错误、稳定复现、检查最近变化、必要时加诊断日志、形成单一假设再最小验证。
修复要求：根因明确后写失败测试/复现，再做单一修复。
验证：[regression test/manual repro/full command]
```

Weak prompt smells:

- "修一下 bug" with no repro or error.
- proposed fix before root cause evidence.
- multiple changes at once "看看能不能好".

## Subagent-Driven Development

Required prompt inputs:

- implementation plan path or full task list
- task independence and boundaries
- context each subagent needs
- work directory
- review requirements: spec compliance first, code quality second
- status handling expectations: DONE, DONE_WITH_CONCERNS, BLOCKED, NEEDS_CONTEXT

Rewrite shape:

```text
请使用 Superpowers 子代理驱动开发执行这个计划。
计划：[plan path or task list]
工作目录：[directory]
上下文：[architecture/dependencies/constraints]
执行规则：每个任务派发新子代理；给子代理完整任务文本和必要上下文；任务后先做规格符合性审查，再做代码质量审查；通过后再进入下一任务。
阻塞处理：遇到 BLOCKED/NEEDS_CONTEXT 不要硬猜，补上下文、换模型或拆任务。
输出：每个任务的状态、测试结果、提交信息、审查结论。
```

Weak prompt smells:

- "让子代理做" without plan text, context, or review gates.
- asking subagent to read broad history instead of giving curated task context.

## Code Review

Required prompt inputs:

- description of work
- plan/spec/requirements
- base SHA and head SHA or diff scope
- severity expectations
- action rules: fix critical/important, note minor

Rewrite shape:

```text
请按 Superpowers 方式请求代码审查。
工作说明：[description]
需求/计划：[plan or requirements]
范围：[base SHA/head SHA or diff]
重点：[correctness/spec compliance/tests/security/performance]
处理规则：Critical 立即修；Important 继续前修；Minor 记录即可；如果审查意见错误，用代码和测试反驳。
输出：findings、严重级别、文件/行号、是否可继续。
```

## Verification Before Completion

Required prompt inputs:

- claim to verify
- command that proves the claim
- expected output or pass criteria
- whether partial verification is acceptable

Rewrite shape:

```text
在声明完成前先验证。
要证明的结论：[claim]
验证命令：[full command]
通过标准：[expected output/exit code/failure count]
规则：运行新鲜完整验证，读取输出和退出码，再基于证据陈述状态。不要用 should/probably/seems。
```

Weak prompt smells:

- "应该好了".
- "不用跑测试，直接告诉我完成".
- success claim without fresh command output.

## Finishing a Development Branch

Required prompt inputs:

- test command
- branch and base branch
- whether normal repo/worktree/detached workspace
- preferred integration path: merge, PR, keep, discard
- permission for destructive cleanup

Rewrite shape:

```text
请完成开发分支收尾。
先运行完整测试：[test command]
分支信息：[current/base/worktree state if known]
如果测试失败，停止并报告失败。
如果测试通过，检测环境并给出结构化选项：本地合并、推送建 PR、保留分支、丢弃工作。
只有用户明确选择后再执行；丢弃必须二次确认。
```

## Writing Skills

Required prompt inputs:

- skill purpose and trigger conditions
- pressure scenarios to test
- expected failure without skill
- desired behavior with skill
- target agent/platform
- validation method

Rewrite shape:

```text
请按 Superpowers 写 skill 的方法创建/修改这个 skill。
目标：[skill purpose]
触发：[specific situations]
压力场景：[test cases]
基线失败：[what agents do wrong without it]
期望行为：[what the skill must enforce]
验证：[subagent forward test or quick validation]
输出：[SKILL.md/resources/update summary]
```

Weak prompt smells:

- skill description summarizes workflow instead of trigger conditions.
- no pressure tests.
- bloated skill text with no discovery strategy.
