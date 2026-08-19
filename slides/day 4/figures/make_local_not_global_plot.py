"""Local maximum that is not a global maximum."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"
GLOBAL_COLOR = "#27AE60"
OUT_DIR = Path(__file__).resolve().parent


def f(x):
    return (
        1.55 * np.exp(-2.4 * (x + 1.35) ** 2)
        + 2.45 * np.exp(-1.9 * (x - 1.55) ** 2)
    )


def main():
    fig, ax = plt.subplots(
        figsize=(8.2, 4.2),
        dpi=220,
    )

    grid = np.linspace(-3.0, 3.2, 500)
    ax.plot(
        grid,
        f(grid),
        color=DARK_TEAL,
        lw=2.6,
        zorder=3,
    )

    x_local = -1.35
    x_global = 1.55
    ax.plot(
        x_local,
        f(x_local),
        "o",
        color=ACCENT,
        ms=9,
        zorder=5,
    )
    ax.plot(
        x_global,
        f(x_global),
        "*",
        color=GLOBAL_COLOR,
        ms=15,
        zorder=5,
    )
    ax.annotate(
        r"local max",
        xy=(x_local, f(x_local)),
        xytext=(x_local - 0.15, f(x_local) + 0.38),
        fontsize=12,
        color=ACCENT,
        fontweight="bold",
        ha="center",
    )
    ax.annotate(
        r"global max",
        xy=(x_global, f(x_global)),
        xytext=(x_global + 0.15, f(x_global) + 0.22),
        fontsize=12,
        color=GLOBAL_COLOR,
        fontweight="bold",
        ha="center",
    )

    ax.set_xlim(-3.0, 3.2)
    ax.set_ylim(-0.15, 3.35)
    ax.set_xlabel(r"$x$", fontsize=11)
    ax.set_ylabel(r"$f(x)$", fontsize=11)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=9)
    ax.set_xticks([])
    ax.set_yticks([])

    out = OUT_DIR / "local_not_global.png"
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
