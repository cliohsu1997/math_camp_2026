"""Concave and convex functions with tangents — dual panel."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

DARK_TEAL = "#23373B"
TANGENT1 = "#E74C3C"
TANGENT2 = "#27AE60"
TANGENT3 = "#9B59B6"
OUT_DIR = Path(__file__).resolve().parent


def plot_concave(ax) -> None:
    x = np.linspace(-1.5, 2.5, 400)
    y = -0.8 * (x - 0.5) ** 2 + 2.0

    ax.plot(x, y, color=DARK_TEAL, lw=2.5, zorder=3)

    tangent_points = [-0.8, 0.5, 1.8]
    tangent_colors = [TANGENT1, TANGENT2, TANGENT3]

    for x0, color in zip(tangent_points, tangent_colors):
        y0 = -0.8 * (x0 - 0.5) ** 2 + 2.0
        slope = -1.6 * (x0 - 0.5)
        tangent = y0 + slope * (x - x0)

        ax.plot(x, tangent, color=color, lw=1.8, ls="--", alpha=0.8, zorder=2)
        ax.plot(x0, y0, "o", color=color, ms=6, zorder=4)

    ax.set_title("Concave", fontsize=11, fontweight="bold", color=DARK_TEAL, pad=6)
    style_axis(ax)


def plot_convex(ax) -> None:
    x = np.linspace(-1.5, 2.5, 400)
    y = 0.6 * (x - 0.8) ** 2 + 0.5

    ax.plot(x, y, color=DARK_TEAL, lw=2.5, zorder=3)

    tangent_points = [-0.5, 0.8, 2.0]
    tangent_colors = [TANGENT1, TANGENT2, TANGENT3]

    for x0, color in zip(tangent_points, tangent_colors):
        y0 = 0.6 * (x0 - 0.8) ** 2 + 0.5
        slope = 1.2 * (x0 - 0.8)
        tangent = y0 + slope * (x - x0)

        ax.plot(x, tangent, color=color, lw=1.8, ls="--", alpha=0.8, zorder=2)
        ax.plot(x0, y0, "o", color=color, ms=6, zorder=4)

    ax.set_title("Convex", fontsize=11, fontweight="bold", color=DARK_TEAL, pad=6)
    style_axis(ax)


def style_axis(ax) -> None:
    ax.set_xlim(-1.5, 2.5)
    ax.set_ylim(0, 3)
    ax.set_xlabel(r"$x$", fontsize=10)
    ax.set_ylabel(r"$f(x)$", fontsize=10)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=8)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(9.5, 3.6), dpi=220)

    plot_concave(axes[0])
    plot_convex(axes[1])

    out = OUT_DIR / "concave_tangents.png"
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white", pad_inches=0.08)
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
