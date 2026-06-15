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
    n: int = 200,
) -> tuple[np.ndarray, np.ndarray]:
    t = np.linspace(0.0, 2.0 * np.pi, n)
    x_local = 0.5 * width * np.cos(t)
    y_local = 0.5 * height * np.sin(t)
    theta = np.deg2rad(angle_deg)
    rot = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    xy = rot @ np.vstack([x_local, y_local])
    return center[0] + xy[0], center[1] + xy[1]


def make_separation_plot() -> None:
    """Disjoint convex sets A, B and a separating line p·x = beta in R^2."""
    fig, ax = plt.subplots(figsize=(5.6, 4.0), dpi=220)

    center_a = (1.55, 2.35)
    center_b = (4.05, 1.35)
    ellipse_a = Ellipse(
        center_a,
        width=1.55,
        height=1.05,
        angle=28.0,
        facecolor=DARK_TEAL,
        edgecolor=DARK_TEAL,
        alpha=0.18,
        linewidth=2.0,
        zorder=2,
    )
    ellipse_b = Ellipse(
        center_b,
        width=1.45,
        height=0.95,
        angle=-18.0,
        facecolor=ACCENT,
        edgecolor=ACCENT,
        alpha=0.20,
        linewidth=2.0,
        zorder=2,
    )
    ax.add_patch(ellipse_a)
    ax.add_patch(ellipse_b)

    xa, ya = _ellipse_points(center_a, 1.55, 1.05, 28.0)
    xb, yb = _ellipse_points(center_b, 1.45, 0.95, -18.0)
    ax.plot(xa, ya, color=DARK_TEAL, linewidth=2.2, zorder=3)
    ax.plot(xb, yb, color=ACCENT, linewidth=2.2, zorder=3)

    # Separating line: p = (0.55, 0.85), beta = 2.35
    p1, p2, beta = 0.55, 0.85, 2.35
    x_line = np.linspace(0.2, 5.0, 2)
    y_line = (beta - p1 * x_line) / p2
    ax.plot(x_line, y_line, color=DARK_TEAL, linewidth=2.0, linestyle="--", zorder=4)

    arrow_start = np.array([2.55, 0.55])
    p_vec = np.array([p1, p2])
    p_vec = 0.55 * p_vec / np.linalg.norm(p_vec)
    ax.annotate(
        "",
        xy=arrow_start + p_vec,
        xytext=arrow_start,
        arrowprops=dict(arrowstyle="->", color=ACCENT, lw=1.8),
        zorder=5,
    )
    ax.text(arrow_start[0] + p_vec[0] + 0.08, arrow_start[1] + p_vec[1] + 0.05, r"$p$", color=ACCENT, fontsize=10)

    ax.text(center_a[0], center_a[1], r"$A$", fontsize=12, color=DARK_TEAL, ha="center", va="center", fontweight="bold")
    ax.text(center_b[0], center_b[1], r"$B$", fontsize=12, color=ACCENT, ha="center", va="center", fontweight="bold")

    ax.text(0.55, 3.35, r"$p \cdot x = \beta$", fontsize=9, color=DARK_TEAL)
    ax.text(0.55, 3.12, r"$p \cdot a \leq \beta$ for $a \in A$", fontsize=8, color=DARK_TEAL)
    ax.text(3.05, 0.42, r"$p \cdot b \geq \beta$ for $b \in B$", fontsize=8, color=ACCENT)

    ax.set_xlim(0.0, 5.2)
    ax.set_ylim(0.0, 3.6)
    ax.set_xlabel(r"good 1 ($x_1$)", fontsize=10)
    ax.set_ylabel(r"good 2 ($x_2$)", fontsize=10)
    ax.set_title(r"Disjoint convex sets separated by a line", fontsize=10, color=DARK_TEAL, pad=8)
    ax.set_aspect("equal", adjustable="box")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=8)

    out = OUT_DIR / "separation_hyperplane.png"
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    make_separation_plot()
