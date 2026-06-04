# Content and Document Prompt Standards

Use for writing, editing, documentation, DOCX/Word/Google Docs artifacts, release documentation, redlines, comments, and professional written deliverables.

## Required Prompt Inputs

- Document type: memo, proposal, README, guide, policy, launch note, redline, comment pass, Google Doc, DOCX.
- Audience and purpose.
- Source material or facts that must be included.
- Tone and style.
- Structure requirements.
- Formatting or template constraints.
- Edit mode: create, revise, redline, comment, summarize, preserve formatting.
- Verification: render/inspect for DOCX, link/source check for docs, final artifact path.

## DOCX/Google Docs

Add:

- destination: local DOCX or native Google Docs
- design preset or visual style
- whether to preserve existing formatting
- sections/tables/lists/forms required
- render-and-inspect gate when producing DOCX

## Project Documentation

Add:

- docs to update
- shipped change or diff to reflect
- intended reader: developer, maintainer, user, stakeholder
- compatibility with existing docs
- no unrelated doc churn

Rewrite shape:

```text
请创建/修改 [document type]。
目标：[purpose]
受众：[audience]
素材：[source facts/files]
结构：[sections]
风格：[tone/design/template]
编辑模式：[create/revise/redline/comment/preserve formatting]
验证：[render/link/source consistency/final artifact]
输出：[final doc/path/summary]
```
