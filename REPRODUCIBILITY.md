# Reproducibility

## Canonical Inputs

- `proofs/artifacts/reproduce_validation.py` inline `CASES` corpus for the six in-scope bounded SVG fixtures
- `proofs/artifacts/reproduce_validation.py` inline `REJECTS` corpus for the three out-of-scope rejection probes
- `tests/test_style_authority.py` focused authority assertions over the same bounded public surface

## Golden-Bundle Hash

will be populated by the `receipt-bundle.yml` workflow in Wave 3

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

- CPython `>=3.11`
- Fresh-clone execution from the repo root in a local POSIX shell environment (`bash` or `zsh`)
