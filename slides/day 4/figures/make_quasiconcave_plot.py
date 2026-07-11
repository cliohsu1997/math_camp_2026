"""Contour plot: convex upper contour sets for log(x+1)+log(y+1)."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"
OUT_DIR = Path(__file__).resolve().parent


def main() -> None:
    x = np.linspace(0.05, 4.5, 200)
    y = np.linspace(0.05, 4.5, 200)
    X, Y = np.meshgrid(x, y)
    Z = np.log(X + 1.0) + np.log(Y + 1.0)

    levels = np.linspace(0.4, 2.2, 7)

    fig, ax = plt.subplots(figsize=(5.4, 4.6), dpi=220)
    contours = ax.contour(
        X,
        Y,
        Z,
        levels=levels,
        colors=DARK_TEAL,
        linewidths=1.4,
    )
    ax.clabel(contours, inline=True, fontsize=7, fmt="%.1f")

    # Shade one upper contour set {f >= c}
    c_highlight = 1.4
    ax.contourf(
        X,
        Y,
        Z,
        levels=[c_highlight, Z.max()],
        colors=[ACCENT],
        alpha=0.22,
    )
    ax.contour(
        X,
        Y,
        Z,
        levels=[c_highlight],
        colors=[ACCENT],
        linewidths=2.6,
    )

    ax.annotate(
        r"$\{f\geq c\}$ convex",
        xy=(2.8, 1.1),
        fontsize=10,
        color=ACCENT,
    )
    ax.set_xlabel(r"$x$", fontsize=10)
    ax.set_ylabel(r"$y$", fontsize=10)
    ax.set_title(
        r"$f(x,y)=\ln(x+1)+\ln(y+1)$ --- quasiconcave",
        fontsize=11,
        color=DARK_TEAL,
        pad=8,
    )
    ax.set_aspect("equal", adjustable="box")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=8)

    out = OUT_DIR / "quasiconcave_contours.png"
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
