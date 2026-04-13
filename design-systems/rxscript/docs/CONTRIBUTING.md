# Contributing to RxScript Design

RxScript Design is the public, open-source design system for RxScriptor. Contributions welcome.

## Scope

- **In scope**: public tokens, components, docs, open-licensed assets.
- **Out of scope**: anything GC Biopharma-specific (colors, logo, Freesentation font licensing) — those belong to the private GCBP Design (`design-systems/gcbp/`).

## How to propose a change

1. Open an issue describing the token/component and the problem it solves.
2. Submit a PR editing `tokens/rxscript-tokens.css`, `docs/DESIGN-SYSTEM.md`, or both.
3. Keep the `--rx-*` namespace. Do not introduce `--gc-*` variables.

## Naming conventions

- CSS variables: `--rx-<category>-<name>` (e.g. `--rx-primary`, `--rx-space-lg`).
- Component classes (future): `.rx-<component>[__element][--modifier]` BEM-ish.

## License

By contributing you agree your contributions are licensed under the project's LICENSE (TBD, likely MIT).
