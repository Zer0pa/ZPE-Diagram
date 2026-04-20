# Architecture

`zpe-diagram` exposes one narrow runtime path:

1. `DiagramEncoder.add_svg()` parses SVG line geometry into normalized polylines.
2. `quantize_polylines()` snaps those polylines onto the integer grid.
3. `polylines_to_strokes()` converts them into `MoveTo` plus eight-direction draw steps.
4. `validate_style_scope()` accepts only the bounded style channel:
   - 8-color palette
   - stroke width quantized to `[1, 10]`
   - no fill
   - no dashed encode path
5. `pack_diagram_paths(..., encode_styles=True)` emits the public 20-bit word stream.
6. `unpack_diagram_words()` reconstructs the structural path plus bounded style payload.

The repo does not ship a broader shared-core runtime. The package is intentionally standalone.

