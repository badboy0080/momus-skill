# Knowledge Base Expansion Guide

Use this file when adding future domain prompt standards to Momus.

## File Structure

Add new files under `references/prompt-standards/` using this naming pattern:

```text
NN-domain-name.md
```

Keep each file focused on one domain. Do not create one giant catch-all reference.

## Required Sections

Every domain file should include:

- When to use
- Required prompt inputs
- Rewrite shape
- Weak prompt smells
- Verification or acceptance fields
- Optional specialized subdomains

## Index Update

After adding a file, update `00-index.md`:

- add the file to `Domain Files`
- add selection rules
- mention source influence if the file is distilled from another skill or knowledge source

## Extraction Method

When mining another skill or knowledge source:

1. Identify the workflow the skill enforces.
2. Extract the questions it implicitly needs answered before execution.
3. Convert those questions into required prompt inputs.
4. Add a concise rewrite shape.
5. Add weak prompt smells that should trigger Momus.
6. Keep procedural tool details out unless they affect user prompt quality.

When mining installed plugins:

- record the plugin cache path as source influence in `00-index.md`
- preserve category names that help retrieval
- do not copy large passages from plugin skills
- translate hard gates into prompt inputs, verification fields, and weak-prompt smells
- keep platform-specific tool mechanics out unless the user's prompt must specify them

## Quality Rules

- Prefer checklists over prose.
- Keep examples short and reusable.
- Do not copy large passages from source skills.
- Do not add speculative fields that are rarely useful.
- Keep categories stable so external knowledge-base tooling can index them.
