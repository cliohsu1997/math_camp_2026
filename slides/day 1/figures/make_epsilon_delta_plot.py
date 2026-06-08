"""Epsilon-delta limit figure for Day 1 section 1.9."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"

A = 1.0
L = 2.0
F_A = 3.0
EPSILON = 0.5
DELTA = 0.5


def make_epsilon_delta_plot() -> None:
    x_left = np.linspace(0.0, A - 0.07, 200)
    x_right = np.linspace(A + 0.07, 3.0, 200)
    y_left = x_left + 1.0
    y_right = x_right + 1.0

    fig, ax = plt.subplots(figsize=(5.0, 4.2), dpi=220)

    ax.axhspan(
        L - EPSILON,
        L + EPSILON,
        color=ACCENT,
        alpha=0.18,
        zorder=0,
    )
    ax.axvspan(
        A - DELTA,
        A + DELTA,
        color=DARK_TEAL,
        alpha=0.10,
        zorder=0,
    )

    ax.axhline(
        L - EPSILON,
        color=ACCENT,
        linestyle="--",
        linewidth=1.6,
        zorder=1,
    )
    ax.axhline(
        L + EPSILON,
        color=ACCENT,
        linestyle="--",
        linewidth=1.6,
        zorder=1,
    )
    ax.axvline(
        A - DELTA,
        color=DARK_TEAL,
        linestyle="--",
        linewidth=1.6,
        zorder=1,
    )
    ax.axvline(
        A + DELTA,
        color=DARK_TEAL,
        linestyle="--",
        linewidth=1.6,
        zorder=1,
    )

    ax.plot(
        x_left,
        y_left,
        color=DARK_TEAL,
        linewidth=2.4,
        zorder=3,
    )
    ax.plot(
        x_right,
        y_right,
        color=DARK_TEAL,
        linewidth=2.4,
        zorder=3,
    )

    ax.plot(
        A,
        L,
        marker="o",
        markersize=9,
        markerfacecolor="white",
        markeredgecolor=DARK_TEAL,
        markeredgewidth=2.0,
        linestyle="none",
        zorder=4,
    )
    ax.plot(
        A,
        F_A,
        marker="o",
        markersize=9,
        markerfacecolor=ACCENT,
        markeredgecolor=ACCENT,
        linestyle="none",
        zorder=5,
    )

    ax.annotate(
        r"$\lim_{x\to a}f(x)=L$",
        xy=(A, L),
        xytext=(A + 0.22, L - 0.55),
        fontsize=10,
        color=DARK_TEAL,
    )
    ax.annotate(
        r"$f(a)$",
        xy=(A, F_A),
        xytext=(A + 0.18, F_A + 0.08),
        fontsize=10,
        color=ACCENT,
    )
    ax.text(
        3.05,
        L - EPSILON - 0.05,
        r"$L-\varepsilon$",
        fontsize=9,
        color=ACCENT,
        ha="right",
    )
    ax.text(
        3.05,
        L + EPSILON + 0.05,
        r"$L+\varepsilon$",
        fontsize=9,
        color=ACCENT,
        ha="right",
        va="bottom",
    )
    ax.text(
        A - DELTA,
        3.75,
        r"$a-\delta$",
        fontsize=9,
        color=DARK_TEAL,
        ha="center",
    )
    ax.text(
        A + DELTA,
        3.75,
        r"$a+\delta$",
        fontsize=9,
        color=DARK_TEAL,
        ha="center",
    )
    ax.text(
        A,
        -0.18,
        r"$a$",
        fontsize=10,
        ha="center",
        color=DARK_TEAL,
    )
    ax.text(
        -0.12,
        L,
        r"$L$",
        fontsize=10,
        ha="right",
        va="center",
        color=DARK_TEAL,
    )

    ax.set_xlim(-0.15, 3.15)
    ax.set_ylim(-0.25, 3.9)
    ax.set_xlabel(r"$x$", fontsize=11)
    ax.set_ylabel(r"$y$", fontsize=11)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=9)

    out = Path(__file__).resolve().parent / "epsilon_delta_limit.png"
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    make_epsilon_delta_plot()
