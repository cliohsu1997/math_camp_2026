"""f(x)=x^3: f'=0 and f''<=0 but not a local max."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"
OUT_DIR = Path(__file__).resolve().parent


def f(x):
    return x**3


def main():
    fig, ax = plt.subplots(
        figsize=(7.6, 4.2),
        dpi=220,
    )

    grid = np.linspace(-1.35, 1.35, 400)
    ax.plot(
        grid,
        f(grid),
        color=DARK_TEAL,
        lw=2.6,
        zorder=3,
    )
    ax.axhline(
        0.0,
        color=ACCENT,
        lw=1.8,
        ls="--",
        zorder=2,
    )
    ax.plot(
        0.0,
        0.0,
        "o",
        color=ACCENT,
        ms=9,
        zorder=5,
    )
    ax.annotate(
        r"$x^*=0$",
        xy=(0.0, 0.0),
        xytext=(0.18, 0.35),
        fontsize=12,
        color=DARK_TEAL,
        fontweight="bold",
    )
    ax.annotate(
        r"$f'(0)=0$, $f''(0)=0\leq 0$",
        xy=(0.85, 0.0),
        xytext=(0.25, -1.55),
        fontsize=12,
        color=ACCENT,
        fontweight="bold",
        arrowprops=dict(
            arrowstyle="->",
            color=ACCENT,
            lw=1.1,
        ),
    )
    ax.annotate(
        r"not a local max",
        xy=(0.9, 0.73),
        fontsize=12,
        color=DARK_TEAL,
        fontweight="bold",
    )

    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-2.2, 2.2)
    ax.set_xlabel(r"$x$", fontsize=11)
    ax.set_ylabel(r"$f(x)=x^3$", fontsize=11)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=9)

    out = OUT_DIR / "soc_not_sufficient.png"
    fig.tight_layout()
    fig.savefig(
        out,
        bbox_inches="tight",
        facecolor="white",
        pad_inches=0.08,
    )
    plt.close()
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
