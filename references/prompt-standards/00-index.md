# Prompt Standards Index

Use this index to choose the smallest relevant prompt-standard file. Do not load every file by default.

## Source Influence

These standards are distilled from local skill patterns and the installed Superpowers plugin:

- Installed Superpowers plugin at `C:\Users\huyoc\.codex\plugins\cache\openai-curated\superpowers\fef63ecf`: brainstorming, writing-plans, TDD, systematic-debugging, subagent-driven-development, requesting-code-review, verification-before-completion, finishing-a-development-branch, writing-skills.
- Local gstack skills: investigate, QA, review, ship, office-hours, plan CEO/engineering/design review.
- Frontend/design skills: design-taste-frontend, redesign-existing-projects, image-to-code, high-end visual design.
- Data Analytics skills: product/business analysis, build-report, KPI/reporting/dashboard/report patterns.
- Office artifact skills: documents, spreadsheets, presentations.
- Agent and skill-building skills: agentscope-agent-builder, skill-creator, colleague-skill.

## Domain Files

- `01-engineering-workflow.md`: planning, architecture review, TDD, worktrees, subagents, verification discipline, finishing branches.
- `02-software-development.md`: general coding, backend, API, full-stack, debugging, QA, code review, deployment.
- `03-frontend-design.md`: frontend UI, visual design, landing pages, redesigns, responsive QA, image-to-code.
- `04-product-business.md`: product ideas, strategy, scope, startup thinking, decision framing, market/business analysis.
- `05-data-analytics.md`: metrics, dashboards, reports, KPI readouts, source-backed analysis.
- `06-content-documents.md`: writing, documentation, Word/Docs artifacts, redlines, release docs.
- `07-office-artifacts.md`: spreadsheets, presentations, workbooks, decks, executive artifacts.
- `08-knowledge-base-expansion.md`: how to add new domain prompt standards later.
- `09-superpowers-engineering.md`: prompt standards mined directly from the installed Superpowers plugin's engineering workflow skills.

## Selection Rules

- For vague coding requests, load `02-software-development.md`.
- For "build a site/page/component/UI" requests, load `03-frontend-design.md`.
- For "is this worth building", product strategy, or scope questions, load `04-product-business.md`.
- For metrics, analysis, reports, dashboards, or KPI questions, load `05-data-analytics.md`.
- For docs, docx, README, release notes, or policy-style writing, load `06-content-documents.md`.
- For Excel, Sheets, PPT, decks, or executive workbooks, load `07-office-artifacts.md`.
- For requests about development process, planning, TDD, review gates, subagents, or branch completion, load `09-superpowers-engineering.md` first, then `01-engineering-workflow.md` only if a shorter generic version is needed.

When multiple domains apply, load at most two files: the primary task domain and the delivery-artifact domain.

## Universal Prompt Fields

Every strong prompt should clarify:

- objective
- context
- scope and non-scope
- constraints
- required evidence or source of truth
- execution mode: plan, implement, review, report-only, fix-and-verify
- verification or acceptance criteria
- expected output format

Use domain files to add specialized fields, not to replace these basics.
