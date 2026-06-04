# Software Development Prompt Standards

Use for coding, backend, API, full-stack, debugging, QA, code review, deployment, and implementation prompts.

## General Coding

Require:

- feature/fix outcome
- current behavior and desired behavior
- relevant files, modules, API routes, or components
- constraints: language, framework, dependency, compatibility, style, ownership
- edit permissions: implement, explain only, review only, or plan first
- verification: tests, lint, typecheck, build, manual checks

Rewrite shape:

```text
请在当前项目中实现/修复 [task]。先阅读相关代码，沿用现有模式，避免无关重构。
上下文：[current behavior/project area]
目标：[desired behavior]
范围：[files/modules/features]
约束：[framework/style/dependencies/backward compatibility]
验证：[tests/lint/typecheck/manual check]
输出：[changed files summary + verification result]
```

## Backend and API

Add:

- endpoint/service/job name
- request/response schema
- auth and permission rules
- validation and error behavior
- database/model changes
- backward compatibility and migration needs
- integration tests or API checks

## Full-Stack

Add:

- frontend flow and UI states
- API behavior and data contract
- database/schema/persistence rules
- auth, validation, rate limits, or security constraints
- error and loading states
- end-to-end verification

## Debugging

Require:

- exact error, stack trace, log, screenshot, or symptom
- reproduction steps
- expected vs actual behavior
- recent changes or suspected area
- environment: OS, browser, runtime, dependency versions, branch
- instruction to find root cause before fixing
- regression check

Rewrite shape:

```text
请调查并修复 [bug]。先复现/定位根因，不要直接猜修。
现象：[actual behavior/error]
期望：[expected behavior]
复现步骤：[steps]
上下文：[recent changes/environment]
范围：[likely files/modules]
验证：[regression test/manual repro/check command]
```

## QA

Require:

- target URL/page/feature/flow
- QA depth: quick, standard, exhaustive
- devices/viewports/browsers
- priorities: functional, visual, accessibility, performance
- report-only or fix-and-verify
- evidence: severity, repro steps, screenshots, health score, readiness

## Code Review

Require:

- diff, branch, PR, or file scope
- base branch or comparison target
- focus: correctness, security, tests, contracts, performance, maintainability
- output format: findings first, file/line refs, severity
- whether to fix findings or report only

## Deployment and PR

Require:

- current branch, base branch, destination
- permissions for commit, push, PR, deploy
- pre-ship checks
- version/changelog/docs requirements
- rollback or production-risk constraints
- final evidence: command results, PR/deploy link
