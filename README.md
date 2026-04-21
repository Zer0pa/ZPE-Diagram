# ZPE Diagram

## What This Is

ZPE Diagram is an always-in-beta bounded adopter for controlled line-based SVG inputs. It preserves structural geometry, a bounded style channel, and draw order inside a narrow public scope that is useful now for deterministic diagram pipelines. The public claim is structural-with-style only, and it does not claim general SVG coverage.

| Field | Value |
|-------|-------|
| Architecture | DIAGRAM_STREAM |
| Encoding | DIAGRAM_STYLE_SUFFIX_V1 |

## Key Metrics

| Metric | Value | Baseline |
|-------|-------|-------|
| STRUCTURAL_EXACT | 1.00 | Reference |
| STYLE_EXACT | 1.00 | Reference |
| ORDER_STATE | 6/6 | Cases |
| REJECT_PROBES | 3/3 | Unsupported |

> Source: [bounded_style_validation.json](validation/results/bounded_style_validation.json), [CURRENT_AUTHORITY_PACKET.md](proofs/manifests/CURRENT_AUTHORITY_PACKET.md)

## What We Prove

- Structural line geometry survives the public word stream exactly on the bounded validation set.
- The bounded style channel preserves only the frozen 8-color palette plus quantized stroke width.
- Draw order survives as explicit state on the same bounded validation set.
- Unsupported fill, dashed input, and out-of-palette colors are rejected instead of silently collapsing.

## What We Don't Claim

- We do not claim fill support.
- We do not claim dashed support on the encode path.
- We do not claim taper, pressure variation, or broader authorial-style recovery.
- We do not claim out-of-palette color identity.
- We do not claim arbitrary SVG coverage or general illustration semantics.

## Commercial Readiness

This local remediation surface is pending final authority restamp.

| Field | Value |
|-------|-------|
| Verdict | PASS |
| Commit SHA | UNSTAMPED |
| Confidence | 100% |
| Source | validation/results/bounded_style_validation.json |

## Tests and Verification

| Code | Check | Verdict |
|-------|-------|-------|
| V_01 | `pytest tests/test_style_authority.py` | PASS |
| V_02 | `python proofs/artifacts/reproduce_validation.py` | PASS |
| V_03 | bounded reject probes for fill, dashed input, and palette escape | PASS |

## Proof Anchors

| Path | State |
|-------|-------|
| `proofs/manifests/CURRENT_AUTHORITY_PACKET.md` | VERIFIED |
| `proofs/artifacts/reproduce_validation.py` | VERIFIED |
| `validation/results/bounded_style_validation.json` | VERIFIED |
| `tests/test_style_authority.py` | VERIFIED |

## Repo Shape

| Field | Value |
|-------|-------|
| Proof Anchors | 4 |
| Modality Lanes | 1 |
| Authority Source | `validation/results/bounded_style_validation.json` |
| Package Root | `src/zpe_diagram` |

## Quick Start

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python proofs/artifacts/reproduce_validation.py
python -m pytest tests/test_style_authority.py
```

### Scope

See [SCOPE.md](SCOPE.md) for the plain-language product boundary.

### Citation

Use [CITATION.cff](CITATION.cff) for software citation metadata.

### Open Risks (Non-Blocking)

- The public scope is intentionally narrow.
- The encode path rejects fills, dashed input, and out-of-palette colors.
- Wider SVG claims need new proof artifacts before they belong in this repo.
