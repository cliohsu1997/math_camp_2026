"""Two-panel linear market: supply shock vs demand shock."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"


def _mark_equilibrium(
    ax,
    q_star,
    p_star,
    color,
    label,
    dx,
    dy,
):
    ax.plot(
        q_star,
        p_star,
        "o",
        color=color,
        markersize=6.5,
        zorder=4,
    )
    ax.hlines(
        p_star,
        0,
        q_star,
        colors=color,
        linestyles=":",
        linewidth=1.1,
        alpha=0.7,
    )
    ax.vlines(
        q_star,
        0,
        p_star,
        colors=color,
        linestyles=":",
        linewidth=1.1,
        alpha=0.7,
    )
    ax.text(
        q_star + dx,
        p_star + dy,
        label,
        fontsize=9,
        color=color,
    )


def _style_axes(
    ax,
    title,
    q_ticks,
    q_labels,
    p_ticks,
    p_labels,
):
    ax.set_xlim(
        0,
        10.2,
    )
    ax.set_ylim(
        0,
        9.2,
    )
    ax.set_title(
        title,
        fontsize=11,
        color=DARK_TEAL,
        pad=8,
    )
    ax.set_xlabel(
        r"quantity $q$",
        fontsize=10,
        color=DARK_TEAL,
    )
    ax.set_ylabel(
        r"price $p$",
        fontsize=10,
        color=DARK_TEAL,
    )
    ax.set_xticks(
        q_ticks,
        labels=q_labels,
    )
    ax.set_yticks(
        p_ticks,
        labels=p_labels,
    )
    ax.tick_params(
        labelsize=9,
        colors=DARK_TEAL,
    )
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(DARK_TEAL)
    ax.spines["bottom"].set_color(DARK_TEAL)


def make_linear_market_two_shocks() -> None:
    q = np.linspace(
        0.0,
        10.0,
        200,
    )
    # Baseline: α=8, b=1, d=1, s=2 → (q*, p*) = (5, 3)
    p_d = 8.0 - q
    p_s = q - 2.0
    # Positive supply shock: s=4 → (6, 2)
    p_s_new = q - 4.0
    # Positive demand shock: α=10 → (6, 4)
    p_d_new = 10.0 - q

    fig, axes = plt.subplots(
        1,
        2,
        figsize=(10.8, 4.2),
        dpi=220,
    )
    ax_s, ax_d = axes

    ax_s.plot(
        q,
        p_d,
        color=DARK_TEAL,
        linewidth=2.3,
        zorder=3,
    )
    ax_s.plot(
        q,
        p_s,
        color=ACCENT,
        linewidth=2.1,
        zorder=3,
    )
    ax_s.plot(
        q,
        p_s_new,
        color=ACCENT,
        linewidth=2.1,
        linestyle="--",
        zorder=3,
    )
    _mark_equilibrium(
        ax_s,
        5.0,
        3.0,
        DARK_TEAL,
        r"$(q^*,p^*)$",
        0.18,
        -0.55,
    )
    _mark_equilibrium(
        ax_s,
        6.0,
        2.0,
        ACCENT,
        r"$(q^{*'},p^{*'})$",
        0.18,
        -0.55,
    )
    ax_s.annotate(
        "",
        xy=(6.0, 2.0),
        xytext=(5.0, 3.0),
        arrowprops={
            "arrowstyle": "->",
            "color": ACCENT,
            "lw": 1.5,
        },
    )
    ax_s.text(
        7.15,
        1.15,
        r"$D$",
        fontsize=11,
        color=DARK_TEAL,
        fontweight="bold",
    )
    ax_s.text(
        8.15,
        6.35,
        r"$S$",
        fontsize=11,
        color=ACCENT,
        fontweight="bold",
    )
    ax_s.text(
        8.15,
        4.35,
        r"$S'$",
        fontsize=11,
        color=ACCENT,
        fontweight="bold",
    )
    _style_axes(
        ax_s,
        r"Positive supply shock ($s\uparrow$)",
        [0, 5, 6],
        [r"$0$", r"$q^*$", r"$q^{*'}$"],
        [0, 2, 3],
        [r"$0$", r"$p^{*'}$", r"$p^*$"],
    )

    ax_d.plot(
        q,
        p_d,
        color=DARK_TEAL,
        linewidth=2.3,
        zorder=3,
    )
    ax_d.plot(
        q,
        p_d_new,
        color=DARK_TEAL,
        linewidth=2.3,
        linestyle="--",
        zorder=3,
    )
    ax_d.plot(
        q,
        p_s,
        color=ACCENT,
        linewidth=2.1,
        zorder=3,
    )
    _mark_equilibrium(
        ax_d,
        5.0,
        3.0,
        DARK_TEAL,
        r"$(q^*,p^*)$",
        0.18,
        -0.55,
    )
    _mark_equilibrium(
        ax_d,
        6.0,
        4.0,
        ACCENT,
        r"$(q^{*'},p^{*'})$",
        0.18,
        0.22,
    )
    ax_d.annotate(
        "",
        xy=(6.0, 4.0),
        xytext=(5.0, 3.0),
        arrowprops={
            "arrowstyle": "->",
            "color": ACCENT,
            "lw": 1.5,
        },
    )
    ax_d.text(
        7.15,
        1.15,
        r"$D$",
        fontsize=11,
        color=DARK_TEAL,
        fontweight="bold",
    )
    ax_d.text(
        7.15,
        3.15,
        r"$D'$",
        fontsize=11,
        color=DARK_TEAL,
        fontweight="bold",
    )
    ax_d.text(
        8.15,
        6.35,
        r"$S$",
        fontsize=11,
        color=ACCENT,
        fontweight="bold",
    )
    _style_axes(
        ax_d,
        r"Positive demand shock ($\alpha\uparrow$)",
        [0, 5, 6],
        [r"$0$", r"$q^*$", r"$q^{*'}$"],
        [0, 3, 4],
        [r"$0$", r"$p^*$", r"$p^{*'}$"],
    )

    fig.tight_layout()
    out = Path(__file__).resolve().parent / "linear_market_two_shocks.png"
    fig.savefig(
        out,
        bbox_inches="tight",
        facecolor="white",
    )
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    make_linear_market_two_shocks()
