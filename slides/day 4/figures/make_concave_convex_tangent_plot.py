"""Concave and convex functions with multiple tangent lines - no text."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

DARK_TEAL = "#23373B"
TANGENT1 = "#E74C3C"  # Red
TANGENT2 = "#27AE60"  # Green
TANGENT3 = "#9B59B6"  # Purple
OUT_DIR = Path(__file__).resolve().parent


def plot_concave(ax):
    """Plot concave function with multiple tangents above curve."""
    x = np.linspace(-1.5, 2.5, 400)
    
    # Smooth concave function
    y = -0.8 * (x - 0.5)**2 + 2.0
    
    ax.plot(x, y, color=DARK_TEAL, lw=2.5, zorder=3)
    
    # Multiple tangent points with different colors
    tangent_points = [-0.8, 0.5, 1.8]
    tangent_colors = [TANGENT1, TANGENT2, TANGENT3]
    
    for x0, color in zip(tangent_points, tangent_colors):
        y0 = -0.8 * (x0 - 0.5)**2 + 2.0
        slope = -1.6 * (x0 - 0.5)
        tangent = y0 + slope * (x - x0)
        
        ax.plot(x, tangent, color=color, lw=1.8, ls="--", alpha=0.8, zorder=2)
        ax.plot(x0, y0, "o", color=color, ms=7, zorder=4)
    
    ax.set_xlim(-1.5, 2.5)
    ax.set_ylim(0, 3)
    ax.set_xlabel(r"$x$", fontsize=11)
    ax.set_ylabel(r"$f(x)$", fontsize=11)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=9)


def plot_convex(ax):
    """Plot convex function with multiple tangents below curve."""
    x = np.linspace(-1.5, 2.5, 400)
    
    # Smooth convex function
    y = 0.6 * (x - 0.8)**2 + 0.5
    
    ax.plot(x, y, color=DARK_TEAL, lw=2.5, zorder=3)
    
    # Multiple tangent points
    tangent_points = [-0.5, 0.8, 2.0]
    tangent_colors = [TANGENT1, TANGENT2, TANGENT3]
    
    for x0, color in zip(tangent_points, tangent_colors):
        y0 = 0.6 * (x0 - 0.8)**2 + 0.5
        slope = 1.2 * (x0 - 0.8)
        tangent = y0 + slope * (x - x0)
        
        ax.plot(x, tangent, color=color, lw=1.8, ls="--", alpha=0.8, zorder=2)
        ax.plot(x0, y0, "o", color=color, ms=7, zorder=4)
    
    ax.set_xlim(-1.5, 2.5)
    ax.set_ylim(0, 3)
    ax.set_xlabel(r"$x$", fontsize=11)
    ax.set_ylabel(r"$f(x)$", fontsize=11)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=9)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5), dpi=220)
    
    plot_concave(axes[0])
    plot_convex(axes[1])
    
    out = OUT_DIR / "concave_convex_tangents.png"
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white", pad_inches=0.1)
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
