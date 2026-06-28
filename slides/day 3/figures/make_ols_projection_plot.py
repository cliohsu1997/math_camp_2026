"""OLS projection schematic: age/educ axes, yellow plane = Col(X), e perp to columns."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"
BG = "#E8EEF0"
OUT_DIR = Path(__file__).resolve().parent

# Schematic (n=3): age column -> x-axis, educ column -> y-axis, Col(X) = xy-plane.
Y_HAT = np.array([2.35, 1.45, 0.0])
E_LEN = 1.55
Y = Y_HAT + np.array([0.0, 0.0, E_LEN])


def _segment_3d(
    ax: plt.Axes,
    start: np.ndarray,
    end: np.ndarray,
    color: str,
    lw: float = 2.4,
    ls: str = "-",
) -> None:
    ax.plot(
        [start[0], end[0]],
        [start[1], end[1]],
        [start[2], end[2]],
        color=color,
        lw=lw,
        ls=ls,
        zorder=4,
    )


def _right_angle_marker(
    ax: plt.Axes,
    corner: np.ndarray,
    dir_a: np.ndarray,
    dir_b: np.ndarray,
    size: float = 0.28,
) -> None:
    da = size * dir_a / np.linalg.norm(dir_a)
    db = size * dir_b / np.linalg.norm(dir_b)
    p1 = corner + da
    p2 = corner + da + db
    p3 = corner + db
    _segment_3d(ax, corner, p1, "0.45", lw=1.2)
    _segment_3d(ax, p1, p2, "0.45", lw=1.2)
    _segment_3d(ax, p2, p3, "0.45", lw=1.2)


def make_ols_projection_plot() -> None:
    fig = plt.figure(figsize=(8.0, 5.8), dpi=220)
    fig.patch.set_facecolor(BG)
    ax = fig.add_axes([0.24, 0.06, 0.74, 0.88], projection="3d")
    ax.set_facecolor(BG)

    s = np.linspace(-0.35, 3.0, 10)
    t = np.linspace(-0.35, 2.4, 10)
    ss, tt = np.meshgrid(s, t)
    ax.plot_surface(
        ss,
        tt,
        np.zeros_like(ss),
        color=ACCENT,
        alpha=0.20,
        edgecolor="none",
        shade=False,
        zorder=1,
    )

    origin = np.zeros(3)

    _segment_3d(ax, origin, Y_HAT, DARK_TEAL, lw=2.8)
    _segment_3d(ax, origin, Y, DARK_TEAL, lw=2.8)
    _segment_3d(ax, Y_HAT, Y, ACCENT, lw=2.4)
    _right_angle_marker(ax, Y_HAT, Y_HAT, np.array([0.0, 0.0, 1.0]))

    ax.text(Y[0] + 0.05, Y[1] + 0.05, Y[2] + 0.08, r"$\mathbf{y}$ (income)", color=DARK_TEAL, fontsize=11)
    ax.text(
        Y_HAT[0] * 0.55,
        Y_HAT[1] * 0.55,
        -0.22,
        r"$\widehat{\mathbf{y}}=X\widehat{\boldsymbol{\beta}}$",
        color=DARK_TEAL,
        fontsize=10,
    )
    ax.text(
        Y_HAT[0] + 0.12,
        Y_HAT[1] + 0.12,
        Y_HAT[2] + 0.55 * E_LEN,
        r"$\mathbf{e}=\mathbf{y}-\widehat{\mathbf{y}}$",
        color=ACCENT,
        fontsize=10,
    )
    ax.text(
        Y_HAT[0] + 0.35,
        Y_HAT[1] + 0.35,
        Y_HAT[2] + 0.72 * E_LEN,
        r"$\perp$ age, educ",
        color=ACCENT,
        fontsize=9,
    )

    ax.set_xlim(-0.3, 3.2)
    ax.set_ylim(-0.3, 2.6)
    ax.set_zlim(-0.35, 2.2)
    ax.set_xlabel("age", fontsize=11, labelpad=2)
    ax.set_ylabel("education", fontsize=11, labelpad=2)
    ax.set_zlabel("")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.view_init(elev=24, azim=-52)
    ax.grid(False)
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.pane.fill = False
        axis.pane.set_edgecolor("0.85")
        axis.line.set_color("0.55")

    fig.text(
        0.03,
        0.58,
        "Yellow plane\n=\nCol(X)",
        fontsize=12,
        color=ACCENT,
        ha="left",
        va="center",
        linespacing=1.4,
        weight="bold",
    )

    out = OUT_DIR / "ols_projection.png"
    fig.savefig(
        out,
        bbox_inches="tight",
        facecolor=BG,
        edgecolor="none",
        pad_inches=0.10,
    )
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    make_ols_projection_plot()
