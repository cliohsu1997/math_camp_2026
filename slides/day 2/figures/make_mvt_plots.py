"""Rolle and Mean Value Theorem figures for Day 2."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"
OUT_DIR = Path(__file__).resolve().parent


def make_rolle_plot() -> None:
    """f(x)=-(x-1)^2+1 on [0,2]: f(0)=f(2)=0, horizontal tangent at x=1."""
    a, b = 0.0, 2.0
    x = np.linspace(a, b, 300)
    y = -(x - 1.0) ** 2 + 1.0
    c = 1.0
    y_c = 1.0

    fig, ax = plt.subplots(figsize=(4.8, 3.6), dpi=220)
    ax.plot(x, y, color=DARK_TEAL, linewidth=2.4, zorder=3)
    ax.plot([a, b], [0.0, 0.0], color="0.55", linewidth=1.5, linestyle="--", zorder=2)
    ax.axhline(y_c, xmin=0.18, xmax=0.82, color=ACCENT, linewidth=2.0, zorder=4)
    ax.plot([a, b], [0.0, 0.0], "o", color="white", markeredgecolor=DARK_TEAL, markersize=7, zorder=5)
    ax.plot(c, y_c, "o", color=ACCENT, markersize=7, zorder=5)

    ax.annotate(
        r"$a$",
        xy=(a, 0.0),
        xytext=(a, -0.12),
        ha="center",
        fontsize=10,
        color=DARK_TEAL,
    )
    ax.annotate(
        r"$b$",
        xy=(b, 0.0),
        xytext=(b, -0.12),
        ha="center",
        fontsize=10,
        color=DARK_TEAL,
    )
    ax.annotate(
        r"$c$",
        xy=(c, y_c),
        xytext=(c + 0.12, y_c + 0.08),
        fontsize=10,
        color=ACCENT,
    )
    ax.annotate(
        r"$f'(c)=0$",
        xy=(c, y_c),
        xytext=(0.35, 0.82),
        fontsize=9,
        color=ACCENT,
        arrowprops=dict(arrowstyle="->", color=ACCENT, lw=1.2),
    )

    ax.set_xlim(-0.15, 2.15)
    ax.set_ylim(-0.22, 1.18)
    ax.set_xlabel(r"$x$", fontsize=10)
    ax.set_ylabel(r"$f(x)$", fontsize=10)
    ax.set_title(r"Rolle: $f(a)=f(b)$", fontsize=10, color=DARK_TEAL, pad=8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=8)

    out = OUT_DIR / "mvt_rolle.png"
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Wrote {out}")


def make_mvt_plot() -> None:
    """f(x)=x^2 on [0,2]: secant slope equals tangent slope at c=1."""
    a, b = 0.0, 2.0
    x = np.linspace(a, b, 300)
    y = x**2
    c = 1.0
    sec_slope = (b**2 - a**2) / (b - a)
    sec_y = sec_slope * (x - a) + a**2
    tan_x = np.linspace(0.25, 1.75, 2)
    tan_y = sec_slope * (tan_x - c) + c**2

    fig, ax = plt.subplots(figsize=(4.8, 3.6), dpi=220)
    ax.plot(x, y, color=DARK_TEAL, linewidth=2.4, zorder=3)
    ax.plot(x, sec_y, color="0.55", linewidth=1.8, linestyle="--", zorder=2)
    ax.plot(tan_x, tan_y, color=ACCENT, linewidth=2.0, zorder=4)
    ax.plot([a, b], [a**2, b**2], "o", color="white", markeredgecolor=DARK_TEAL, markersize=7, zorder=5)
    ax.plot(c, c**2, "o", color=ACCENT, markersize=7, zorder=5)

    ax.annotate(
        r"secant slope $=2$",
        xy=(1.35, 2.2),
        fontsize=8.5,
        color="0.45",
    )
    ax.annotate(
        r"$f'(c)=2$",
        xy=(c, c**2),
        xytext=(1.45, 0.55),
        fontsize=9,
        color=ACCENT,
        arrowprops=dict(arrowstyle="->", color=ACCENT, lw=1.2),
    )
    ax.annotate(
        r"$c$",
        xy=(c, 0.0),
        xytext=(c, -0.35),
        ha="center",
        fontsize=10,
        color=ACCENT,
    )

    ax.set_xlim(-0.15, 2.25)
    ax.set_ylim(-0.45, 4.5)
    ax.set_xlabel(r"$x$", fontsize=10)
    ax.set_ylabel(r"$f(x)$", fontsize=10)
    ax.set_title(r"MVT: $f(x)=x^2$ on $[0,2]$", fontsize=10, color=DARK_TEAL, pad=8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=8)

    out = OUT_DIR / "mvt_secant_tangent.png"
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Wrote {out}")


def make_mc_ac_plot() -> None:
    """MC and AC for C(q)=q^2+4; cross at minimum AC (q*=2)."""
    q = np.linspace(0.35, 5.0, 300)
    mc = 2.0 * q
    ac = q + 4.0 / q
    q_star = 2.0
    mc_star = 4.0

    fig, ax = plt.subplots(figsize=(5.2, 3.8), dpi=220)
    ax.plot(q, mc, color=ACCENT, linewidth=2.4, zorder=3)
    ax.plot(q, ac, color=DARK_TEAL, linewidth=2.4, zorder=3)
    ax.plot(q_star, mc_star, "o", color="white", markeredgecolor=ACCENT, markersize=8, zorder=5)
    ax.plot(q_star, mc_star, "o", color="white", markeredgecolor=DARK_TEAL, markersize=8, zorder=5)
    ax.axvline(q_star, color="0.75", linestyle=":", linewidth=1.0, zorder=1)

    ax.text(4.55, 2.0 * 4.55 + 0.25, "MC", color=ACCENT, fontsize=9, ha="right", va="bottom")
    ax.text(4.55, 4.55 + 4.0 / 4.55 + 0.25, "AC", color=DARK_TEAL, fontsize=9, ha="right", va="bottom")

    ax.annotate(
        r"$q^*$",
        xy=(q_star, 0.0),
        xytext=(q_star, -0.35),
        ha="center",
        fontsize=10,
        color=DARK_TEAL,
    )
    ax.annotate(
        r"MC$=$AC",
        xy=(q_star, mc_star),
        xytext=(3.1, 5.2),
        fontsize=9,
        color=ACCENT,
        arrowprops=dict(arrowstyle="->", color=ACCENT, lw=1.2),
    )

    ax.set_xlim(0.0, 5.2)
    ax.set_ylim(0.0, 8.5)
    ax.set_xlabel(r"output $q$", fontsize=10)
    ax.set_ylabel(r"cost per unit", fontsize=10)
    ax.set_title(r"$C(q)=q^2+4$: MC and AC", fontsize=10, color=DARK_TEAL, pad=8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=8)

    out = OUT_DIR / "mvt_mc_ac.png"
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    make_rolle_plot()
    make_mvt_plot()
    make_mc_ac_plot()
