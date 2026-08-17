"""Egg-market supply-demand figure for Day 2 section 2.1."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"


def make_egg_market_plot() -> None:
    q = np.linspace(
        0.0,
        9.5,
        200,
    )
    p_d = 10.0 - q
    p_s = 1.0 + 0.8 * q
    p_s_new = 3.5 + 0.8 * q

    q0 = 5.0
    p0 = 5.0
    q1 = 6.5 / 1.8
    p1 = 10.0 - q1

    fig, ax = plt.subplots(
        figsize=(8.2, 4.2),
        dpi=220,
    )
    ax.plot(
        q,
        p_d,
        color=DARK_TEAL,
        linewidth=2.4,
        label=r"Demand $D$",
        zorder=3,
    )
    ax.plot(
        q,
        p_s,
        color=ACCENT,
        linewidth=2.2,
        label=r"Supply $S$ (old)",
        zorder=3,
    )
    ax.plot(
        q,
        p_s_new,
        color=ACCENT,
        linewidth=2.2,
        linestyle="--",
        label=r"Supply $S'$ (higher feed costs)",
        zorder=3,
    )

    ax.plot(
        q0,
        p0,
        "o",
        color=DARK_TEAL,
        markersize=7,
        zorder=4,
    )
    ax.plot(
        q1,
        p1,
        "o",
        color=ACCENT,
        markersize=7,
        zorder=4,
    )

    ax.hlines(
        p0,
        0,
        q0,
        colors=DARK_TEAL,
        linestyles=":",
        linewidth=1.2,
        alpha=0.7,
    )
    ax.vlines(
        q0,
        0,
        p0,
        colors=DARK_TEAL,
        linestyles=":",
        linewidth=1.2,
        alpha=0.7,
    )
    ax.hlines(
        p1,
        0,
        q1,
        colors=ACCENT,
        linestyles=":",
        linewidth=1.2,
        alpha=0.7,
    )
    ax.vlines(
        q1,
        0,
        p1,
        colors=ACCENT,
        linestyles=":",
        linewidth=1.2,
        alpha=0.7,
    )

    ax.annotate(
        "",
        xy=(q1, p1),
        xytext=(q0, p0),
        arrowprops={
            "arrowstyle": "->",
            "color": ACCENT,
            "lw": 1.6,
        },
    )

    ax.text(
        q0 + 0.18,
        p0 - 0.55,
        r"$(q^*,p^*)$",
        fontsize=10,
        color=DARK_TEAL,
    )
    ax.text(
        q1 + 0.18,
        p1 + 0.28,
        r"$(q^{*'},p^{*'})$",
        fontsize=10,
        color=ACCENT,
    )
    ax.text(
        7.3,
        2.3,
        r"$D$",
        fontsize=12,
        color=DARK_TEAL,
        fontweight="bold",
    )
    ax.text(
        8.15,
        7.05,
        r"$S$",
        fontsize=12,
        color=ACCENT,
        fontweight="bold",
    )
    ax.text(
        5.15,
        8.45,
        r"$S'$",
        fontsize=12,
        color=ACCENT,
        fontweight="bold",
    )

    ax.set_xlim(0, 9.6)
    ax.set_ylim(0, 10.2)
    ax.set_xlabel(
        r"quantity of eggs $q$",
        fontsize=11,
        color=DARK_TEAL,
    )
    ax.set_ylabel(
        r"price $p$",
        fontsize=11,
        color=DARK_TEAL,
    )
    ax.set_xticks(
        [0, q1, q0],
        labels=[r"$0$", r"$q^{*'}$", r"$q^*$"],
    )
    ax.set_yticks(
        [0, p0, p1],
        labels=[r"$0$", r"$p^*$", r"$p^{*'}$"],
    )
    ax.tick_params(
        labelsize=10,
        colors=DARK_TEAL,
    )
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(DARK_TEAL)
    ax.spines["bottom"].set_color(DARK_TEAL)
    ax.legend(
        frameon=False,
        fontsize=9,
        loc="center left",
        bbox_to_anchor=(1.04, 0.5),
        borderaxespad=0.0,
    )

    out = Path(__file__).resolve().parent / "egg_market_supply_shock.png"
    fig.savefig(
        out,
        bbox_inches="tight",
        facecolor="white",
    )
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    make_egg_market_plot()
