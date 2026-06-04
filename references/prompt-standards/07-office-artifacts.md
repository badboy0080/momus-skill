# Office Artifact Prompt Standards

Use for spreadsheets, workbooks, Google Sheets, presentations, decks, PPTX, executive artifacts, financial models, trackers, and dashboards in office formats.

## Spreadsheets

Require:

- workbook purpose: tracker, model, dashboard, analysis, template, budget, forecast.
- data source and assumptions.
- sheet structure: summary/dashboard, inputs, calculations, detail, checks.
- formula expectations and whether values should be editable.
- charts/tables/conditional formatting/validation needs.
- domain: finance, marketing, healthcare, research, operations.
- verification: formulas compute, key ranges inspected, layout rendered/readable.

Rewrite shape:

```text
请创建/修改一个 [spreadsheet/workbook]，用于 [purpose]。
数据/假设：[source/inputs]
工作表结构：[dashboard/inputs/calculations/detail/checks]
计算要求：[formulas/model logic]
视觉和可用性：[formatting/charts/tables/validation]
验证：[formula checks/rendered layout/key ranges]
输出：[final xlsx or Sheets deliverable]
```

## Presentations

Require:

- deck mode: create, template-following, targeted edit.
- audience and story purpose.
- source material and reference deck roles.
- claim spine: main argument and slide-level claims.
- design system or template fidelity.
- expected slide count or sections.
- verification: render previews, contact-sheet quality, no filler.

Rewrite shape:

```text
请制作/修改一个 [PPTX/deck]。
模式：[create/template-following/targeted-edit]
受众：[audience]
故事目标：[decision/story]
素材：[source docs/data/reference deck]
结构：[sections/slide count/claim spine]
设计要求：[template fidelity or visual direction]
验证：[rendered previews/contact sheet/readability]
输出：[final PPTX]
```

## Weak Prompt Smells

- "做个表格" without purpose, columns, formulas, or data.
- "做个 PPT" without audience, story, source material, or slide count.
- "高级一点" without reference, audience, or quality bar.
