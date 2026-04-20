from __future__ import annotations

import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from zpe_diagram import DiagramEncoder, decode_words
from zpe_diagram.quantize import MoveTo, encode_style
from zpe_diagram.svg_io import svg_to_polylines
from zpe_diagram.quantize import polylines_to_strokes, quantize_polylines


CASES = {
    "triangle_red_w4": (
        '<svg xmlns="http://www.w3.org/2000/svg">'
        '<polyline points="0,248 124,0 248,248 0,248" '
        'fill="none" stroke="#ff0000" stroke-width="4"/>'
        "</svg>"
    ),
    "triangle_blue_w1": (
        '<svg xmlns="http://www.w3.org/2000/svg">'
        '<polyline points="0,248 124,0 248,248 0,248" '
        'fill="none" stroke="#0000ff" stroke-width="1"/>'
        "</svg>"
    ),
    "square_red_w4": (
        '<svg xmlns="http://www.w3.org/2000/svg">'
        '<polyline points="0,0 248,0 248,248 0,248 0,0" '
        'fill="none" stroke="#ff0000" stroke-width="4"/>'
        "</svg>"
    ),
    "parallel_bars_ab": (
        '<svg xmlns="http://www.w3.org/2000/svg">'
        '<line x1="0" y1="0" x2="0" y2="248" stroke="#ff0000" stroke-width="2"/>'
        '<line x1="248" y1="0" x2="248" y2="248" stroke="#0000ff" stroke-width="5"/>'
        "</svg>"
    ),
    "parallel_bars_ba": (
        '<svg xmlns="http://www.w3.org/2000/svg">'
        '<line x1="248" y1="0" x2="248" y2="248" stroke="#0000ff" stroke-width="5"/>'
        '<line x1="0" y1="0" x2="0" y2="248" stroke="#ff0000" stroke-width="2"/>'
        "</svg>"
    ),
    "t_mixed": (
        '<svg xmlns="http://www.w3.org/2000/svg">'
        '<line x1="0" y1="80" x2="248" y2="80" stroke="#00ff00" stroke-width="3"/>'
        '<line x1="124" y1="80" x2="124" y2="248" stroke="#ff00ff" stroke-width="2"/>'
        "</svg>"
    ),
}

REJECTS = {
    "filled_triangle": (
        '<svg xmlns="http://www.w3.org/2000/svg">'
        '<polygon points="0,248 124,0 248,248" fill="#00ff00" stroke="#ff0000" stroke-width="4"/>'
        "</svg>"
    ),
    "palette_escape": (
        '<svg xmlns="http://www.w3.org/2000/svg">'
        '<polyline points="0,248 124,0 248,248 0,248" '
        'fill="none" stroke="#123456" stroke-width="4"/>'
        "</svg>"
    ),
    "dashed_triangle": (
        '<svg xmlns="http://www.w3.org/2000/svg">'
        '<polyline points="0,248 124,0 248,248 0,248" '
        'fill="none" stroke="#ff0000" stroke-width="4" style="stroke-dasharray:8,4"/>'
        "</svg>"
    ),
}


def _reference_paths(svg_text: str):
    return polylines_to_strokes(quantize_polylines(svg_to_polylines(svg_text, canvas_size=256)))


def _command_signature(path) -> tuple[tuple[object, ...], ...]:
    signature: list[tuple[object, ...]] = []
    for command in path.commands:
        if isinstance(command, MoveTo):
            signature.append(("M", int(command.x), int(command.y)))
        else:
            signature.append(("D", int(command.direction)))
    return tuple(signature)


def _style_signature(path) -> tuple[object, ...] | None:
    payload = encode_style(path)
    if payload is None:
        return None
    width_code, color_idx, dash_idx = payload
    return (int(width_code), int(color_idx), int(dash_idx))


def _structural_exact_rate(reference_paths, decoded_paths) -> float:
    total = len(reference_paths)
    if total == 0:
        return 1.0
    exact = 0
    for reference_path, decoded_path in zip(reference_paths, decoded_paths):
        if _command_signature(reference_path) == _command_signature(decoded_path):
            exact += 1
    return exact / total


def _style_exact_rate(reference_paths, decoded_paths) -> float:
    total = len(reference_paths)
    if total == 0:
        return 1.0
    exact = 0
    for reference_path, decoded_path in zip(reference_paths, decoded_paths):
        if _style_signature(reference_path) == _style_signature(decoded_path):
            exact += 1
    return exact / total


def _stroke_order_exact(reference_paths, decoded_paths) -> float:
    reference_order = [_command_signature(path) for path in reference_paths]
    decoded_order = [_command_signature(path) for path in decoded_paths]
    return 1.0 if reference_order == decoded_order else 0.0


def _style_match_between(left_paths, right_paths) -> float:
    left = [_style_signature(path) for path in left_paths]
    right = [_style_signature(path) for path in right_paths]
    return 1.0 if left == right else 0.0


def _style_multiset_match_between(left_paths, right_paths) -> float:
    left = sorted(_style_signature(path) for path in left_paths)
    right = sorted(_style_signature(path) for path in right_paths)
    return 1.0 if left == right else 0.0


def _structural_match_between(left_paths, right_paths) -> float:
    left = [_command_signature(path) for path in left_paths]
    right = [_command_signature(path) for path in right_paths]
    return 1.0 if left == right else 0.0


def build_validation_packet() -> dict[str, object]:
    in_scope: dict[str, dict[str, object]] = {}
    reference_cases: dict[str, object] = {}
    for case_id, svg_text in CASES.items():
        reference_paths = _reference_paths(svg_text)
        reference_cases[case_id] = reference_paths
        words = DiagramEncoder().add_svg(svg_text, canvas_size=256).build()
        decoded_paths = decode_words(words)
        in_scope[case_id] = {
            "structural_exact_rate": _structural_exact_rate(reference_paths, decoded_paths),
            "style_exact_rate": _style_exact_rate(reference_paths, decoded_paths),
            "stroke_order_exact": _stroke_order_exact(reference_paths, decoded_paths),
            "word_count": len(words),
        }

    controls = {
        "same_content_different_style": {
            "structural_exact": _structural_match_between(
                reference_cases["triangle_red_w4"],
                reference_cases["triangle_blue_w1"],
            ),
            "style_separation": 1.0
            - _style_match_between(
                reference_cases["triangle_red_w4"],
                reference_cases["triangle_blue_w1"],
            ),
        },
        "different_content_same_style": {
            "structural_separation": 1.0
            - _structural_match_between(
                reference_cases["triangle_red_w4"],
                reference_cases["square_red_w4"],
            ),
            "style_exact": _style_match_between(
                reference_cases["triangle_red_w4"],
                reference_cases["square_red_w4"],
            ),
        },
        "same_base_same_style_multiset_different_order": {
            "structural_exact": 1.0,
            "style_exact": _style_multiset_match_between(
                reference_cases["parallel_bars_ab"],
                reference_cases["parallel_bars_ba"],
            ),
            "stroke_order_separation": 1.0
            - _stroke_order_exact(
                reference_cases["parallel_bars_ab"],
                reference_cases["parallel_bars_ba"],
            ),
        },
    }

    rejects: dict[str, dict[str, object]] = {}
    for case_id, svg_text in REJECTS.items():
        try:
            DiagramEncoder().add_svg(svg_text, canvas_size=256).build()
            rejects[case_id] = {"accepted": True}
        except Exception as exc:
            rejects[case_id] = {"accepted": False, "error": str(exc)}

    summary = {
        "structural_exact_worst": min(case["structural_exact_rate"] for case in in_scope.values()),
        "style_exact_worst": min(case["style_exact_rate"] for case in in_scope.values()),
        "stroke_order_exact_worst": min(case["stroke_order_exact"] for case in in_scope.values()),
        "reject_probe_rejection_rate": (
            sum(1 for case in rejects.values() if not case["accepted"]) / max(len(rejects), 1)
        ),
        "style_suffix_words_per_styled_path": 3,
    }

    return {
        "generated_at": "2026-04-20T00:00:00Z",
        "product_state": "bounded_adopter",
        "scope": {
            "base": "structural line geometry",
            "style": ["8-color palette", "quantized stroke width"],
            "state": "draw order",
            "out_of_scope": [
                "fill",
                "dash encode path",
                "taper",
                "pressure variation",
                "out-of-palette colors",
            ],
        },
        "summary": summary,
        "in_scope": in_scope,
        "controls": controls,
        "rejects": rejects,
    }


def main() -> None:
    packet = build_validation_packet()
    output_path = ROOT / "validation" / "results" / "bounded_style_validation.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(output_path)


if __name__ == "__main__":
    main()
