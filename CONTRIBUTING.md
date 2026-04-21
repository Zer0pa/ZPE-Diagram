# Contributing

Thanks for working on `zpe-diagram`.

## Ground Rules

- Keep the public claim narrow: structural geometry plus the bounded style channel only.
- Do not widen the product claim in docs or code without new committed proof artifacts.
- Keep fills, dashed input, taper, and out-of-palette colors out of scope unless a new bounded proof packet lands.
- Use a named branch for changes. Owner review is required before merge.

## Submission Notes

- Run `python proofs/artifacts/reproduce_validation.py`.
- Run `python -m pytest tests/test_style_authority.py`.
- Update proof artifacts if any promoted metric changes.

By submitting a contribution, you confirm you have the right to submit the work and that the public claim remains backed by committed proof artifacts.
