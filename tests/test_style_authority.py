from __future__ import annotations

from pathlib import Path
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from zpe_diagram import DiagramEncoder, decode_words
from zpe_diagram.quantize import MoveTo


STYLE_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg">'
    '<polyline points="0,248 124,0 248,248 0,248" '
    'fill="none" stroke="#ff0000" stroke-width="4"/>'
    "</svg>"
)
ORDER_AB_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg">'
    '<line x1="0" y1="0" x2="0" y2="248" stroke="#ff0000" stroke-width="2"/>'
    '<line x1="248" y1="0" x2="248" y2="248" stroke="#0000ff" stroke-width="5"/>'
    "</svg>"
)
ORDER_BA_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg">'
    '<line x1="248" y1="0" x2="248" y2="248" stroke="#0000ff" stroke-width="5"/>'
    '<line x1="0" y1="0" x2="0" y2="248" stroke="#ff0000" stroke-width="2"/>'
    "</svg>"
)
FILLED_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg">'
    '<polygon points="0,248 124,0 248,248" fill="#00ff00" stroke="#ff0000" stroke-width="4"/>'
    "</svg>"
)
PALETTE_ESCAPE_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg">'
    '<polyline points="0,248 124,0 248,248 0,248" '
    'fill="none" stroke="#123456" stroke-width="4"/>'
    "</svg>"
)
DASHED_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg">'
    '<polyline points="0,248 124,0 248,248 0,248" '
    'fill="none" stroke="#ff0000" stroke-width="4" style="stroke-dasharray:8,4"/>'
    "</svg>"
)


def _decoded_paths(svg_text: str):
    return decode_words(DiagramEncoder().add_svg(svg_text, canvas_size=256).build())


def _first_move_x(path) -> int:
    for command in path.commands:
        if isinstance(command, MoveTo):
            return int(command.x)
    raise AssertionError("path missing MoveTo")


def test_add_svg_preserves_bounded_style_fiber() -> None:
    paths = _decoded_paths(STYLE_SVG)
    assert len(paths) == 1
    assert paths[0].stroke == "#ff0000"
    assert paths[0].stroke_width == 4.0
    assert paths[0].dash == "solid"
    assert paths[0].fill is None


def test_add_svg_preserves_stroke_order_state() -> None:
    paths_ab = _decoded_paths(ORDER_AB_SVG)
    paths_ba = _decoded_paths(ORDER_BA_SVG)

    assert [(path.stroke, path.stroke_width) for path in paths_ab] == [
        ("#ff0000", 2.0),
        ("#0000ff", 5.0),
    ]
    assert [(path.stroke, path.stroke_width) for path in paths_ba] == [
        ("#0000ff", 5.0),
        ("#ff0000", 2.0),
    ]
    assert [_first_move_x(path) for path in paths_ab] == [4, 252]
    assert [_first_move_x(path) for path in paths_ba] == [252, 4]


def test_add_svg_rejects_filled_shapes_out_of_scope() -> None:
    with pytest.raises(ValueError, match="diagram fill out of scope"):
        DiagramEncoder().add_svg(FILLED_SVG, canvas_size=256)


def test_add_svg_rejects_palette_escape_out_of_scope() -> None:
    with pytest.raises(ValueError, match="diagram stroke color out of scope"):
        DiagramEncoder().add_svg(PALETTE_ESCAPE_SVG, canvas_size=256)


def test_add_svg_rejects_dashed_input_out_of_scope() -> None:
    with pytest.raises(ValueError, match="diagram dash out of scope"):
        DiagramEncoder().add_svg(DASHED_SVG, canvas_size=256)
