"""Determinant as parallelogram area (2x2): ad - bc illustration."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.path import Path as MplPath
from matplotlib.patches import Polygon, Rectangle

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"
VIOLET = "#6B4C9A"
BG = "#E8EEF0"
OUT_DIR = Path(__file__).resolve().parent


def _arrow(
    ax: plt.Axes,
    start: np.ndarray,
    vec: np.ndarray,
    color: str,
    label: str,
    label_offset: tuple[float, float],
    *,
    lw: float = 2.4,
    fontsize: float = 11,
) -> None:
    end = start + vec
    ax.annotate(
        "",
        xy=end,
        xytext=start,
        arrowprops={
            "arrowstyle": "->",
            "color": color,
            "lw": lw,
            "shrinkA": 0.0,
            "shrinkB": 0.0,
        },
        zorder=6,
    )
    ax.annotate(
        label,
        xy=end,
        xytext=(end[0] + label_offset[0], end[1] + label_offset[1]),
        fontsize=fontsize,
        color=color,
        ha="left",
        va="bottom",
    )


def _style_ax(ax: plt.Axes, xlim: tuple[float, float], ylim: tuple[float, float]) -> None:
    ax.axhline(0.0, color="0.35", lw=0.9, zorder=1)
    ax.axvline(0.0, color="0.35", lw=0.9, zorder=1)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("$x_1$", fontsize=11)
    ax.set_ylabel("$x_2$", fontsize=11)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.grid(False)


def make_det_area_parallelogram() -> None:
    """Parallelogram for A=[[3,1],[1,2]]: det = ad-bc = 5."""
    a, b, c, d = 3.0, 1.0, 1.0, 2.0
    col1 = np.array([a, c])
    col2 = np.array([b, d])
    det = a * d - b * c
    box_w, box_h = a + b, c + d

    # Parallelogram: O, a1, a1+a2, a2 (in order around the polygon).
    para = np.array(
        [
            [0.0, 0.0],
            col1,
            col1 + col2,
            col2,
        ]
    )
    unit_sq = np.array([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0]])

    fig, ax = plt.subplots(figsize=(6.8, 5.8), dpi=220)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)

    # Shade region inside bounding box but outside parallelogram (trim pieces).
    para_path = MplPath(para)
    grid_n = 120
    xs = np.linspace(0.0, box_w, grid_n)
    ys = np.linspace(0.0, box_h, grid_n)
    xx, yy = np.meshgrid(xs, ys)
    pts = np.column_stack([xx.ravel(), yy.ravel()])
    inside_para = para_path.contains_points(pts).reshape(xx.shape)
    outside = ~inside_para
    ax.contourf(
        xx,
        yy,
        outside.astype(float),
        levels=[0.5, 1.5],
        colors=[VIOLET],
        alpha=0.18,
        zorder=2,
    )

    # Bounding box (a+b) x (c+d).
    ax.add_patch(
        Rectangle(
            (0.0, 0.0),
            box_w,
            box_h,
            fill=False,
            edgecolor="0.55",
            lw=1.3,
            ls="--",
            zorder=3,
        )
    )

    # Unit square spanned by (1,0) and (0,1) before A (area 1).
    ax.add_patch(
        Polygon(
            unit_sq,
            closed=True,
            fill=False,
            edgecolor="0.45",
            lw=1.2,
            ls=":",
            zorder=3,
        )
    )

    # Image parallelogram spanned by A e1 and A e2.
    ax.add_patch(
        Polygon(
            para,
            closed=True,
            facecolor=ACCENT,
            edgecolor=DARK_TEAL,
            lw=2.0,
            alpha=0.35,
            zorder=4,
        )
    )

    # Complete parallelogram edges (shifted copy of a2 from tip of a1).
    ax.plot(
        [col1[0], col1[0] + col2[0]],
        [col1[1], col1[1] + col2[1]],
        color=DARK_TEAL,
        lw=1.4,
        ls="-",
        zorder=4,
    )
    ax.plot(
        [col2[0], col1[0] + col2[0]],
        [col2[1], col1[1] + col2[1]],
        color=DARK_TEAL,
        lw=1.4,
        ls="-",
        zorder=4,
    )

    _arrow(
        ax,
        np.zeros(2),
        col1,
        DARK_TEAL,
        r"$(1,0)\mapsto(a,c)$",
        (0.05, 0.12),
    )
    _arrow(
        ax,
        np.zeros(2),
        col2,
        ACCENT,
        r"$(0,1)\mapsto(b,d)$",
        (0.05, -0.55),
    )

    ax.plot(0.0, 0.0, "o", color=DARK_TEAL, markersize=5, zorder=7)
    ax.annotate(
        "unit square\narea $=1$",
        xy=(0.5, 0.5),
        fontsize=9,
        color="0.40",
        ha="center",
        va="center",
    )
    ax.annotate(
        f"area $= ad-bc = {a:.0f}\\cdot{d:.0f}-{b:.0f}\\cdot{c:.0f} = {det:.0f}$",
        xy=(col1[0] + 0.38 * col2[0], col1[1] + 0.38 * col2[1]),
        fontsize=11,
        color=DARK_TEAL,
        ha="center",
        va="center",
        bbox={
            "boxstyle": "round,pad=0.35",
            "facecolor": "white",
            "edgecolor": "0.75",
            "alpha": 0.92,
        },
        zorder=8,
    )
    ax.annotate(
        f"box $(a+b)(c+d)={box_w:.0f}\\times{box_h:.0f}={box_w * box_h:.0f}$",
        xy=(box_w * 0.5, box_h + 0.22),
        fontsize=9.5,
        color="0.45",
        ha="center",
    )
    ax.annotate(
        "trimmed pieces",
        xy=(2.6, 2.45),
        fontsize=9,
        color=VIOLET,
        ha="center",
        alpha=0.9,
    )

    _style_ax(ax, (-0.4, box_w + 0.9), (-0.6, box_h + 0.9))

    out = OUT_DIR / "det_area_parallelogram.png"
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


def make_det_zero_collapsed() -> None:
    """Dependent columns: area 0 (parallelogram collapses to a line)."""
    col1 = np.array([2.0, 1.0])
    col2 = np.array([4.0, 2.0])  # col2 = 2 * col1

    fig, ax = plt.subplots(figsize=(6.8, 5.2), dpi=220)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)

    t = np.linspace(-0.5, 2.5, 2)
    ax.plot(
        t * col1[0],
        t * col1[1],
        color=DARK_TEAL,
        lw=2.8,
        zorder=3,
    )

    _arrow(ax, np.zeros(2), col1, DARK_TEAL, r"$\mathbf{a}_1$", (0.08, 0.12))
    _arrow(ax, np.zeros(2), col2, ACCENT, r"$\mathbf{a}_2=2\mathbf{a}_1$", (0.08, -0.45))

    ax.annotate(
        r"$\det(A)=ad-bc=0$ $\Rightarrow$ area $=0$",
        xy=(3.0, 1.5),
        fontsize=11,
        color=DARK_TEAL,
        ha="center",
        bbox={
            "boxstyle": "round,pad=0.35",
            "facecolor": "white",
            "edgecolor": "0.75",
            "alpha": 0.92,
        },
    )
    ax.annotate(
        "columns linearly dependent",
        xy=(3.0, 0.9),
        fontsize=10,
        color="0.40",
        ha="center",
    )

    _style_ax(ax, (-0.8, 5.5), (-0.5, 3.5))

    out = OUT_DIR / "det_zero_collapsed.png"
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
    make_det_area_parallelogram()
    make_det_zero_collapsed()
