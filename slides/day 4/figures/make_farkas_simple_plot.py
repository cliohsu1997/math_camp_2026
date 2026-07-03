"""Farkas Lemma: cone and vector on OPPOSITE sides of separating hyperplane. NO TEXT."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"
SEPARATOR = "#E74C3C"
FEASIBLE = "#27AE60"
CONE_ALPHA = 0.25
OUT_DIR = Path(__file__).resolve().parent


def _cone_polygon(g1, g2, scale):
    """Return polygon points for cone between g1 and g2."""
    angles = np.linspace(np.arctan2(g1[1], g1[0]), np.arctan2(g2[1], g2[0]), 40)
    pts = [[0, 0]]
    for a in angles:
        pts.append([scale * np.cos(a), scale * np.sin(a)])
    pts.append([0, 0])
    return np.array(pts)


def draw_optimal(ax):
    """Left panel: vector inside cone (optimal)."""
    # Cone in first quadrant
    g1 = np.array([1.3, 0.2])
    g2 = np.array([0.2, 1.3])
    
    # Draw cone fill
    cone = _cone_polygon(g1, g2, 2.0)
    ax.add_patch(Polygon(cone, closed=True, facecolor=DARK_TEAL, 
                        edgecolor=DARK_TEAL, alpha=CONE_ALPHA, lw=1.5))
    
    # Draw constraint gradient arrows
    ax.annotate("", xy=g1, xytext=[0,0], 
                arrowprops=dict(arrowstyle="-|>", color=DARK_TEAL, lw=2.5),
                zorder=5)
    ax.text(g1[0]*1.3, g1[1]*1.3, r"$\nabla g_1$", fontsize=11, 
            color=DARK_TEAL, ha="center", fontweight="bold")
    
    ax.annotate("", xy=g2, xytext=[0,0], 
                arrowprops=dict(arrowstyle="-|>", color=DARK_TEAL, lw=2.5),
                zorder=5)
    ax.text(g2[0]*1.3, g2[1]*1.3, r"$\nabla g_2$", fontsize=11, 
            color=DARK_TEAL, ha="center", fontweight="bold")
    
    # -grad f inside cone
    ngf = 0.6*g1 + 0.4*g2
    ax.annotate("", xy=ngf, xytext=[0,0], 
                arrowprops=dict(arrowstyle="-|>", color=ACCENT, lw=3),
                zorder=6)
    ax.text(ngf[0]*1.3, ngf[1]*1.3, r"$-\nabla f$", fontsize=12, 
            color=ACCENT, ha="center", fontweight="bold")
    
    # Mark origin
    ax.plot(0, 0, "ko", ms=6, zorder=7)
    
    # Cone label
    ax.text(1.0, 0.8, r"$K$", fontsize=14, color=DARK_TEAL, 
            ha="center", fontweight="bold", alpha=0.9)
    
    ax.set_xlim(-0.5, 2.2)
    ax.set_ylim(-0.5, 2.2)
    ax.set_aspect("equal")
    ax.axis("off")


def draw_not_optimal(ax):
    """Right panel: vector outside cone with separating hyperplane."""
    # Cone in first quadrant
    g1 = np.array([1.3, 0.2])
    g2 = np.array([0.2, 1.3])
    
    # Draw cone fill
    cone = _cone_polygon(g1, g2, 2.0)
    ax.add_patch(Polygon(cone, closed=True, facecolor=DARK_TEAL, 
                        edgecolor=DARK_TEAL, alpha=CONE_ALPHA, lw=1.5))
    
    # Draw constraint gradient arrows
    ax.annotate("", xy=g1, xytext=[0,0], 
                arrowprops=dict(arrowstyle="-|>", color=DARK_TEAL, lw=2.5),
                zorder=5)
    ax.text(g1[0]*1.3, g1[1]*1.3, r"$\nabla g_1$", fontsize=11, 
            color=DARK_TEAL, ha="center", fontweight="bold")
    
    ax.annotate("", xy=g2, xytext=[0,0], 
                arrowprops=dict(arrowstyle="-|>", color=DARK_TEAL, lw=2.5),
                zorder=5)
    ax.text(g2[0]*1.3, g2[1]*1.3, r"$\nabla g_2$", fontsize=11, 
            color=DARK_TEAL, ha="center", fontweight="bold")
    
    # -grad f OUTSIDE cone - pointing to upper left (opposite side from cone)
    ngf = np.array([-1.2, 1.0])
    ngf = ngf / np.linalg.norm(ngf) * 1.5
    ax.annotate("", xy=ngf, xytext=[0,0], 
                arrowprops=dict(arrowstyle="-|>", color=ACCENT, lw=3),
                zorder=6)
    ax.text(ngf[0]*1.2, ngf[1]*1.2, r"$-\nabla f$", fontsize=12, 
            color=ACCENT, ha="center", fontweight="bold")
    
    # Separating hyperplane - line through origin with steep negative slope
    # This separates first quadrant (cone) from second quadrant (-grad f)
    # Line: y = -2x ensures cone is on one side, -grad f on other
    sep_x = np.linspace(-1.5, 1.5, 100)
    sep_y = -2 * sep_x
    ax.plot(sep_x, sep_y, '--', color=SEPARATOR, lw=3, zorder=4)
    
    # Feasible direction d - in cone
    d = np.array([1.0, 0.8])
    d = d / np.linalg.norm(d) * 1.0
    ax.annotate("", xy=d, xytext=[0,0], 
                arrowprops=dict(arrowstyle="-|>", color=FEASIBLE, lw=2.5),
                zorder=5)
    ax.text(d[0]*1.5, d[1]*1.5, r"$\mathbf{d}$", fontsize=11, 
            color=FEASIBLE, ha="center", fontweight="bold")
    
    # Mark origin
    ax.plot(0, 0, "ko", ms=6, zorder=7)
    
    # Cone label
    ax.text(1.0, 0.8, r"$K$", fontsize=14, color=DARK_TEAL, 
            ha="center", fontweight="bold", alpha=0.9)
    
    ax.set_xlim(-1.8, 2.2)
    ax.set_ylim(-0.5, 2.2)
    ax.set_aspect("equal")
    ax.axis("off")


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.5), dpi=220)
    
    draw_optimal(axes[0])
    draw_not_optimal(axes[1])
    
    out = OUT_DIR / "farkas_simple.png"
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white", pad_inches=0.15)
    plt.close()
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
