"""Linear transformation figures: shear and rotation (before/after panels)."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

from matplotlib.ticker import MultipleLocator

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"
MUTED = "#6B8E95"
BG = "#E8EEF0"
OUT_DIR = Path(__file__).resolve().parent

E1 = np.array([1.0, 0.0])
E2 = np.array([0.0, 1.0])
UNIT_CORNER = E1 + E2

SHEAR = np.array([[1.0, 1.0], [0.0, 1.0]])
ROTATION = np.array([[0.0, 1.0], [-1.0, 0.0]])  # 90° clockwise

V1 = 2.0
V2 = 3.0
V = V1 * E1 + V2 * E2


def _style_axes(
    ax: plt.Axes,
    xlim: tuple[float, float],
    ylim: tuple[float, float],
    *,
    tick_step: float,
) -> None:
    ax.set_facecolor(BG)
    ax.axhline(0.0, color="0.35", lw=0.9, zorder=1)
    ax.axvline(0.0, color="0.35", lw=0.9, zorder=1)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="box")
    ax.xaxis.set_major_locator(MultipleLocator(tick_step))
    ax.yaxis.set_major_locator(MultipleLocator(tick_step))
    ax.set_xlabel(r"$x_1$", fontsize=10)
    ax.set_ylabel(r"$x_2$", fontsize=10)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.grid(False)


def _align_paired_axes(
    axes: np.ndarray,
    xlim: tuple[float, float],
    ylim: tuple[float, float],
    *,
    tick_step: float,
) -> None:
    for ax in axes:
        _style_axes(ax, xlim, ylim, tick_step=tick_step)


def _arrow(
    ax: plt.Axes,
    start: np.ndarray,
    vec: np.ndarray,
    color: str,
    label: str,
    label_xy: tuple[float, float],
    *,
    lw: float = 2.2,
    zorder: int = 4,
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
        zorder=zorder,
    )
    ax.annotate(
        label,
        xy=label_xy,
        fontsize=10,
        color=color,
        ha="left",
        va="center",
        zorder=zorder + 1,
    )


def _draw_unit_square(ax: plt.Axes, *, facecolor: str, edgecolor: str, alpha: float) -> None:
    square = np.array([[0.0, 0.0], E1, UNIT_CORNER, E2])
    ax.add_patch(
        Polygon(
            square,
            closed=True,
            facecolor=facecolor,
            edgecolor=edgecolor,
            lw=1.1,
            alpha=alpha,
            zorder=2,
        )
    )


def _draw_polygon(
    ax: plt.Axes,
    corners: np.ndarray,
    *,
    facecolor: str,
    edgecolor: str,
    alpha: float,
) -> None:
    ax.add_patch(
        Polygon(
            corners,
            closed=True,
            facecolor=facecolor,
            edgecolor=edgecolor,
            lw=1.1,
            alpha=alpha,
            zorder=2,
        )
    )


def make_shear_plot() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(8.8, 4.2), dpi=220, sharex=True, sharey=True)
    fig.patch.set_facecolor(BG)

    ax_before, ax_after = axes
    _align_paired_axes(
        axes,
        xlim=(-0.35, 2.35),
        ylim=(-0.35, 1.35),
        tick_step=0.5,
    )

    ax_before.set_title("Before", fontsize=11, color=DARK_TEAL, pad=6)
    ax_after.set_title(r"After $T(\mathbf{x})=(x_1+x_2,x_2)$", fontsize=11, color=DARK_TEAL, pad=6)

    _draw_unit_square(ax_before, facecolor=MUTED, edgecolor=DARK_TEAL, alpha=0.22)
    _arrow(ax_before, np.zeros(2), E1, DARK_TEAL, r"$\mathbf{e}_1$", (1.05, -0.18), lw=2.0)
    _arrow(ax_before, np.zeros(2), E2, DARK_TEAL, r"$\mathbf{e}_2$", (-0.55, 1.05), lw=2.0)

    sheared = np.array(
        [[0.0, 0.0], SHEAR @ E1, SHEAR @ UNIT_CORNER, SHEAR @ E2]
    )
    _draw_polygon(ax_after, sheared, facecolor=ACCENT, edgecolor=ACCENT, alpha=0.20)
    te1 = SHEAR @ E1
    te2 = SHEAR @ E2
    _arrow(ax_after, np.zeros(2), te1, ACCENT, r"$T(\mathbf{e}_1)$", (1.05, -0.18), lw=2.2)
    _arrow(ax_after, np.zeros(2), te2, ACCENT, r"$T(\mathbf{e}_2)$", (0.55, 1.08), lw=2.2)

    for ax in axes:
        ax.plot(0.0, 0.0, "o", color=DARK_TEAL, markersize=4, zorder=5)

    out = OUT_DIR / "shear_horizontal.png"
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.16, top=0.88, wspace=0.28)
    fig.savefig(out, bbox_inches="tight", facecolor=BG, edgecolor="none", pad_inches=0.08)
    plt.close(fig)
    print(f"Wrote {out}")


def make_shear_decompose_plot() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.4), dpi=220, sharex=True, sharey=True)
    fig.patch.set_facecolor(BG)

    piece1 = V1 * E1
    piece2 = V2 * E2
    tpiece1 = SHEAR @ piece1
    tpiece2 = SHEAR @ piece2
    tv = SHEAR @ V

    ax_in, ax_out = axes
    _align_paired_axes(
        axes,
        xlim=(-0.5, 6.0),
        ylim=(-0.5, 3.5),
        tick_step=1.0,
    )

    ax_in.set_title(r"Decompose $\mathbf{v}=2\mathbf{e}_1+3\mathbf{e}_2$", fontsize=11, color=DARK_TEAL, pad=6)
    ax_out.set_title(r"Transform pieces, then combine", fontsize=11, color=DARK_TEAL, pad=6)

    para_in = np.array([[0.0, 0.0], piece1, V, piece2])
    _draw_polygon(ax_in, para_in, facecolor=MUTED, edgecolor=DARK_TEAL, alpha=0.20)
    _arrow(ax_in, np.zeros(2), piece1, DARK_TEAL, r"$2\mathbf{e}_1$", (2.05, -0.35), lw=2.0)
    _arrow(ax_in, np.zeros(2), piece2, DARK_TEAL, r"$3\mathbf{e}_2$", (-1.05, 3.05), lw=2.0)
    _arrow(ax_in, np.zeros(2), V, MUTED, r"$\mathbf{v}$", (2.05, 3.05), lw=2.2)

    para_out = np.array([[0.0, 0.0], tpiece1, tv, tpiece2])
    _draw_polygon(ax_out, para_out, facecolor=ACCENT, edgecolor=ACCENT, alpha=0.18)
    _arrow(ax_out, np.zeros(2), tpiece1, ACCENT, r"$2T(\mathbf{e}_1)$", (2.05, -0.35), lw=2.0)
    _arrow(ax_out, np.zeros(2), tpiece2, ACCENT, r"$3T(\mathbf{e}_2)$", (2.05, 3.05), lw=2.0)
    _arrow(ax_out, np.zeros(2), tv, ACCENT, r"$T(\mathbf{v})$", (5.05, 3.05), lw=2.2)

    for ax in axes:
        ax.plot(0.0, 0.0, "o", color=DARK_TEAL, markersize=4, zorder=5)

    out = OUT_DIR / "shear_decompose.png"
    fig.subplots_adjust(left=0.06, right=0.98, bottom=0.16, top=0.88, wspace=0.30)
    fig.savefig(out, bbox_inches="tight", facecolor=BG, edgecolor="none", pad_inches=0.08)
    plt.close(fig)
    print(f"Wrote {out}")


def make_rotation_plot() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(8.8, 4.2), dpi=220, sharex=True, sharey=True)
    fig.patch.set_facecolor(BG)

    ax_before, ax_after = axes
    _align_paired_axes(
        axes,
        xlim=(-1.35, 1.35),
        ylim=(-1.35, 1.35),
        tick_step=0.5,
    )

    ax_before.set_title("Before", fontsize=11, color=DARK_TEAL, pad=6)
    ax_after.set_title(r"After $90^\circ$ clockwise", fontsize=11, color=DARK_TEAL, pad=6)

    _draw_unit_square(ax_before, facecolor=MUTED, edgecolor=DARK_TEAL, alpha=0.22)
    _arrow(ax_before, np.zeros(2), E1, DARK_TEAL, r"$\mathbf{e}_1$", (1.05, -0.18), lw=2.0)
    _arrow(ax_before, np.zeros(2), E2, DARK_TEAL, r"$\mathbf{e}_2$", (-0.55, 1.05), lw=2.0)

    rotated = np.array(
        [[0.0, 0.0], ROTATION @ E1, ROTATION @ UNIT_CORNER, ROTATION @ E2]
    )
    _draw_polygon(ax_after, rotated, facecolor=ACCENT, edgecolor=ACCENT, alpha=0.20)
    te1 = ROTATION @ E1
    te2 = ROTATION @ E2
    _arrow(ax_after, np.zeros(2), te1, ACCENT, r"$T(\mathbf{e}_1)$", (0.12, -1.05), lw=2.2)
    _arrow(ax_after, np.zeros(2), te2, ACCENT, r"$T(\mathbf{e}_2)$", (1.05, 0.05), lw=2.2)

    for ax in axes:
        ax.plot(0.0, 0.0, "o", color=DARK_TEAL, markersize=4, zorder=5)

    out = OUT_DIR / "rotation_clockwise.png"
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.16, top=0.88, wspace=0.28)
    fig.savefig(out, bbox_inches="tight", facecolor=BG, edgecolor="none", pad_inches=0.08)
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    make_shear_plot()
    make_shear_decompose_plot()
    make_rotation_plot()
