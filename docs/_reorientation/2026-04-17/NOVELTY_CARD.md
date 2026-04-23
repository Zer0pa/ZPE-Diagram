# ZPE-Diagram Novelty Card

**Product:** ZPE-Diagram
**Domain:** Deterministic bounded line-diagram encoding for structural Euclidean geometry with bounded style and explicit stroke-order state.
**What we sell:** Exact replay of structural line geometry plus a bounded style suffix and explicit draw-order preservation for controlled SVG diagram pipelines.

## Novel contributions

1. **Structural diagram base / bounded-style fiber separation** — A deterministic codec in which structural Euclidean line-diagram geometry is carried as the invariant base while bounded presentation style rides as a separately typed suffix layer. `src/zpe_diagram/encoder.py` enforces the bounded style contract before `pack_diagram_paths(..., encode_styles=True)` emits the public word stream, and `src/zpe_diagram/pack.py` reconstructs the structural path independently of the optional style suffix. The novel contribution is the product boundary itself: structure stays sovereign while bounded style is carried separately rather than being fused into the geometric path representation.

2. **Stroke-order as explicit separate state** — Draw order is preserved as explicit replay state rather than inferred later from rendering heuristics. `src/zpe_diagram/svg_io.py` collects drawable elements in document order, `src/zpe_diagram/quantize.py` converts them into ordered `MoveTo` / `DrawDir` command streams, and `src/zpe_diagram/pack.py` preserves that ordered path stream through packing and unpacking. The novel contribution is the explicit stroke-order replay contract on the bounded diagram surface.

3. **Typed input-rejection contract for out-of-bounds presentational classes** — `src/zpe_diagram/encoder.py` rejects fill, dashed input, and out-of-range stroke widths rather than silently coercing them into the bounded surface. The novel contribution is the explicit codec-level rejection contract tied to the declared public scope.

## Standard techniques used (explicit, not novel)

- Freeman-style 8-direction chain-code tokenization for stroke segments
- Run-length encoding for repeated draw directions
- Integer-grid quantization of input polylines
- SVG path parsing and polyline flattening
- Fixed-width bit packing for public word emission

## Compass-8 / 8-primitive architecture

NO (as a product claim). LICENSE §7.2 is authoritative.

The codec does use an internal 8-direction chain-code representation: the `DIRS` table is defined in `src/zpe_diagram/quantize.py`, and `_emit_run()` in `src/zpe_diagram/pack.py` packs `(direction, run_length)` pairs into the public word stream. That is an implementation technique, not the product-level novelty claim.

What this product claims as novel is narrower: structural-geometry base separation from bounded style, explicit stroke-order state, and typed rejection of out-of-bounds presentational classes.

## Open novelty questions for the license agent

- None in this pass. The §7.2 clarification is a wording correction, not a novelty-surface expansion.
