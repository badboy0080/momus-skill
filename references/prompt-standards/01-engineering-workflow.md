# Engineering Workflow Prompt Standards

Use for generic requests about planning, architecture, TDD, implementation workflow, review gates, branch finishing, or disciplined development. For Superpowers-specific workflows, prefer `09-superpowers-engineering.md`.

## Required Prompt Inputs

- Problem statement and desired outcome.
- Current project state: repo, branch, existing plan, relevant docs, or starting point.
- Workflow mode: brainstorm, plan, implement, TDD, debug, review, ship, or finish branch.
- Scope boundary: files/modules/features in scope and what must not change.
- Verification gate: tests, lint, typecheck, build, manual repro, review checklist.
- Completion contract: what evidence proves the work is done.
- Whether the user wants a lightweight plan or a Superpowers-style gated workflow.

## Superpowers-Style Rewrite Pattern

```text
请按系统化工程流程处理这个任务。

目标：[outcome]
当前上下文：[repo/branch/plan/current state]
执行模式：[brainstorm / plan / TDD / implement / debug / review / finish branch]
范围：[in scope]
不做：[out of scope]
验证门槛：[tests/lint/typecheck/build/manual checks]
完成标准：[evidence required before final answer]
输出：[plan, code changes summary, review findings, or ship report]
```

## Planning Requests

Add:

- architecture and data flow questions
- edge cases and failure modes
- dependency and migration risks
- task breakdown into verifiable chunks
- explicit "do not code yet" when the user only wants a plan

## TDD Requests

Add:

- failing test target
- expected behavior
- red-green-refactor loop
- command to run tests
- instruction not to weaken tests to pass

## Review-Gated Work

Add:

- spec compliance review before code quality review
- evidence for each completed claim
- blockers for critical issues
- follow-up list for non-blocking issues

## Weak Prompt Smells

- "按最佳实践来" without naming the desired outcome.
- "写个计划" without scope, constraints, or verification.
- "做完并上线" without branch, checks, deploy target, or permissions.
- "用 TDD" without saying what behavior should fail first.
