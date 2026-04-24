# Reproducibility

## Canonical Inputs

- `proofs/artifacts/reproduce_validation.py` — bounded validation cases that regenerate `validation/results/bounded_style_validation.json`.
- `tests/test_style_authority.py` — inline SVG fixtures covering the bounded style surface, draw-order preservation, and explicit reject cases.

## Golden-Bundle Hash

This field will be populated by the `receipt-bundle.yml` workflow in Wave 3.

## Verification Command

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python proofs/artifacts/reproduce_validation.py
python -m pytest tests/test_style_authority.py
```

## Supported Runtimes

- Python 3.11 and newer
- Local package install from the repo root
- Deterministic validation on standard Python runtimes for macOS, Linux, and Windows
