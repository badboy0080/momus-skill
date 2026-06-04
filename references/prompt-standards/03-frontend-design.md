# Frontend and Design Prompt Standards

Use for frontend UI, web apps, landing pages, dashboards, redesigns, visual implementation, image-to-code, and mobile/web screen design.

## Required Prompt Inputs

- Surface type: landing page, dashboard, form, editor, app shell, portfolio, redesign, component, game, mobile screen.
- Audience and use case.
- Visual direction: brand, vibe, references, screenshots, or design system.
- Existing stack: React/Next/Vite, CSS/Tailwind/version, component libraries, icon libraries.
- Content and assets: copy, images, logo, data, placeholders allowed or not.
- Interaction states: hover, active, focus, loading, empty, error, disabled.
- Responsive requirements: desktop/mobile/tablet and critical breakpoints.
- Verification: browser screenshot, responsive QA, accessibility, no clipping/overlap, text fitting.

## Rewrite Shape

```text
请基于当前项目实现 [frontend surface]。
先做一句 design read：这是 [surface type]，面向 [audience]，视觉方向偏 [style/system]。
上下文：[existing stack/assets/current UI]
目标：[desired user-visible result]
范围：[pages/components/files]
视觉要求：[brand/vibe/references/layout density]
交互状态：[loading/empty/error/hover/focus/etc.]
响应式：[viewports/breakpoints]
验证：[browser screenshot/responsive/a11y/no overlap/text fit]
输出：[changed files + verification summary]
```

## Redesign

Add:

- preserve vs overhaul
- existing visual problems
- functionality that must not break
- stack and styling system
- visual QA expectations

## Image-to-Code

Add:

- source image/reference role
- fidelity target
- which details matter: layout, spacing, typography, colors, assets, responsive behavior
- browser verification requirement

## Weak Prompt Smells

- "做个好看的页面" without audience, surface type, content, or stack.
- "高级一点" without visual direction or references.
- "照这个图做" without fidelity level, viewport, or what may differ.
- "优化 UI" without saying whether to preserve functionality or redesign broadly.
