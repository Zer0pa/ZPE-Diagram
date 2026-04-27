# ZPE Diagram

## What This Is

ZPE Diagram is a bounded encoding product for structural-with-style diagram encoding. It is one of the 17 independent encoding products in the Zer0pa portfolio, alongside Image, Mental, Music, Smell, Taste, Touch, and the earlier public lanes.

The product claim is the structural-geometry base / bounded-style fiber separation: exact geometry reconstruction, exact color and stroke-width preservation, and explicit draw-order encoding — on every in-scope case in the public proof packet. **1.000 structural, style, and draw-order fidelity (6/6 cases); 1.000 rejection rate (3/3 out-of-scope probes).** Useful now, improving continuously.

The current public evidence surface is limited to:

- structural line geometry
- bounded style preservation for the frozen 8-color palette plus quantized stroke width
- draw order as explicit state
- explicit rejection of fill, dashed input, and out-of-palette colors

Compass-8 posture (per V2 §7.2): NO. Any 8-direction technique used internally is implementation, not product claim.

Licensed under the [Zer0pa Source-Available License v7.0](LICENSE). Source: [validation/results/bounded_style_validation.json](validation/results/bounded_style_validation.json), [proofs/manifests/CURRENT_AUTHORITY_PACKET.md](proofs/manifests/CURRENT_AUTHORITY_PACKET.md), [tests/test_style_authority.py](tests/test_style_authority.py)

| Field | Value |
|-------|-------|
| Architecture | DIAGRAM_STREAM |
| Encoding | DIAGRAM_BOUNDED_STYLE_V1 |

## Key Metrics

| Metric | Value | Baseline |
|--------|-------|----------|
| `structural_exact_worst` | **1.000** (6/6 cases) | exact geometry reconstruction on every in-scope case |
| `style_exact_worst` | **1.000** (6/6 cases) | exact color + stroke-width preservation on every in-scope case |
| `stroke_order_exact_worst` | **1.000** (6/6 cases) | exact draw-order preservation on every in-scope case |
| `reject_probe_rejection_rate` | **1.000** (3/3 probes) | every out-of-scope input (fill, palette escape, dash) rejected at encode time |

> Source: [`validation/results/bounded_style_validation.json`](validation/results/bounded_style_validation.json), regenerable via V_02.

## What We Prove

- Exact geometry reconstruction on every in-scope case in the public proof packet (structural_exact_worst = 1.000, 6/6 cases). Proof anchor: `validation/results/bounded_style_validation.json`.
- Exact color and stroke-width preservation on every in-scope case (style_exact_worst = 1.000, 6/6 cases). Proof anchor: `validation/results/bounded_style_validation.json`.
- Exact draw-order preservation on every in-scope case (stroke_order_exact_worst = 1.000, 6/6 cases). Proof anchor: `validation/results/bounded_style_validation.json`.
- Every out-of-scope input (fill, palette escape, dashed stroke) is rejected at encode time (reject_probe_rejection_rate = 1.000, 3/3 probes). Proof anchor: `tests/test_style_authority.py`.
- Structural and style axes are non-aliasing: same geometry/different style → style codes differ; different geometry/same style → geometry codes differ; same elements/different order → order codes differ. All separation metrics = 1.0.

## What We Don't Claim

- No fill encoding. Fill inputs are explicitly rejected.
- No palette escape. Only the frozen 8-color palette is in scope; out-of-palette colors are rejected.
- No dashed stroke encoding. Dashed inputs are rejected at encode time.
- No arbitrary SVG coverage. The in-scope surface is line-based SVG with the frozen palette and solid strokes.
- No Compass-8 product claim. Any 8-direction technique is internal implementation, not product claim (Compass-8 posture: NO, per V2 §7.2).
- No compression claim. ZPE-Diagram is a structural-fidelity codec, not a compression codec.
- No claims outside the 6 in-scope synthetic SVG cases currently in the public proof packet.

## Commercial Readiness

| Field | Value |
|-------|-------|
| Verdict | STAGED |
| Commit SHA | 71a5950 |
| Source | `validation/results/bounded_style_validation.json` |

## Tests and Verification

| Code | Check | Verdict |
|------|-------|---------|
| V_01 | `pytest tests/test_style_authority.py` — exercises style preservation, draw-order preservation, and bounded reject behavior | PASS |
| V_02 | `python proofs/artifacts/reproduce_validation.py` — regenerates `validation/results/bounded_style_validation.json` used by the authority packet | PASS |

## Proof Anchors

| Path | State |
|------|-------|
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
| Compass-8 Posture | NO (internal technique only) |

## Quick Start

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python proofs/artifacts/reproduce_validation.py
python -m pytest tests/test_style_authority.py
```

## Upcoming Workstreams

This section captures the active lane priorities — what the next agent or contributor picks up, and what investors should expect. Cadence is continuous, not milestoned.

- **Real-world SVG corpus expansion** — Active Engineering. Expand corpus from 6 synthetic SVGs to: Mermaid output (~30 cases), Graphviz output (~30 cases), one open UI icon set (~50 cases). Re-run existing fidelity test harness. Compass-8 NO posture preserved.

### Scope

See [SCOPE.md](SCOPE.md) for the plain-language product boundary.

### Citation

Use [CITATION.cff](CITATION.cff) for software citation metadata.
