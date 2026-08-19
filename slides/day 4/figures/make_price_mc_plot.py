"""Price versus MC: why p=MC at an interior profit max."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"
MAX_COLOR = "#27AE60"
MIN_COLOR = "#E74C3C"
OUT_DIR = Path(__file__).resolve().parent
PRICE = 5.0


def mc(q):
    return q**2 - 6 * q + 10


def main():
    fig, ax = plt.subplots(
        figsize=(8.4, 4.6),
        dpi=220,
    )

    grid = np.linspace(0.0, 7.0, 400)
    ax.plot(
        grid,
        mc(grid),
        color=DARK_TEAL,
        lw=2.6,
        zorder=3,
        label=r"$\mathrm{MC}(q)$",
    )
    ax.axhline(
        PRICE,
        color=ACCENT,
        lw=1.9,
        ls="--",
        zorder=2,
    )
    ax.text(
        6.35,
        5.35,
        r"$p=5$",
        fontsize=12,
        color=ACCENT,
        fontweight="bold",
    )

    ax.plot(1.0, PRICE, "v", color=MIN_COLOR, ms=9, zorder=5)
    ax.plot(5.0, PRICE, "*", color=MAX_COLOR, ms=16, zorder=5)
    ax.annotate(
        r"$q=1$",
        xy=(1.0, PRICE),
        xytext=(0.15, 7.4),
        fontsize=11,
        color=MIN_COLOR,
        fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=MIN_COLOR, lw=1.1),
    )
    ax.annotate(
        r"$q=5$",
        xy=(5.0, PRICE),
        xytext=(5.35, 8.0),
        fontsize=11,
        color=MAX_COLOR,
        fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=MAX_COLOR, lw=1.1),
    )

    left = np.linspace(0.0, 1.0, 120)
    mid = np.linspace(1.0, 5.0, 200)
    ax.fill_between(
        left,
        mc(left),
        PRICE,
        color=MIN_COLOR,
        alpha=0.22,
        zorder=1,
    )
    ax.fill_between(
        mid,
        mc(mid),
        PRICE,
        color=MAX_COLOR,
        alpha=0.28,
        zorder=1,
    )
    ax.annotate(
        r"$-\pi$",
        xy=(0.42, 6.6),
        fontsize=12,
        color=MIN_COLOR,
        fontweight="bold",
        ha="center",
    )
    ax.annotate(
        r"profit",
        xy=(3.0, 3.15),
        fontsize=12,
        color=MAX_COLOR,
        fontweight="bold",
        ha="center",
    )
    ax.annotate(
        r"$p<\mathrm{MC}$: produce less",
        xy=(6.05, 12.2),
        fontsize=11,
        color=DARK_TEAL,
        fontweight="bold",
        ha="center",
    )

    ax.set_xlim(0.0, 7.0)
    ax.set_ylim(0.0, 16.0)
    ax.set_xlabel(r"quantity $q$", fontsize=11)
    ax.set_ylabel(r"price, marginal cost", fontsize=11)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=9)

    out = OUT_DIR / "price_equals_mc.png"
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
