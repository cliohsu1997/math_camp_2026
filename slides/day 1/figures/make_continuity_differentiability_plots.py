"""Continuity vs differentiability figures for Day 1 section 1.9."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"
OUT_DIR = Path(__file__).resolve().parent


def make_abs_corner_plot() -> None:
    x = np.linspace(-2.0, 2.0, 400)
    y = np.abs(x)

    fig, ax = plt.subplots(figsize=(4.6, 3.6), dpi=220)
    ax.plot(x, y, color=DARK_TEAL, linewidth=2.4, zorder=3)
    ax.plot(0.0, 0.0, marker="o", markersize=7, color=ACCENT, zorder=4)

    ax.plot(
        [-0.9, 0.0],
        [0.9, 0.0],
        color=ACCENT,
        linewidth=1.5,
        linestyle="--",
        zorder=2,
    )
    ax.plot(
        [0.0, 0.9],
        [0.0, 0.9],
        color=ACCENT,
        linewidth=1.5,
        linestyle="--",
        zorder=2,
    )
    ax.annotate(
        "slope $-1$",
        xy=(-0.55, 0.55),
        fontsize=9,
        color=ACCENT,
    )
    ax.annotate(
        "slope $+1$",
        xy=(0.18, 0.55),
        fontsize=9,
        color=ACCENT,
    )
    ax.annotate(
        r"$x=0$",
        xy=(0.0, 0.0),
        xytext=(0.12, -0.35),
        fontsize=9,
        color=DARK_TEAL,
    )

    ax.set_xlim(-2.1, 2.1)
    ax.set_ylim(-0.35, 2.2)
    ax.set_xlabel(r"$x$", fontsize=10)
    ax.set_ylabel(r"$y$", fontsize=10)
    ax.set_title(r"$f(x)=|x|$", fontsize=11, color=DARK_TEAL, pad=8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=8)

    out = OUT_DIR / "abs_x_corner.png"
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Wrote {out}")


def weierstrass_partial(x: np.ndarray, n_terms: int = 10) -> np.ndarray:
    a = 0.5
    b = 7.0
    y = np.zeros_like(x, dtype=float)
    for n in range(n_terms + 1):
        y += (a**n) * np.cos((b**n) * np.pi * x)
    return y


def make_weierstrass_plot() -> None:
    x = np.linspace(-1.0, 1.0, 4000)
    y = weierstrass_partial(x, n_terms=10)

    fig, ax = plt.subplots(figsize=(4.6, 3.6), dpi=220)
    ax.plot(x, y, color=DARK_TEAL, linewidth=1.0, zorder=3)

    ax.set_xlim(-1.0, 1.0)
    ax.set_ylim(-2.0, 2.0)
    ax.set_xlabel(r"$x$", fontsize=10)
    ax.set_ylabel(r"$y$", fontsize=10)
    ax.set_title(
        r"Weierstrass function (partial sum)",
        fontsize=10,
        color=DARK_TEAL,
        pad=8,
    )
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=8)

    out = OUT_DIR / "weierstrass_partial.png"
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    make_abs_corner_plot()
    make_weierstrass_plot()
