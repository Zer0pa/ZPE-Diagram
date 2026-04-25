# ZPE Diagram

## What This Is

ZPE Diagram is a bounded adopter for structural-with-style diagram encoding.

The current public evidence surface is limited to:

- structural line geometry
- bounded style preservation for the frozen 8-color palette plus quantized stroke width
- draw order as explicit state
- explicit rejection of fill, dashed input, and out-of-palette colors

Source: [validation/results/bounded_style_validation.json](validation/results/bounded_style_validation.json), [proofs/manifests/CURRENT_AUTHORITY_PACKET.md](proofs/manifests/CURRENT_AUTHORITY_PACKET.md), [tests/test_style_authority.py](tests/test_style_authority.py)

## CI-Backed Checks

| Code | Check | Evidence |
|-------|-------|-------|
| V_01 | `pytest tests/test_style_authority.py` | exercises style preservation, draw-order preservation, and bounded reject behavior |
| V_02 | `python proofs/artifacts/reproduce_validation.py` | regenerates `validation/results/bounded_style_validation.json` used by the authority packet |

## Proof Anchors

| Path | State |
|-------|-------|
| `proofs/manifests/CURRENT_AUTHORITY_PACKET.md` | VERIFIED |
| `proofs/artifacts/reproduce_validation.py` | VERIFIED |
| `validation/results/bounded_style_validation.json` | VERIFIED |
| `tests/test_style_authority.py` | VERIFIED |

## Quick Start

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python proofs/artifacts/reproduce_validation.py
python -m pytest tests/test_style_authority.py
```

## Scope

See [SCOPE.md](SCOPE.md) for the plain-language product boundary.

## Citation

Use [CITATION.cff](CITATION.cff) for software citation metadata.
