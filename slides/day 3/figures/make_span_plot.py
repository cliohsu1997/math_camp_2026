"""Span of two vectors in the plane."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"
BG = "#E8EEF0"
OUT_DIR = Path(__file__).resolve().parent

V1 = np.array([2.4, 0.9])
V2 = np.array([0.8, 2.3])


def _arrow(
    ax: plt.Axes,
    start: np.ndarray,
    vec: np.ndarray,
    color: str,
    label: str,
    label_offset: tuple[float, float],
) -> None:
    end = start + vec
    ax.annotate(
        "",
        xy=end,
        xytext=start,
        arrowprops={
            "arrowstyle": "->",
            "color": color,
            "lw": 2.4,
            "shrinkA": 0.0,
            "shrinkB": 0.0,
        },
        zorder=4,
    )
    ax.annotate(
        label,
        xy=end,
        xytext=(end[0] + label_offset[0], end[1] + label_offset[1]),
        fontsize=12,
        color=color,
        ha="left",
        va="bottom",
    )


def make_span_two_vectors_plot() -> None:
    fig, ax = plt.subplots(figsize=(6.8, 5.6), dpi=220)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)

    # Direction lines through the origin.
    t = np.linspace(-2.2, 2.2, 2)
    ax.plot(t * V1[0], t * V1[1], color=DARK_TEAL, lw=1.0, ls=":", alpha=0.45, zorder=2)
    ax.plot(t * V2[0], t * V2[1], color=ACCENT, lw=1.0, ls=":", alpha=0.45, zorder=2)

    # Example parallelogram (fill only).
    para = np.array([[0.0, 0.0], V1, V1 + V2, V2])
    ax.add_patch(
        Polygon(
            para,
            closed=True,
            facecolor=ACCENT,
            edgecolor="none",
            alpha=0.16,
            zorder=3,
        )
    )

    _arrow(ax, np.zeros(2), V1, DARK_TEAL, "v1", (0.08, 0.08))
    _arrow(ax, np.zeros(2), V2, ACCENT, "v2", (0.08, 0.08))
    _arrow(ax, V1, V2, DARK_TEAL, "v1 + v2", (0.10, 0.05))

    ax.plot(0.0, 0.0, "o", color=DARK_TEAL, markersize=6, zorder=5)
    ax.annotate(
        "0",
        xy=(0.0, 0.0),
        xytext=(-0.35, -0.45),
        fontsize=11,
        color="0.25",
    )
    ax.annotate(
        "span{v1, v2}\n= whole plane",
        xy=(0.0, 0.0),
        xytext=(1.6, -2.8),
        fontsize=12,
        color=DARK_TEAL,
        ha="center",
    )
    ax.annotate(
        "c1 v1 + c2 v2",
        xy=(0.5 * V1[0] + 0.5 * V2[0], 0.5 * V1[1] + 0.5 * V2[1]),
        xytext=(-3.2, 3.0),
        fontsize=11,
        color="0.35",
        arrowprops={
            "arrowstyle": "->",
            "color": "0.45",
            "lw": 1.1,
            "connectionstyle": "arc3,rad=0.15",
        },
    )

    ax.axhline(0.0, color="0.35", lw=0.9, zorder=2)
    ax.axvline(0.0, color="0.35", lw=0.9, zorder=2)
    ax.set_xlim(-4.5, 4.8)
    ax.set_ylim(-4.5, 4.8)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("x1", fontsize=12)
    ax.set_ylabel("x2", fontsize=12)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.grid(False)

    out = OUT_DIR / "span_two_vectors.png"
    fig.subplots_adjust(left=0.12, right=0.96, bottom=0.14, top=0.96)
    fig.savefig(
        out,
        bbox_inches="tight",
        facecolor=BG,
        edgecolor="none",
        pad_inches=0.12,
    )
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    make_span_two_vectors_plot()
