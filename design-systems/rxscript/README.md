# RxScript Design

Public design system for RxScriptor. Currently in **v0.1 skeleton** state — tokens are placeholders, components are unwritten.

## Contents

- `tokens/rxscript-tokens.css` — CSS custom properties (`--rx-*`), base typography
- `docs/` — specification scaffold (DESIGN-SYSTEM.md, CONTRIBUTING.md, LICENSE.md)
- `logo/` — (TBD)

## Use in a project

```yaml
# projects/<name>/_metadata.yml
format:
  html:
    css:
      - /design-systems/rxscript/tokens/rxscript-tokens.css
```

## Namespace

`--rx-*` variables and (future) `.rx-*` classes. The `--gc-*` / `.gc-*` namespace is reserved for GCBP Design (private).

## Status

See `docs/DESIGN-SYSTEM.md` for the section-by-section TBD checklist.
