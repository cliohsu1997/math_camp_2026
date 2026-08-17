"""Two-panel nonlinear market: supply shock vs demand shock."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"


def _find_p_star(
    alpha: float,
    s: float,
) -> float:
    lo = 0.0
    hi = 8.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        excess = (
            alpha * np.exp(-mid)
            - s
            - mid
        )
        if excess > 0.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


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
        7.6,
    )
    ax.set_ylim(
        0,
        4.2,
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


def _plot_demand(
    ax,
    alpha,
    linestyle,
    linewidth,
):
    p = np.linspace(
        0.05,
        4.3,
        250,
    )
    q = alpha * np.exp(-p)
    ax.plot(
        q,
        p,
        color=DARK_TEAL,
        linewidth=linewidth,
        linestyle=linestyle,
        zorder=3,
    )


def _plot_supply(
    ax,
    s,
    linestyle,
    linewidth,
):
    q = np.linspace(
        s,
        8.2,
        200,
    )
    p = q - s
    ax.plot(
        q,
        p,
        color=ACCENT,
        linewidth=linewidth,
        linestyle=linestyle,
        zorder=3,
    )


def make_nonlinear_market_two_shocks() -> None:
    alpha0 = 6.0
    s0 = 0.5
    alpha1 = 12.0
    s1 = 2.0

    p0 = _find_p_star(
        alpha0,
        s0,
    )
    q0 = s0 + p0
    p_s = _find_p_star(
        alpha0,
        s1,
    )
    q_s = s1 + p_s
    p_d = _find_p_star(
        alpha1,
        s0,
    )
    q_d = s0 + p_d

    fig, axes = plt.subplots(
        1,
        2,
        figsize=(10.8, 4.2),
        dpi=220,
    )
    ax_s, ax_d = axes

    _plot_demand(
        ax_s,
        alpha0,
        "-",
        2.3,
    )
    _plot_supply(
        ax_s,
        s0,
        "-",
        2.1,
    )
    _plot_supply(
        ax_s,
        s1,
        "--",
        2.1,
    )
    _mark_equilibrium(
        ax_s,
        q0,
        p0,
        DARK_TEAL,
        r"$(q^*,p^*)$",
        0.12,
        0.18,
    )
    _mark_equilibrium(
        ax_s,
        q_s,
        p_s,
        ACCENT,
        r"$(q^{*'},p^{*'})$",
        0.12,
        -0.38,
    )
    ax_s.annotate(
        "",
        xy=(q_s, p_s),
        xytext=(q0, p0),
        arrowprops={
            "arrowstyle": "->",
            "color": ACCENT,
            "lw": 1.5,
        },
    )
    ax_s.text(
        3.85,
        0.38,
        r"$D$",
        fontsize=11,
        color=DARK_TEAL,
        fontweight="bold",
    )
    ax_s.text(
        4.15,
        3.55,
        r"$S$",
        fontsize=11,
        color=ACCENT,
        fontweight="bold",
    )
    ax_s.text(
        5.55,
        3.45,
        r"$S'$",
        fontsize=11,
        color=ACCENT,
        fontweight="bold",
    )
    _style_axes(
        ax_s,
        r"Positive supply shock ($s\uparrow$)",
        [0, q0, q_s],
        [r"$0$", r"$q^*$", r"$q^{*'}$"],
        [0, p_s, p0],
        [r"$0$", r"$p^{*'}$", r"$p^*$"],
    )

    _plot_demand(
        ax_d,
        alpha0,
        "-",
        2.3,
    )
    _plot_demand(
        ax_d,
        alpha1,
        "--",
        2.3,
    )
    _plot_supply(
        ax_d,
        s0,
        "-",
        2.1,
    )
    _mark_equilibrium(
        ax_d,
        q0,
        p0,
        DARK_TEAL,
        r"$(q^*,p^*)$",
        0.12,
        -0.38,
    )
    _mark_equilibrium(
        ax_d,
        q_d,
        p_d,
        ACCENT,
        r"$(q^{*'},p^{*'})$",
        0.12,
        0.16,
    )
    ax_d.annotate(
        "",
        xy=(q_d, p_d),
        xytext=(q0, p0),
        arrowprops={
            "arrowstyle": "->",
            "color": ACCENT,
            "lw": 1.5,
        },
    )
    ax_d.text(
        3.85,
        0.38,
        r"$D$",
        fontsize=11,
        color=DARK_TEAL,
        fontweight="bold",
    )
    ax_d.text(
        5.85,
        0.55,
        r"$D'$",
        fontsize=11,
        color=DARK_TEAL,
        fontweight="bold",
    )
    ax_d.text(
        4.15,
        3.55,
        r"$S$",
        fontsize=11,
        color=ACCENT,
        fontweight="bold",
    )
    _style_axes(
        ax_d,
        r"Positive demand shock ($\alpha\uparrow$)",
        [0, q0, q_d],
        [r"$0$", r"$q^*$", r"$q^{*'}$"],
        [0, p0, p_d],
        [r"$0$", r"$p^*$", r"$p^{*'}$"],
    )

    fig.tight_layout()
    out = (
        Path(__file__).resolve().parent
        / "nonlinear_market_two_shocks.png"
    )
    fig.savefig(
        out,
        bbox_inches="tight",
        facecolor="white",
    )
    plt.close(fig)
    print(f"Wrote {out}")
    print(
        f"baseline (q,p)=({q0:.3f},{p0:.3f}); "
        f"supply ({q_s:.3f},{p_s:.3f}); "
        f"demand ({q_d:.3f},{p_d:.3f})"
    )


if __name__ == "__main__":
    make_nonlinear_market_two_shocks()
