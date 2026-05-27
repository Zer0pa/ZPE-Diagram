# ZPE-Diagram

> Product-page mirror for `/encoding/ZPE-Diagram/`.
> Live public repo: [Zer0pa/ZPE-Diagram](https://github.com/Zer0pa/ZPE-Diagram).
> GitHub Markdown cannot reproduce the website typography, CSS, JavaScript, scroll behavior, or live bento layout; this README translates the product page into GitHub-safe Markdown evidence blocks.

## 0. Install / Developer Commands

The product page is the positioning authority. This section is the only retained developer-surface material from the previous root README.

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m pytest tests/test_style_authority.py
```

## Product Page Mirror

**Product-page title:** ZPE-Diagram · Bounded graph-structure diagram encoding · Zer0pa

**Product-page description:** ZPE-Diagram · bounded graph-structure diagram encoding · six declared synthetic SVGs round-trip exactly across geometry, color/stroke, and draw order · three OOD probes (fill, dash, palette escape) rejected at encode time · PyPI zpe-diagram 0.1.0 connected · not a compression codec.

### Hero Translation

> 00 · ZPE-DIAGRAM · GRAPH-STRUCTUREPYPI 0.1.0 · CONNECTED Encoding the Grammar of Diagrams Bounded structural diagram codec · ZPE-Diagram · PyPI zpe-diagram v0.1.0 · github.com/Zer0pa/ZPE-Diagram Most diagram exports flatten a structured drawing into a picture. Six declared synthetic SVGs round-trip through ZPE-Diagram as explicit graph state — geometry, color, stroke width, and draw order all exact. Three out-of-scope probes — fills, dashed strokes, palette escapes — are refused at the door instead of silently approximated. This is not compression and not a general SVG renderer. It is a bounded codec that keeps the rules that make a diagram readable as a diagram.

## Positioning

| Field | Value |
| --- | --- |
| Section | encoding |
| Product route | /encoding/ZPE-Diagram/ |
| Live public repository | https://github.com/Zer0pa/ZPE-Diagram |
| Repo identity used here | ZPE-Diagram |
| Website display identity | ZPE-Diagram |
| Verdict | STAGED |
| Posture | always_in_beta |
| Headline metric | 1.000 structural, style, and draw-order fidelity (6/6 cases); 1.000 rejection rate (3/3 out-of-scope probes). Useful now, improving continuously. |
| Honest blocker | We do not claim fill support; We do not claim dashed support on the encode path; We do not claim taper, pressure variation, or broader authorial-style recovery. |
| Mechanics asset from product page | DIAGRAM.gif |

## Key Metrics

| Metric | Value | Baseline |
| --- | --- | --- |
| structural_exact_worst | 1.000 (6/6 cases) | exact geometry reconstruction on every in-scope case |
| style_exact_worst | 1.000 (6/6 cases) | exact color + stroke-width preservation on every in-scope case |
| stroke_order_exact_worst | 1.000 (6/6 cases) | exact draw-order preservation on every in-scope case |
| reject_probe_rejection_rate | 1.000 (3/3 probes) | every out-of-scope input (fill, palette escape, dash) rejected at encode time |

## Proof Anchors

| Path | State |
| --- | --- |
| proofs/manifests/CURRENT_AUTHORITY_PACKET.md | VERIFIED |
| proofs/artifacts/reproduce_validation.py | VERIFIED |
| validation/results/bounded_style_validation.json | VERIFIED |
| tests/test_style_authority.py | VERIFIED |

## What We Prove

- Exact geometry reconstruction on every in-scope case in the public proof packet (structural_exact_worst = 1.000, 6/6 cases). Proof anchor: validation/results/bounded_style_validation.json.
- Exact color and stroke-width preservation on every in-scope case (style_exact_worst = 1.000, 6/6 cases). Proof anchor: validation/results/bounded_style_validation.json.
- Exact draw-order preservation on every in-scope case (stroke_order_exact_worst = 1.000, 6/6 cases). Proof anchor: validation/results/bounded_style_validation.json.
- Every out-of-scope input (fill, palette escape, dashed stroke) is rejected at encode time (reject_probe_rejection_rate = 1.000, 3/3 probes). Proof anchor: tests/test_style_authority.py.
- Structural and style axes are non-aliasing: same geometry/different style → style codes differ; different geometry/same style → geometry codes differ; same elements/different order → order codes differ. All separation metrics = 1.0.

## What We Do Not Claim

- No fill encoding. Fill inputs are explicitly rejected.
- No palette escape. Only the frozen 8-color palette is in scope; out-of-palette colors are rejected.
- No dashed stroke encoding. Dashed inputs are rejected at encode time.
- No arbitrary SVG coverage. The in-scope surface is line-based SVG with the frozen palette and solid strokes.
- No Compass-8 product claim. Any 8-direction technique is internal implementation, not product claim (Compass-8 posture: NO, per V2 §7.2).
- No compression claim. ZPE-Diagram is a structural-fidelity codec, not a compression codec.
- No claims outside the 6 in-scope synthetic SVG cases currently in the public proof packet.

## Blockers / Failures

> We do not claim fill support; We do not claim dashed support on the encode path; We do not claim taper, pressure variation, or broader authorial-style recovery.

## Verification Surface

| Code | Check | Verdict |
| --- | --- | --- |
| V_01 | pytest tests/test_style_authority.py — exercises style preservation, draw-order preservation, and bounded reject behavior | PASS |
| V_02 | python proofs/artifacts/reproduce_validation.py — regenerates validation/results/bounded_style_validation.json used by the authority packet | PASS |

## License

| Field | Value |
| --- | --- |
| License | LicenseRef-Zer0pa-SAL-7.1 |
| Authority source | validation/results/bounded_style_validation.json |

## Upcoming Workstreams

| Category | Summary |
| --- | --- |
| Active Engineering | Real-world SVG corpus expansion. Expand corpus from 6 synthetic SVGs to: Mermaid output (~30 cases), Graphviz output (~30 cases), one open UI icon set (~50 cases). Re-run existing fidelity test harness. Compass-8 NO posture preserved. |

## Related Repos

No related repos are declared on the product page frontmatter.

<details>
<summary>Full Visible Product-Page Bento Translation</summary>

This section preserves the product page cells as Markdown text blocks. It intentionally omits shared site navigation, footer chrome, CSS, and scripts.

### Bento Cell 1

> 00 · ZPE-DIAGRAM · GRAPH-STRUCTUREPYPI 0.1.0 · CONNECTED Encoding the Grammar of Diagrams Bounded structural diagram codec · ZPE-Diagram · PyPI zpe-diagram v0.1.0 · github.com/Zer0pa/ZPE-Diagram Most diagram exports flatten a structured drawing into a picture. Six declared synthetic SVGs round-trip through ZPE-Diagram as explicit graph state — geometry, color, stroke width, and draw order all exact. Three out-of-scope probes — fills, dashed strokes, palette escapes — are refused at the door instead of silently approximated. This is not compression and not a general SVG renderer. It is a bounded codec that keeps the rules that make a diagram readable as a diagram.

### Bento Cell 2

> 01 · THE GAPLOST IN EXPORT A diagram exported as an image loses the grammar that made it a diagram.

### Bento Cell 3

> 02 · MARKETSWEDGE MAP Diagramming software$1.9B Graphic design software$85.5B Technical documentation tooling$4.8B Standards-body technical drawing$0.8B Document archival software$7.3B Diagramming and adjacent archival categories · the wedge is line-based technical drawings, not the whole graphic design market.

### Bento Cell 4

> 03 · VALUE $1.9B2030 Diagramming software by 2030; ZPE-Diagram keeps line-based drawings readable as drawings after export.

### Bento Cell 5

> 04 · INSIGHT A diagram's grammar is the draw order, not the pixels.

### Bento Cell 6

> 05.1 · CURRENT TECHPIXELS ONLY Standard diagram exports preserve appearance, not intent. The file shows lines in roughly the right place while losing the structural roles, the connection types, and the order in which a person actually built the drawing.

### Bento Cell 7

> 05.2 · OUR TECHKEEP THE GRAMMAR ZPE-Diagram keeps the grammar. On six declared synthetic line-based SVGs, geometry, a frozen eight-color palette, quantized stroke width, and draw order all round-trip exactly. Three out-of-scope probes — fills, dashed strokes, palette escapes — are rejected at encode time rather than silently coerced into something they are not.

### Bento Cell 8

> 05.3 · BENCHMARKSVALIDATION Cases6SVGs Structure1.000exact Style1.000exact Order1.000exact structure1.000 style1.000 reject3 / 3 Source: bounded_style_validation.json · 6/6 in-scope at 1.000 · 3/3 out-of-scope refused.

### Bento Cell 9

> 06 · MEASUREMENTBOUNDED VALIDATION Six in-scope cases verified; three out-of-scope probes refused at encode.

### Bento Cell 10

> 06.1 · BOUNDED VALIDATIONSYNTHETIC SVG FIXTURES Structure1.000 Style (color + stroke)1.000 Draw order1.000 Out-of-scope reject3 / 3 Six declared synthetic SVGs (triangle ×2, square, parallel bars ×2, T-mixed) plus three reject probes (fill, dash, palette escape). Source: validation/results/bounded_style_validation.json. No comparator codec evaluated.

### Bento Cell 11

> 07 · KEY METRICSBOUNDED STRUCTURAL CODEC

### Bento Cell 12

> 07.1 · STRUCTURAL FIDELITY 6/ 6 Synthetic cases · structure, style, draw-order all exact

### Bento Cell 13

> 07.2 · OUT-OF-SCOPE REJECT 3/ 3 Probes refused · fill · dash · palette escape

### Bento Cell 14

> 07.3 · RELEASE v0.1.0 PyPI connected · zpe-diagram 0.1.0

### Bento Cell 15

> 07.4 · CHECKED PACKET VERIFIED Public validation packet · bounded synthetic scope

### Bento Cell 16

> 07.5 · COMPRESSION CLAIM none Not a compression codec · structure preserved, not file size

### Bento Cell 17

> 08 · DETERMINISMCOMMITTED FIXTURES Committed fixtures. Same bounded metrics.

### Bento Cell 18

> 08.1 · WHAT DETERMINISTIC MEANSFIXTURES + REJECTS Grammar here means something precise: the rules that make a drawing readable as a diagram rather than a pile of lines. Geometry encodes where elements sit. Style encodes how connections differ. Draw order encodes the sequence in which a person placed them. ZPE-Diagram keeps all three axes on committed fixtures and replays them byte-for-byte. On the bounded surface of six declared synthetic SVGs, structural, style, and draw-order fidelity each measure 1.000 — and the three out-of-scope probes never enter the packet.

### Bento Cell 19

> 08.2 · THE FIDELITY GAP Honest Blocker · No fill encode path. No dash encode path. No arbitrary SVG coverage. No compression claim. The current evidence is six synthetic fixtures plus three out-of-scope rejects. Real-world corpus closure, the is_diagram_header() boundary profile, and stroke-width normalization beyond the synthetic packet all remain open work.

### Bento Cell 20

> 09 DIAGRAMS WITH A RECEIPT.

### Bento Cell 21

> 09.1 · THE AMBITION The ambition is to make exported diagrams behave like the structured objects their authors meant them to be: archivable, comparable, searchable by structure rather than by pixel. A docs team, a standards committee, or an engineering archive should be able to trust that the drawing they store is the drawing they later retrieve.

### Bento Cell 22

> 09.2 · WHAT WORKS NOW Working today, on six declared synthetic SVGs: geometry, style, and draw order survive encoding exactly.

### Bento Cell 23

> 09.3 · WHAT'S STILL OPEN Still open: public corpora, header-boundary profile, and stroke-width handling outside the synthetic packet.

### Bento Cell 24

> 09.4 · DOCS · NEAR-TERM (12–24 MO) Docs teams keep diagram meaning A documentation team that exports a system diagram no longer ships a flat picture. The export carries node positions, line roles, and draw order, so the next writer can update the diagram instead of redrawing it from scratch.

### Bento Cell 25

> 09.5 · PIPELINES · NEAR-TERM (12–24 MO) Pipelines refuse the wrong input An archival pipeline that ingests diagrams now receives either a clean bounded object or a clear refusal. The operations team stops debugging silent visual corruption later and starts seeing rejection reasons at the moment of ingest.

### Bento Cell 26

> 09.6 · STANDARDS · MID-TERM (24–48 MO) Standards bodies archive structure, not screenshots ISO, IEEE, and ANSI technical drawing submissions can travel as structural objects with geometry, color, and draw order intact. A standards committee can compare two revisions of a wiring diagram or process flow without arguing about which export tool rendered it.

### Bento Cell 27

> 09.7 · DIFFS · MID-TERM (24–48 MO) Diagram review moves off pixel overlays Two versions of an architecture diagram become a structural diff: which boxes moved, which lines changed role, which elements were reordered. Reviewers stop squinting at overlaid screenshots and start reading change lists they can talk about in meetings.

### Bento Cell 28

> 09.8 · PROVENANCE · PARADIGM (48 MO+) Drawings acquire chain-of-custody A technical drawing in a regulatory submission, an engineering archive, or a patent filing can be proven identical or different across decades. Drawings stop being images and become governed structural objects that survive the people, vendors, and tools that produced them.

</details>

---

Source mapping: product route `/encoding/ZPE-Diagram/` -> live public repo `Zer0pa/ZPE-Diagram`. README generated from product-page authority plus retained install/dev commands only.
