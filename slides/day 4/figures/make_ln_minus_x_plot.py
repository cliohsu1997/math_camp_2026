"""Graph of f(x)=ln(x)-x: unique global max at x=1."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"
OUT_DIR = Path(__file__).resolve().parent


def f(x):
    return np.log(x) - x


def main():
    fig, ax = plt.subplots(
        figsize=(7.4, 4.6),
        dpi=220,
    )

    grid = np.linspace(
        0.12,
        4.2,
        500,
    )
    ax.plot(
        grid,
        f(grid),
        color=DARK_TEAL,
        lw=2.6,
        zorder=3,
    )

    x_star = 1.0
    y_star = f(x_star)
    tangent_x = np.linspace(
        0.28,
        1.72,
        50,
    )
    ax.plot(
        tangent_x,
        np.full_like(
            tangent_x,
            y_star,
        ),
        "--",
        color=ACCENT,
        lw=2.0,
        zorder=2,
    )
    ax.plot(
        x_star,
        y_star,
        "o",
        color=ACCENT,
        ms=9,
        zorder=5,
    )
    ax.annotate(
        r"$x^*=1$",
        xy=(
            x_star,
            y_star,
        ),
        xytext=(
            x_star,
            y_star + 0.28,
        ),
        fontsize=12,
        color=DARK_TEAL,
        fontweight="bold",
        ha="center",
    )
    ax.annotate(
        r"$f'(x^*)=0$",
        xy=(
            1.68,
            y_star,
        ),
        xytext=(
            2.45,
            y_star + 0.12,
        ),
        fontsize=11,
        color=ACCENT,
        fontweight="bold",
        ha="center",
        arrowprops={
            "arrowstyle": "->",
            "color": ACCENT,
            "lw": 1.2,
        },
    )
    ax.annotate(
        r"unique global max",
        xy=(
            2.55,
            -1.72,
        ),
        fontsize=11,
        color=DARK_TEAL,
        fontweight="bold",
        ha="center",
    )

    ax.axvline(
        0.0,
        color=DARK_TEAL,
        lw=0.8,
        alpha=0.35,
        zorder=1,
    )
    ax.set_xlim(
        -0.15,
        4.35,
    )
    ax.set_ylim(
        -3.35,
        -0.45,
    )
    ax.set_xlabel(
        r"$x>0$",
        fontsize=11,
    )
    ax.set_ylabel(
        r"$f(x)=\ln(x)-x$",
        fontsize=11,
    )
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=9)
    ax.set_xticks(
        [
            1,
        ]
    )
    ax.set_xticklabels(
        [
            r"$1$",
        ]
    )
    ax.set_yticks([])

    out = OUT_DIR / "ln_minus_x.png"
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
