"""Pointwise but not uniform convergence figure for Day 2 section 2.6."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"
OUT_DIR = Path(__file__).resolve().parent


def make_pointwise_not_uniform_plot() -> None:
    """f_n(x)=x^n on [0,1]: pointwise to 0 on [0,1), not uniform on [0,1]."""
    x = np.linspace(0.0, 0.995, 400)
    ns = [1, 2, 5, 15, 50]
    colors = ["#8aa0a4", "#6a8589", DARK_TEAL, "#c45a10", ACCENT]

    fig, ax = plt.subplots(figsize=(5.4, 3.8), dpi=220)
    for n, color in zip(ns, colors):
        ax.plot(x, x**n, color=color, linewidth=2.0, zorder=3)

    legend_x = 1.03
    legend_y = 0.88
    legend_dy = 0.11
    for i, (n, color) in enumerate(zip(ns, colors)):
        ax.text(
            legend_x,
            legend_y - i * legend_dy,
            rf"$n={n}$",
            color=color,
            fontsize=8,
            va="center",
            ha="left",
        )

    eps = 0.15
    ax.axhspan(0.0, eps, color=ACCENT, alpha=0.12, zorder=1)
    ax.axhline(eps, color=ACCENT, linestyle="--", linewidth=1.2, alpha=0.85, zorder=2)
    ax.text(0.04, eps + 0.02, r"$\varepsilon$", color=ACCENT, fontsize=9)

    ax.annotate(
        r"near $x=1$, need larger $n$",
        xy=(0.92, 0.92**15),
        xytext=(0.52, 0.72),
        fontsize=8.5,
        color=DARK_TEAL,
        arrowprops=dict(arrowstyle="->", color=DARK_TEAL, lw=1.1),
    )

    ax.set_xlim(0.0, 1.18)
    ax.set_ylim(-0.03, 1.05)
    ax.set_xlabel(r"$x$", fontsize=10)
    ax.set_ylabel(r"$f_n(x)=x^n$", fontsize=10)
    ax.set_title(
        r"Pointwise but not uniform on $[0,1]$",
        fontsize=10,
        color=DARK_TEAL,
        pad=8,
    )
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=8)

    out = OUT_DIR / "pointwise_not_uniform.png"
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    make_pointwise_not_uniform_plot()
