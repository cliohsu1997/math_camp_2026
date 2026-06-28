"""PPS + isoprofit on one plot (1 input, 1 output, netput coordinates)."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"
FILL_ALPHA = 0.12
OUT_DIR = Path(__file__).resolve().parent

# Numerical example (matches slides).
P1 = 1.0
P2 = 2.0
LABOR_STAR = 4.0


def production_output(labor: np.ndarray) -> np.ndarray:
    """y2 = f(L) with f(L) = 2 sqrt(L)."""
    return 2.0 * np.sqrt(np.clip(labor, 0.0, None))


def make_pps_combined_plot() -> None:
    labor_max = 6.5
    labor = np.linspace(0.0, labor_max, 400)
    y1 = -labor
    y2_frontier = production_output(labor)

    y1_star = -LABOR_STAR
    y2_star = float(production_output(np.array([LABOR_STAR]))[0])
    profit = P1 * y1_star + P2 * y2_star
    y_intercept = profit / P2

    fig, ax = plt.subplots(figsize=(7.2, 5.4), dpi=220)

    # PPS: 0 <= y2 <= f(-y1), y1 <= 0.
    verts = np.column_stack([y1, y2_frontier])
    lower = np.column_stack([y1[::-1], np.zeros_like(y1)])
    region = np.vstack([verts, lower])
    ax.add_patch(
        Polygon(
            region,
            closed=True,
            facecolor=DARK_TEAL,
            edgecolor="none",
            alpha=FILL_ALPHA,
            zorder=1,
        )
    )

    ax.plot(
        y1,
        y2_frontier,
        color=DARK_TEAL,
        linewidth=2.8,
        zorder=3,
        label="frontier y2 = 2 sqrt(-y1)",
    )

    # Isoprofit line through y*.
    y1_line = np.linspace(-7.5, 1.2, 200)
    y2_line = (profit - P1 * y1_line) / P2
    ax.plot(
        y1_line,
        y2_line,
        color=ACCENT,
        linewidth=2.4,
        linestyle="--",
        zorder=4,
        label=f"isoprofit {P1:.0f}y1 + {P2:.0f}y2 = {profit:.0f}",
    )

    ax.axhline(0.0, color="0.4", linewidth=1.0, zorder=2)
    ax.axvline(0.0, color="0.4", linewidth=1.0, zorder=2)

    marker_kw = {
        "color": ACCENT,
        "markersize": 10,
        "zorder": 6,
        "markeredgecolor": "white",
        "markeredgewidth": 2.0,
    }
    ax.plot(y1_star, y2_star, "o", **marker_kw)
    ax.plot(0.0, y_intercept, "o", **marker_kw)

    ax.annotate(
        "y* = (-4, 4)",
        xy=(y1_star, y2_star),
        xytext=(-1.4, 5.35),
        fontsize=11,
        color=ACCENT,
        ha="left",
        va="bottom",
        arrowprops={
            "arrowstyle": "->",
            "color": ACCENT,
            "lw": 1.2,
            "shrinkA": 6,
            "shrinkB": 6,
            "connectionstyle": "arc3,rad=0.12",
        },
    )
    ax.annotate(
        "pi/p2 = 2",
        xy=(0.0, y_intercept),
        xytext=(1.05, 3.55),
        fontsize=11,
        color=ACCENT,
        ha="left",
        va="center",
        arrowprops={
            "arrowstyle": "->",
            "color": ACCENT,
            "lw": 1.2,
            "shrinkA": 6,
            "shrinkB": 6,
            "connectionstyle": "arc3,rad=-0.15",
        },
    )
    ax.annotate(
        "PPS",
        xy=(-4.8, 1.0),
        fontsize=11,
        color=DARK_TEAL,
        ha="center",
        va="center",
    )

    ax.set_xlim(-7.8, 1.6)
    ax.set_ylim(-0.5, 6.0)
    ax.set_xlabel("input", fontsize=13)
    ax.set_ylabel("output", fontsize=13)
    ax.set_title(
        "Production frontier and supporting isoprofit line",
        fontsize=13,
        color=DARK_TEAL,
        pad=12,
    )
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(True, alpha=0.2, linewidth=0.6)
    ax.legend(loc="upper left", bbox_to_anchor=(0.02, 0.98), frameon=False, fontsize=10)

    out = OUT_DIR / "pps_frontier_isoprofit.png"
    fig.subplots_adjust(left=0.10, right=0.97, bottom=0.12, top=0.90)
    fig.savefig(out, bbox_inches="tight", facecolor="white", pad_inches=0.15)
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    make_pps_combined_plot()
