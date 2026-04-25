# ZPE Diagram

## What This Is

ZPE Diagram is a bounded encoding product for structural-with-style diagram encoding. It is one of the 17 independent encoding products in the Zer0pa portfolio, alongside Image, Mental, Music, Smell, Taste, Touch, and the earlier public lanes.

The product claim is the structural-geometry base / bounded-style fiber separation: exact geometry reconstruction, exact color and stroke-width preservation, and explicit draw-order encoding — on every in-scope case in the public proof packet. **1.000 structural, style, and draw-order fidelity (6/6 cases); 1.000 rejection rate (3/3 out-of-scope probes).** Useful now, improving continuously.

The current public evidence surface is limited to:

- structural line geometry
- bounded style preservation for the frozen 8-color palette plus quantized stroke width
- draw order as explicit state
- explicit rejection of fill, dashed input, and out-of-palette colors

Source: [validation/results/bounded_style_validation.json](validation/results/bounded_style_validation.json), [proofs/manifests/CURRENT_AUTHORITY_PACKET.md](proofs/manifests/CURRENT_AUTHORITY_PACKET.md), [tests/test_style_authority.py](tests/test_style_authority.py), [LICENSE](LICENSE)

## Validation Summary

All results from [`validation/results/bounded_style_validation.json`](validation/results/bounded_style_validation.json) (regenerable via V_02):

| Metric | Value | What it means |
|--------|-------|---------------|
| `structural_exact_worst` | **1.000** (6/6 cases) | Exact geometry reconstruction on every in-scope case |
| `style_exact_worst` | **1.000** (6/6 cases) | Exact color + stroke-width preservation on every in-scope case |
| `stroke_order_exact_worst` | **1.000** (6/6 cases) | Exact draw-order preservation on every in-scope case |
| `reject_probe_rejection_rate` | **1.000** (3/3 probes) | Every out-of-scope input (fill, palette escape, dash) rejected at encode time |
| Style overhead | **3 words per styled path** | Compact: style suffix adds exactly 3 extension words per path |

**Separation controls** (same artifact, different axis — no aliasing):

| Control | Result |
|---------|--------|
| Same geometry, different style → style codes differ | `style_separation = 1.0` |
| Different geometry, same style → geometry codes differ | `structural_separation = 1.0` |
| Same elements, different draw order → order codes differ | `stroke_order_separation = 1.0` |

> Beta posture. These results cover the bounded in-scope surface (line-based SVG, frozen palette, solid strokes). No claim is made for arbitrary SVG.

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

## License

Zer0pa Source-Available License v7.0 — see [LICENSE](LICENSE).

## Citation

Use [CITATION.cff](CITATION.cff) for software citation metadata.
