"""IVT figures: generic sign-change and nonlinear excess demand."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"
OUT_DIR = Path(__file__).resolve().parent

ALPHA = 6.0
S = 0.5
P_BAR = 5.0


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


def _excess(
    p,
    alpha: float,
    s: float,
):
    return (
        alpha * np.exp(-p)
        - s
        - p
    )


def _style_axis(
    ax,
    title: str,
    xlabel: str,
    ylabel: str,
) -> None:
    ax.set_title(
        title,
        fontsize=11,
        color=DARK_TEAL,
        pad=8,
    )
    ax.set_xlabel(
        xlabel,
        fontsize=10,
        color=DARK_TEAL,
    )
    ax.set_ylabel(
        ylabel,
        fontsize=10,
        color=DARK_TEAL,
    )
    ax.tick_params(
        labelsize=9,
        colors=DARK_TEAL,
    )
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(DARK_TEAL)
    ax.spines["bottom"].set_color(DARK_TEAL)


def make_ivt_generic() -> None:
    a = 0.0
    b = 2.0
    x = np.linspace(
        a,
        b,
        300,
    )
    y = 2.0 - x ** 2
    k = 1.0
    c = np.sqrt(2.0 - k)

    fig, ax = plt.subplots(
        figsize=(4.8, 3.6),
        dpi=220,
    )
    ax.plot(
        x,
        y,
        color=DARK_TEAL,
        linewidth=2.4,
        zorder=3,
    )
    ax.axhline(
        k,
        color="0.55",
        linewidth=1.4,
        linestyle="--",
        zorder=2,
    )
    ax.text(
        2.02,
        k + 0.08,
        r"$k$",
        fontsize=10,
        color="0.4",
    )
    ax.plot(
        [a, b],
        [y[0], y[-1]],
        "o",
        color="white",
        markeredgecolor=DARK_TEAL,
        markersize=7,
        zorder=5,
    )
    ax.plot(
        c,
        k,
        "o",
        color=ACCENT,
        markersize=7,
        zorder=5,
    )
    ax.annotate(
        r"$a$",
        xy=(a, y[0]),
        xytext=(a + 0.08, y[0] + 0.12),
        fontsize=10,
        color=DARK_TEAL,
    )
    ax.annotate(
        r"$b$",
        xy=(b, y[-1]),
        xytext=(b - 0.18, y[-1] - 0.28),
        fontsize=10,
        color=DARK_TEAL,
    )
    ax.annotate(
        r"$c$",
        xy=(c, k),
        xytext=(c + 0.08, 0.22),
        fontsize=10,
        color=ACCENT,
    )
    ax.annotate(
        r"$f(c)=k$",
        xy=(c, k),
        xytext=(0.45, -0.85),
        fontsize=9,
        color=ACCENT,
        arrowprops={
            "arrowstyle": "->",
            "color": ACCENT,
            "lw": 1.2,
        },
    )

    ax.set_xlim(
        -0.15,
        2.18,
    )
    ax.set_ylim(
        -2.35,
        2.35,
    )
    ax.set_xlabel(
        r"$x$",
        fontsize=10,
    )
    ax.set_ylabel(
        r"$f(x)$",
        fontsize=10,
    )
    ax.set_title(
        r"IVT: $k$ between $f(a)$ and $f(b)$",
        fontsize=10,
        color=DARK_TEAL,
        pad=8,
    )
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(
        labelsize=8,
    )

    fig.tight_layout()
    out = OUT_DIR / "ivt_generic.png"
    fig.savefig(
        out,
        bbox_inches="tight",
        facecolor="white",
    )
    plt.close(fig)
    print(f"Wrote {out}")


def make_ivt_excess_demand() -> None:
    p_star = _find_p_star(
        ALPHA,
        S,
    )
    q_star = S + p_star
    e0 = _excess(
        0.0,
        ALPHA,
        S,
    )
    e_bar = _excess(
        P_BAR,
        ALPHA,
        S,
    )

    fig, axes = plt.subplots(
        1,
        2,
        figsize=(10.8, 4.2),
        dpi=220,
    )
    ax_m, ax_e = axes

    p_curve = np.linspace(
        0.05,
        4.6,
        250,
    )
    q_d = ALPHA * np.exp(-p_curve)
    ax_m.plot(
        q_d,
        p_curve,
        color=DARK_TEAL,
        linewidth=2.3,
        zorder=3,
    )
    q_s = np.linspace(
        S,
        7.2,
        200,
    )
    p_s = q_s - S
    ax_m.plot(
        q_s,
        p_s,
        color=ACCENT,
        linewidth=2.1,
        zorder=3,
    )
    ax_m.plot(
        q_star,
        p_star,
        "o",
        color=DARK_TEAL,
        markersize=6.5,
        zorder=4,
    )
    ax_m.hlines(
        p_star,
        0,
        q_star,
        colors=DARK_TEAL,
        linestyles=":",
        linewidth=1.1,
        alpha=0.7,
    )
    ax_m.vlines(
        q_star,
        0,
        p_star,
        colors=DARK_TEAL,
        linestyles=":",
        linewidth=1.1,
        alpha=0.7,
    )
    ax_m.text(
        q_star + 0.15,
        p_star + 0.18,
        r"$(q^*,p^*)$",
        fontsize=9,
        color=DARK_TEAL,
    )
    ax_m.text(
        3.55,
        0.32,
        r"$D$",
        fontsize=11,
        color=DARK_TEAL,
        fontweight="bold",
    )
    ax_m.text(
        4.05,
        3.45,
        r"$S$",
        fontsize=11,
        color=ACCENT,
        fontweight="bold",
    )
    ax_m.set_xlim(
        0,
        7.4,
    )
    ax_m.set_ylim(
        0,
        4.4,
    )
    ax_m.set_xticks(
        [0, q_star],
        labels=[r"$0$", r"$q^*$"],
    )
    ax_m.set_yticks(
        [0, p_star],
        labels=[r"$0$", r"$p^*$"],
    )
    _style_axis(
        ax_m,
        r"$D=6e^{-p}$, $S=\frac{1}{2}+p$",
        r"quantity $q$",
        r"price $p$",
    )

    p = np.linspace(
        0.0,
        P_BAR,
        300,
    )
    e = _excess(
        p,
        ALPHA,
        S,
    )
    ax_e.plot(
        p,
        e,
        color=DARK_TEAL,
        linewidth=2.4,
        zorder=3,
    )
    ax_e.axhline(
        0.0,
        color="0.55",
        linewidth=1.3,
        linestyle="--",
        zorder=2,
    )
    ax_e.fill_between(
        p,
        0.0,
        e,
        where=(e >= 0.0),
        color=DARK_TEAL,
        alpha=0.12,
        zorder=1,
    )
    ax_e.fill_between(
        p,
        0.0,
        e,
        where=(e <= 0.0),
        color=ACCENT,
        alpha=0.12,
        zorder=1,
    )
    ax_e.plot(
        0.0,
        e0,
        "o",
        color=DARK_TEAL,
        markersize=6.5,
        zorder=4,
    )
    ax_e.plot(
        P_BAR,
        e_bar,
        "o",
        color=ACCENT,
        markersize=6.5,
        zorder=4,
    )
    ax_e.plot(
        p_star,
        0.0,
        "o",
        color=ACCENT,
        markersize=7,
        zorder=5,
    )
    ax_e.annotate(
        r"$E(0)>0$",
        xy=(0.0, e0),
        xytext=(0.45, e0 - 0.15),
        fontsize=9,
        color=DARK_TEAL,
    )
    ax_e.annotate(
        r"$E(5)<0$",
        xy=(P_BAR, e_bar),
        xytext=(P_BAR - 1.85, e_bar + 0.55),
        fontsize=9,
        color=ACCENT,
    )
    ax_e.annotate(
        r"$E(p^*)=0$",
        xy=(p_star, 0.0),
        xytext=(p_star + 0.35, 1.35),
        fontsize=9,
        color=ACCENT,
        arrowprops={
            "arrowstyle": "->",
            "color": ACCENT,
            "lw": 1.2,
        },
    )
    ax_e.text(
        0.35,
        2.35,
        "shortage",
        fontsize=9,
        color=DARK_TEAL,
    )
    ax_e.text(
        3.35,
        -2.15,
        "surplus",
        fontsize=9,
        color=ACCENT,
    )
    ax_e.set_xlim(
        -0.12,
        P_BAR + 0.25,
    )
    ax_e.set_ylim(
        e_bar - 0.7,
        e0 + 0.7,
    )
    ax_e.set_xticks(
        [0, p_star, P_BAR],
        labels=[r"$0$", r"$p^*$", r"$5$"],
    )
    ax_e.set_yticks(
        [e_bar, 0.0, e0],
        labels=[r"$E(5)$", r"$0$", r"$E(0)$"],
    )
    _style_axis(
        ax_e,
        r"Excess demand $E(p)$",
        r"price $p$",
        r"$E(p)$",
    )

    fig.tight_layout()
    out = OUT_DIR / "ivt_excess_demand.png"
    fig.savefig(
        out,
        bbox_inches="tight",
        facecolor="white",
    )
    plt.close(fig)
    print(f"Wrote {out}")
    print(
        f"p*={p_star:.4f}, q*={q_star:.4f}, "
        f"E(0)={e0:.3f}, E(bar)={e_bar:.3f}"
    )


if __name__ == "__main__":
    make_ivt_generic()
    make_ivt_excess_demand()
