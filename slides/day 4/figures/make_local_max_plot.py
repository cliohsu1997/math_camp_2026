"""Local maximum: necessary conditions f'=0 and f''<=0."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"
OUT_DIR = Path(__file__).resolve().parent


def f(x):
    return -0.55 * (x - 1.2) ** 2 + 2.15


def main():
    fig, ax = plt.subplots(
        figsize=(8.2, 4.4),
        dpi=220,
    )

    grid = np.linspace(-0.6, 3.0, 400)
    ax.plot(
        grid,
        f(grid),
        color=DARK_TEAL,
        lw=2.6,
        zorder=3,
    )

    x_star = 1.2
    y_star = f(x_star)
    tangent_x = np.linspace(0.15, 2.25, 50)
    ax.plot(
        tangent_x,
        np.full_like(tangent_x, y_star),
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
        r"$f'(x^*)=0$",
        xy=(2.15, y_star),
        xytext=(2.15, y_star + 0.28),
        fontsize=12,
        color=ACCENT,
        fontweight="bold",
        ha="center",
    )
    ax.annotate(
        r"$x^*$",
        xy=(x_star, y_star),
        xytext=(x_star, y_star + 0.22),
        fontsize=12,
        color=DARK_TEAL,
        fontweight="bold",
        ha="center",
    )
    ax.annotate(
        r"$f''(x^*)\leq 0$",
        xy=(2.35, 1.15),
        fontsize=12,
        color=DARK_TEAL,
        fontweight="bold",
        ha="center",
    )

    ax.set_xlim(-0.6, 3.0)
    ax.set_ylim(0.0, 2.8)
    ax.set_xlabel(r"$x$", fontsize=11)
    ax.set_ylabel(r"$f(x)$", fontsize=11)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=9)
    ax.set_xticks([])
    ax.set_yticks([])

    out = OUT_DIR / "local_max_necessary.png"
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
