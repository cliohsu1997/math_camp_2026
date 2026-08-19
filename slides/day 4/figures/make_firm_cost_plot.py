"""Total cost and marginal cost for the Day 4.1 firm example."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"
OUT_DIR = Path(__file__).resolve().parent


def cost(q):
    return (q**3) / 3 - 3 * q**2 + 10 * q


def mc(q):
    return q**2 - 6 * q + 10


def _style(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=9)
    ax.set_xlabel(r"quantity $q$", fontsize=11)


def main():
    fig, (
        ax_c,
        ax_mc,
    ) = plt.subplots(
        1,
        2,
        figsize=(10.4, 5.1),
        dpi=220,
    )

    grid = np.linspace(0.0, 7.0, 400)

    ax_c.plot(
        grid,
        cost(grid),
        color=DARK_TEAL,
        lw=2.6,
        zorder=3,
    )
    ax_c.set_xlim(0.0, 7.0)
    ax_c.set_ylim(0.0, 40.0)
    ax_c.set_ylabel(r"total cost $C(q)$", fontsize=11)
    ax_c.set_title(
        r"Total cost",
        fontsize=11,
        color=DARK_TEAL,
        pad=6,
    )
    _style(ax_c)

    ax_mc.plot(
        grid,
        mc(grid),
        color=ACCENT,
        lw=2.6,
        zorder=3,
    )
    ax_mc.set_xlim(0.0, 7.0)
    ax_mc.set_ylim(0.0, 16.0)
    ax_mc.set_ylabel(r"marginal cost $\mathrm{MC}(q)$", fontsize=11)
    ax_mc.set_title(
        r"Marginal cost",
        fontsize=11,
        color=DARK_TEAL,
        pad=6,
    )
    _style(ax_mc)

    fig.tight_layout()
    out = OUT_DIR / "firm_cost.png"
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
