from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Sequence

from .pack import pack_diagram_paths, unpack_diagram_words
from .quantize import STYLE_COLORS, StrokePath, polylines_to_strokes, quantize_polylines
from .svg_io import svg_to_polylines


def _expand_style_color(color: str) -> str:
    canonical = color.strip().lower()
    if len(canonical) == 4 and canonical.startswith("#"):
        canonical = "#" + "".join(ch * 2 for ch in canonical[1:])
    return canonical


def validate_style_scope(paths: Sequence[StrokePath]) -> None:
    for path_index, path in enumerate(paths):
        fill = (path.fill or "").strip().lower()
        if fill not in ("", "none"):
            raise ValueError(f"diagram fill out of scope on path {path_index}: {path.fill!r}")
        path.fill = None

        dash = (path.dash or "").strip().lower()
        if dash in ("", "none", "solid"):
            path.dash = None
        else:
            raise ValueError(f"diagram dash out of scope on path {path_index}: {path.dash!r}")

        if path.stroke is not None:
            canonical_color = _expand_style_color(path.stroke)
            if canonical_color not in STYLE_COLORS:
                raise ValueError(f"diagram stroke color out of scope on path {path_index}: {path.stroke!r}")
            path.stroke = canonical_color

        if path.stroke_width is not None:
            width_code = int(round(path.stroke_width))
            if width_code < 1 or width_code > 10:
                raise ValueError(
                    f"diagram stroke width out of scope on path {path_index}: {path.stroke_width!r}"
                )
            path.stroke_width = float(width_code)


@dataclass
class DiagramEncoder:
    _stream: List[int] = field(default_factory=list)

    def add_svg(self, svg_string: str, canvas_size: int = 256) -> "DiagramEncoder":
        polylines = svg_to_polylines(svg_string, canvas_size=canvas_size)
        paths = polylines_to_strokes(quantize_polylines(polylines))
        validate_style_scope(paths)
        self._stream.extend(pack_diagram_paths(paths, canvas_size=canvas_size, encode_styles=True))
        return self

    def build(self) -> List[int]:
        return list(self._stream)


def encode_svg(svg_string: str, canvas_size: int = 256) -> List[int]:
    return DiagramEncoder().add_svg(svg_string, canvas_size=canvas_size).build()


def decode_words(words: Sequence[int]) -> List[StrokePath]:
    return unpack_diagram_words(words)

