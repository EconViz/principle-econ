# CHANGELOG

All notable changes to this project are documented in this file.

## v0.1.0 (2026-04-25)

### Features

- Build a modular package architecture for Principles of Economics linear market analysis:
  - `core` for lines/equilibrium/shifts/controls/elasticity
  - `policy` for tax models, incidence, comparisons, and visual guides
  - `welfare` for CS/PS/tax-revenue/TS/DWL and report helpers
  - `plot` for canvas/figure facade and focused renderers
  - `api` and `cli` facades
- Add tax support for fixed, per-unit, and ad valorem taxes, including consumer-side and producer-side legal incidence.
- Add tax transformation plotting semantics:
  - directional tax-shift arrows (`baseline -> policy`)
  - ad valorem proportional rotation overlays
- Add welfare transition overlays with baseline/policy guide lines and labeled regions (`A/B/C/...`).
- Add monochrome palette and support for `default`, `colorblind`, `nord`, and `monochrome` models.
- Add classroom examples grouped by topic under `examples/scipts/`.

### Tests

- Add unit tests across core, policy, welfare, and palette modules.
- Add plotting smoke tests for equilibrium, comparative statics, tax transforms, and welfare transitions.
- Add CLI smoke tests for equilibrium and tax commands.

### Tooling

- Manage package via Poetry (`pyproject.toml`, `poetry.lock`).
- Add lint/test setup with Ruff and Pytest.
- Add GitHub Actions workflow for CI + PyPI publishing via Trusted Publishing on tag pushes.
