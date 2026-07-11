"""Geometric Farkas for KKT: two-panel figure showing both cases."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"
CONE_ALPHA = 0.28
SEPARATOR_COLOR = "#2E8B57"  # Sea green for separating line
OUT_DIR = Path(__file__).resolve().parent


def _cone_wedge_acute(v1: np.ndarray, v2: np.ndarray, scale: float, n: int = 50) -> np.ndarray:
    """Wedge between two vectors with acute angle."""
    a1 = np.arctan2(v1[1], v1[0])
    a2 = np.arctan2(v2[1], v2[0])
    if abs(a2 - a1) > np.pi:
        if a2 > a1:
            a2 -= 2.0 * np.pi
        else:
            a1 -= 2.0 * np.pi
    angles = np.linspace(a1, a2, n)
    rays = np.column_stack([np.cos(angles), np.sin(angles)])
    boundary = rays * scale
    return np.vstack([np.zeros(2), boundary, np.zeros(2)])


def _arrow(ax, origin, vec, color, label, lw=2.4, label_offset=1.12, zorder=3) -> None:
    ax.annotate(
        "",
        xy=origin + vec,
        xytext=origin,
        arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, mutation_scale=12),
        zorder=zorder,
    )
    ax.text(
        origin[0] + vec[0] * label_offset,
        origin[1] + vec[1] * label_offset,
        label,
        fontsize=9,
        color=color,
        ha="center",
        va="center",
        fontweight="bold",
        zorder=zorder + 1,
    )


def _draw_panel(ax, title, case_type):
    """Draw one panel of the Farkas figure.
    
    case_type: "optimal" (grad_f inside cone) or "separated" (grad_f outside, hyperplane)
    """
    # Active constraint gradients forming acute cone
    g1 = np.array([1.0, 0.6])  # First constraint gradient
    g2 = np.array([0.3, 1.0])  # Second constraint gradient
    g1 = g1 / np.linalg.norm(g1) * 1.4
    g2 = g2 / np.linalg.norm(g2) * 1.4
    
    scale = 2.0
    wedge = _cone_wedge_acute(g1, g2, scale)
    
    # Draw cone fill
    ax.add_patch(
        Polygon(
            wedge,
            closed=True,
            facecolor=DARK_TEAL,
            edgecolor=DARK_TEAL,
            alpha=CONE_ALPHA,
            linewidth=1.2,
            zorder=1,
        )
    )
    
    # Cone boundary lines
    a1 = np.arctan2(g1[1], g1[0])
    a2 = np.arctan2(g2[1], g2[0])
    if abs(a2 - a1) > np.pi:
        if a2 > a1:
            a2 -= 2.0 * np.pi
        else:
            a1 -= 2.0 * np.pi
    
    t = np.linspace(0, 2.4, 100)
    ax.plot(t * np.cos(a1), t * np.sin(a1), '--', color=DARK_TEAL, lw=0.8, alpha=0.4, zorder=0)
    ax.plot(t * np.cos(a2), t * np.sin(a2), '--', color=DARK_TEAL, lw=0.8, alpha=0.4, zorder=0)
    
    origin = np.zeros(2)
    _arrow(ax, origin, g1, DARK_TEAL, r"$\nabla g_1$")
    _arrow(ax, origin, g2, DARK_TEAL, r"$\nabla g_2$")
    
    # Cone label
    mid_angle = (a1 + a2) / 2
    ax.text(0.9 * np.cos(mid_angle), 0.9 * np.sin(mid_angle), 
            r"$K$", fontsize=12, color=DARK_TEAL, ha="center", va="center", 
            fontweight="bold", alpha=0.8, zorder=2)
    
    # Mark origin as x*
    ax.plot(0, 0, "o", ms=6, color="black", zorder=5)
    ax.text(0.12, -0.16, r"$\mathbf{x}^*$", fontsize=10, color=DARK_TEAL, fontweight="bold", zorder=6)
    
    if case_type == "optimal":
        # -grad f inside the cone (optimal case)
        neg_grad_f = 0.5 * g1 + 0.5 * g2  # Inside cone
        _arrow(ax, origin, neg_grad_f, ACCENT, r"$-\nabla f$", lw=2.6, label_offset=1.12, zorder=4)
        
        # Label showing this is optimal
        ax.text(0.5, 1.8, r"$-\nabla f \in K$", fontsize=10, color=ACCENT, 
                ha="center", fontweight="bold", style='italic')
        ax.text(0.5, 1.5, r"(No improving direction)", fontsize=8, color="gray", ha="center")
        
    else:  # separated
        # -grad f outside the cone (not optimal)
        neg_grad_f = np.array([-0.8, 1.2])  # Outside cone, pointing elsewhere
        neg_grad_f = neg_grad_f / np.linalg.norm(neg_grad_f) * 1.3
        _arrow(ax, origin, neg_grad_f, ACCENT, r"$-\nabla f$", lw=2.6, label_offset=1.12, zorder=4)
        
        # Draw separating hyperplane (line perpendicular to direction that separates)
        # The hyperplane normal is such that cone is on one side, -grad_f on other
        normal = np.array([0.6, 0.8])  # Points toward -grad_f, away from cone
        normal = normal / np.linalg.norm(normal)
        
        # Draw the separating line through origin perpendicular to normal
        perp = np.array([-normal[1], normal[0]])
        line_pts = np.column_stack([perp * t_val for t_val in np.linspace(-2.5, 2.5, 100)])
        ax.plot(line_pts[0, :], line_pts[1, :], '-', color=SEPARATOR_COLOR, lw=2.0, alpha=0.8, zorder=3)
        
        # Arrow showing normal direction
        ax.annotate(
            "",
            xy=normal * 1.8,
            xytext=origin,
            arrowprops=dict(arrowstyle="-|>", color=SEPARATOR_COLOR, lw=1.8, mutation_scale=10, alpha=0.7),
            zorder=4,
        )
        ax.text(normal[0] * 2.0, normal[1] * 2.0, r"$\mathbf{d}$", fontsize=9, 
                color=SEPARATOR_COLOR, ha="center", va="center", fontweight="bold")
        
        # Label showing improvement possible
        ax.text(0.5, 1.8, r"$-\nabla f \notin K$", fontsize=10, color=ACCENT, 
                ha="center", fontweight="bold", style='italic')
        ax.text(0.5, 1.5, r"(Separating hyperplane exists)", fontsize=8, color=SEPARATOR_COLOR, ha="center")
        
        # Add text explaining d is improving direction
        ax.text(-1.5, 0.5, r"Feasible direction", fontsize=8, color=SEPARATOR_COLOR)
        ax.text(-1.5, 0.2, r"$\mathbf{d}$: $\nabla g_j \cdot \mathbf{d} \leq 0$", fontsize=7, color=SEPARATOR_COLOR)
        ax.text(-1.5, -0.1, r"$\nabla f \cdot \mathbf{d} > 0$", fontsize=7, color=ACCENT)
    
    ax.set_xlim(-1.8, 2.3)
    ax.set_ylim(-0.6, 2.2)
    ax.set_aspect("equal")
    ax.axhline(0, color="0.9", lw=0.5, zorder=0)
    ax.axvline(0, color="0.9", lw=0.5, zorder=0)
    ax.set_xlabel(r"$x_1$", fontsize=10, labelpad=2)
    ax.set_ylabel(r"$x_2$", fontsize=10, labelpad=2)
    ax.set_title(title, fontsize=10, color=DARK_TEAL, pad=10, fontweight="bold")
    
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("gray")
    ax.spines["bottom"].set_color("gray")
    ax.tick_params(labelsize=8, colors="gray")


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.8), dpi=220)
    
    _draw_panel(axes[0], "Case 1: $-\nabla f \in K$ (Optimal)", "optimal")
    _draw_panel(axes[1], "Case 2: $-\nabla f \notin K$ (Improvement Possible)", "separated")
    
    fig.suptitle(
        r"Geometric Farkas: Either $-\nabla f \in$ cone $K$, or a separating hyperplane exists",
        fontsize=11,
        color=DARK_TEAL,
        fontweight="bold",
        y=1.02,
    )
    
    out = OUT_DIR / "farkas_cone_2d.png"
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white", pad_inches=0.12)
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
