# Data Analytics Prompt Standards

Use for data-backed analysis, dashboards, reports, KPI updates, metric diagnostics, market sizing, and analytical visuals.

## Required Prompt Inputs

- Question and decision the analysis should inform.
- Audience: executive, product, business, technical, operating team.
- Source of truth: dataset, warehouse, dashboard, spreadsheet, connector, provided file.
- Metric definitions, denominator, cohort, time window, and comparison baseline.
- Segments/dimensions to inspect.
- Desired output: answer, report, dashboard, KPI scorecard, chart, table, notebook.
- Evidence and caveat expectations.

## Source-Backed Analysis

Rewrite prompts to require:

- authoritative source selection
- live/fresh source reads when possible
- data quality checks for freshness, grain, joins, missingness, schema drift
- clear caveats when source access is incomplete
- recommendation tied to evidence, not just numbers

## Reports

Add:

- report audience and delivery mode
- answer-first narrative
- evidence order
- caveats and uncertainty
- recommended next step
- charts/tables only when they support a claim

## Dashboards

Add:

- dashboard purpose and monitoring cadence
- KPIs and definitions
- filters and dimensions
- status thresholds or targets
- actionability: what the viewer should do from the dashboard

Rewrite shape:

```text
请做一个数据分析/报告来回答 [question]，用于支持 [decision]。
受众：[audience]
数据来源：[source of truth or provided files]
指标定义：[metric/denominator/cohort/time window]
比较方式：[baseline/segments]
输出：[report/dashboard/chart/table/recommendation]
验证：[source checks/data quality/reconciliation/caveats]
```
