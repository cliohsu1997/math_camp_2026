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


def _boundary_point_toward(
    center: tuple[float, float] | np.ndarray,
    width: float,
    height: float,
    angle_deg: float,
    direction: np.ndarray,
) -> np.ndarray:
    """Boundary point of the ellipse farthest from center in `direction`."""
    xs, ys = _ellipse_points(center, width, height, angle_deg)
    center_arr = np.asarray(center, dtype=float)
    d = direction / np.linalg.norm(direction)
    scores = d[0] * (xs - center_arr[0]) + d[1] * (ys - center_arr[1])
    idx = int(np.argmax(scores))
    return np.array([xs[idx], ys[idx]])


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


def _proof_geometry() -> dict:
    center_a = np.array([0.82, 0.86])
    center_b = np.array([2.78, 2.42])
    width, height = 1.18, 0.82
    angle_a, angle_b = -22.0, 24.0

    toward_b = center_b - center_a
    toward_a = center_a - center_b
    a0 = _boundary_point_toward(center_a, width, height, angle_a, toward_b)
    b0 = _boundary_point_toward(center_b, width, height, angle_b, toward_a)

    p_vec = b0 - a0
    p_unit = p_vec / np.linalg.norm(p_vec)

    max_a, _ = _dot_range(tuple(center_a), width, height, angle_a, p_unit)
    _, min_b = _dot_range(tuple(center_b), width, height, angle_b, p_unit)
    gap = min_b - max_a
    if gap <= 0.03:
        raise RuntimeError("Ellipses overlap along separating direction.")

    beta = max_a + 0.45 * gap

    return {
        "center_a": center_a,
        "center_b": center_b,
        "width": width,
        "height": height,
        "angle_a": angle_a,
        "angle_b": angle_b,
        "p_unit": p_unit,
        "beta": beta,
        "a0": a0,
        "b0": b0,
        "p_vec": p_vec,
    }


def _draw_ellipses(ax: plt.Axes, geom: dict) -> None:
    center_a = tuple(geom["center_a"])
    center_b = tuple(geom["center_b"])
    width = geom["width"]
    height = geom["height"]
    angle_a = geom["angle_a"]
    angle_b = geom["angle_b"]

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


def _axis_style(ax: plt.Axes, title: str) -> None:
    ax.set_xlim(0.0, 3.6)
    ax.set_ylim(0.0, 3.1)
    ax.set_xlabel(r"good 1 ($x_1$)", fontsize=10)
    ax.set_ylabel(r"good 2 ($x_2$)", fontsize=10)
    ax.set_title(title, fontsize=10, color=DARK_TEAL, pad=10)
    ax.set_aspect("equal", adjustable="box")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=8)


def make_separation_plot() -> None:
    """A below a downward-sloping line; B above; p has positive components."""
    geom = _proof_geometry()
    p = geom["p_unit"]
    beta = geom["beta"]
    a0 = geom["a0"]
    b0 = geom["b0"]

    fig, ax = plt.subplots(figsize=(5.6, 4.2), dpi=220)
    _draw_ellipses(ax, geom)

    tangent = np.array([-p[1], p[0]])
    gap_mid = 0.5 * (a0 + b0)
    line_center = gap_mid - (np.dot(p, gap_mid) - beta) * p
    seg_half = 0.78
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

    _axis_style(ax, r"Disjoint convex sets separated by a line")

    out = OUT_DIR / "separation_hyperplane.png"
    fig.subplots_adjust(top=0.90, bottom=0.14, left=0.12, right=0.98)
    fig.savefig(out, bbox_inches="tight", facecolor="white", pad_inches=0.10)
    plt.close(fig)
    print(f"Wrote {out}")


def make_separation_proof_plot() -> None:
    """Proof idea: closest pair on boundaries, normal p=b0-a0, separating line."""
    geom = _proof_geometry()
    a0 = geom["a0"]
    b0 = geom["b0"]
    p_vec = geom["p_vec"]
    p_unit = p_vec / np.linalg.norm(p_vec)
    beta = geom["beta"]
    midpoint = 0.5 * (a0 + b0)

    fig, ax = plt.subplots(figsize=(5.6, 4.2), dpi=220)
    _draw_ellipses(ax, geom)

    ax.plot([a0[0], b0[0]], [a0[1], b0[1]], color=ACCENT, linewidth=2.4, zorder=5)
    ax.plot(a0[0], a0[1], "o", color=DARK_TEAL, markersize=8, zorder=6)
    ax.plot(b0[0], b0[1], "o", color=ACCENT, markersize=8, zorder=6)
    ax.text(a0[0] - 0.20, a0[1] - 0.14, r"$a_0$", fontsize=10, color=DARK_TEAL, zorder=7)
    ax.text(b0[0] + 0.08, b0[1] + 0.08, r"$b_0$", fontsize=10, color=ACCENT, zorder=7)

    ax.annotate(
        "",
        xy=b0,
        xytext=a0,
        arrowprops=dict(arrowstyle="->", color=ACCENT, lw=2.0),
        zorder=6,
    )
    ax.text(
        midpoint[0] - 0.42,
        midpoint[1] - 0.24,
        r"$\mathbf{p}=b_0-a_0$",
        fontsize=9,
        color=ACCENT,
        zorder=7,
    )
    ax.text(
        midpoint[0] + 0.10,
        midpoint[1] + 0.02,
        r"$\|b_0-a_0\|$",
        fontsize=8,
        color="0.35",
        zorder=7,
    )

    tangent = np.array([-p_unit[1], p_unit[0]])
    line_center = midpoint - (np.dot(p_unit, midpoint) - beta) * p_unit
    seg_half = 0.88
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
    ax.text(
        line_end[0] - 0.05,
        line_end[1] + 0.08,
        r"separating line",
        fontsize=8,
        color=DARK_TEAL,
        ha="right",
        zorder=7,
    )

    _axis_style(ax, r"Proof idea: closest pair, then a line $\perp\ \mathbf{p}$")

    out = OUT_DIR / "separation_proof_idea.png"
    fig.subplots_adjust(top=0.90, bottom=0.14, left=0.12, right=0.98)
    fig.savefig(out, bbox_inches="tight", facecolor="white", pad_inches=0.10)
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    make_separation_plot()
    make_separation_proof_plot()
