"""Separating hyperplane figure for Day 3 section 3.2."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"
OUT_DIR = Path(__file__).resolve().parent


def _ellipse_points(
    center: tuple[float, float],
    width: float,
    height: float,
    angle_deg: float,
    n: int = 360,
) -> tuple[np.ndarray, np.ndarray]:
    t = np.linspace(0.0, 2.0 * np.pi, n)
    x_local = 0.5 * width * np.cos(t)
    y_local = 0.5 * height * np.sin(t)
    theta = np.deg2rad(angle_deg)
    rot = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    xy = rot @ np.vstack([x_local, y_local])
    return center[0] + xy[0], center[1] + xy[1]


def _dot_range(
    center: tuple[float, float],
    width: float,
    height: float,
    angle_deg: float,
    p: np.ndarray,
) -> tuple[float, float]:
    xs, ys = _ellipse_points(center, width, height, angle_deg)
    dots = p[0] * xs + p[1] * ys
    return float(dots.min()), float(dots.max())


def make_separation_plot() -> None:
    """A below a downward-sloping line; B above; p has positive components."""
    # A lower-left, B upper-right so positive p separates with a downward-sloping line.
    center_a = (0.95, 0.92)
    center_b = (2.55, 2.18)
    width, height = 0.50, 0.36
    angle_a, angle_b = -22.0, 24.0

    p = np.array([0.72, 0.69])
    p = p / np.linalg.norm(p)

    max_a, _ = _dot_range(center_a, width, height, angle_a, p)
    _, min_b = _dot_range(center_b, width, height, angle_b, p)
    gap = min_b - max_a
    if gap <= 0.05:
        raise RuntimeError("Ellipses overlap along separating direction.")

    beta = max_a + 0.45 * gap

    fig, ax = plt.subplots(figsize=(5.6, 4.2), dpi=220)

    ellipse_a = Ellipse(
        center_a,
        width=width,
        height=height,
        angle=angle_a,
        facecolor=DARK_TEAL,
        edgecolor=DARK_TEAL,
        alpha=0.18,
        linewidth=2.0,
        zorder=2,
    )
    ellipse_b = Ellipse(
        center_b,
        width=width,
        height=height,
        angle=angle_b,
        facecolor=ACCENT,
        edgecolor=ACCENT,
        alpha=0.20,
        linewidth=2.0,
        zorder=2,
    )
    ax.add_patch(ellipse_a)
    ax.add_patch(ellipse_b)

    xa, ya = _ellipse_points(center_a, width, height, angle_a)
    xb, yb = _ellipse_points(center_b, width, height, angle_b)
    ax.plot(xa, ya, color=DARK_TEAL, linewidth=2.2, zorder=3)
    ax.plot(xb, yb, color=ACCENT, linewidth=2.2, zorder=3)

    tangent = np.array([-p[1], p[0]])
    gap_mid = 0.5 * (np.array(center_a) + np.array(center_b))
    line_center = gap_mid - (np.dot(p, gap_mid) - beta) * p
    seg_half = 0.62
    line_start = line_center - seg_half * tangent
    line_end = line_center + seg_half * tangent
    ax.plot(
        [line_start[0], line_end[0]],
        [line_start[1], line_end[1]],
        color=DARK_TEAL,
        linewidth=2.0,
        linestyle="--",
        zorder=4,
    )

    arrow_len = 0.34
    ax.annotate(
        "",
        xy=line_center + arrow_len * p,
        xytext=line_center,
        arrowprops=dict(arrowstyle="->", color=ACCENT, lw=1.8),
        zorder=5,
    )
    ax.text(
        line_center[0] + arrow_len * p[0] + 0.06,
        line_center[1] + arrow_len * p[1] + 0.04,
        r"$\mathbf{p}$",
        color=ACCENT,
        fontsize=10,
        zorder=6,
    )

    ax.text(
        center_a[0],
        center_a[1],
        r"$A$",
        fontsize=12,
        color=DARK_TEAL,
        ha="center",
        va="center",
        fontweight="bold",
        zorder=6,
    )
    ax.text(
        center_b[0],
        center_b[1],
        r"$B$",
        fontsize=12,
        color=ACCENT,
        ha="center",
        va="center",
        fontweight="bold",
        zorder=6,
    )

    ax.set_xlim(0.0, 3.4)
    ax.set_ylim(0.0, 2.9)
    ax.set_xlabel(r"good 1 ($x_1$)", fontsize=10)
    ax.set_ylabel(r"good 2 ($x_2$)", fontsize=10)
    ax.set_title(
        r"Disjoint convex sets separated by a line",
        fontsize=10,
        color=DARK_TEAL,
        pad=10,
    )
    ax.set_aspect("equal", adjustable="box")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=8)

    out = OUT_DIR / "separation_hyperplane.png"
    fig.subplots_adjust(top=0.90, bottom=0.14, left=0.12, right=0.98)
    fig.savefig(out, bbox_inches="tight", facecolor="white", pad_inches=0.10)
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    make_separation_plot()
