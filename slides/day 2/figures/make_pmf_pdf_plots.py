"""PMF/CMF and PDF/CDF figures for Day 2 section 2.3."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"
OUT_DIR = Path(__file__).resolve().parent


def _style_axis(ax, xlabel: str, ylabel: str, title: str) -> None:
    ax.set_xlabel(xlabel, fontsize=8)
    ax.set_ylabel(ylabel, fontsize=8)
    ax.set_title(title, fontsize=9, color=DARK_TEAL, pad=6)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=7)


def make_dice_pmf_cmf_plot() -> None:
    """Fair die: PMF bars and CMF at integer outcomes only."""
    k = np.arange(1, 7)
    pmf = np.full(6, 1.0 / 6.0)
    cmf = np.arange(1, 7) / 6.0

    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.1), dpi=220)

    ax = axes[0]
    ax.bar(k, pmf, width=0.72, color=DARK_TEAL, alpha=0.85, edgecolor="white")
    ax.set_xticks(k)
    ax.set_ylim(0.0, 0.22)
    _style_axis(ax, r"$k$", r"$p(k)$", "PMF")

    ax = axes[1]
    ax.bar(k, cmf, width=0.72, color=ACCENT, alpha=0.85, edgecolor="white")
    ax.set_xticks(k)
    ax.set_ylim(0.0, 1.05)
    _style_axis(ax, r"$k$", r"$C(k)$", "CMF")

    fig.subplots_adjust(wspace=0.32)
    out = OUT_DIR / "dice_pmf_cmf.png"
    fig.savefig(out, bbox_inches="tight", facecolor="white", pad_inches=0.06)
    plt.close(fig)
    print(f"Wrote {out}")


def make_uniform_pdf_cdf_plot() -> None:
    """Uniform(0,1): PDF and CDF side by side."""
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.1), dpi=220)

    ax = axes[0]
    ax.add_patch(
        Rectangle(
            (0.0, 0.0),
            1.0,
            1.0,
            facecolor=DARK_TEAL,
            alpha=0.25,
            edgecolor=DARK_TEAL,
            linewidth=2.0,
        )
    )
    ax.plot([0.0, 0.0, 1.0, 1.0], [0.0, 1.0, 1.0, 0.0], color=DARK_TEAL, lw=2.2)
    ax.set_xlim(-0.35, 1.45)
    ax.set_ylim(-0.08, 1.25)
    _style_axis(ax, r"$x$", r"$f(x)$", "PDF")

    ax = axes[1]
    x_left = np.linspace(-0.35, 0.0, 40)
    x_mid = np.linspace(0.0, 1.0, 120)
    x_right = np.linspace(1.0, 1.45, 40)
    ax.plot(x_left, np.zeros_like(x_left), color=ACCENT, lw=2.2)
    ax.plot(x_mid, x_mid, color=ACCENT, lw=2.2)
    ax.plot(x_right, np.ones_like(x_right), color=ACCENT, lw=2.2)
    ax.plot([0.0, 1.0], [0.0, 1.0], "o", color="white", markeredgecolor=ACCENT, ms=5)
    ax.set_xlim(-0.35, 1.45)
    ax.set_ylim(-0.08, 1.25)
    _style_axis(ax, r"$x$", r"$F(x)$", "CDF")

    fig.subplots_adjust(wspace=0.32)
    out = OUT_DIR / "uniform_pdf_cdf.png"
    fig.savefig(out, bbox_inches="tight", facecolor="white", pad_inches=0.06)
    plt.close(fig)
    print(f"Wrote {out}")


def make_expectation_cdf_plot() -> None:
    """E[X] as vertical strips above CDF for X ~ Unif(0,1)."""
    n_strips = 10
    x_edges = np.linspace(0.0, 1.0, n_strips + 1)

    fig, ax = plt.subplots(figsize=(4.6, 3.6), dpi=220)

    for i in range(n_strips):
        x_left = x_edges[i]
        x_right = x_edges[i + 1]
        width = x_right - x_left
        # Left-endpoint height: P(X > x) = 1 - F(x) = 1 - x
        height = 1.0 - x_left
        color = ACCENT if i % 2 == 0 else DARK_TEAL
        ax.add_patch(
            Rectangle(
                (x_left, x_left),
                width,
                height,
                facecolor=color,
                alpha=0.32,
                edgecolor="white",
                linewidth=1.4,
            )
        )

    x = np.linspace(0.0, 1.0, 200)
    ax.plot(x, x, color=DARK_TEAL, linewidth=2.4)
    ax.axhline(1.0, color="0.55", linewidth=1.0, linestyle="--")
    ax.set_xlim(-0.05, 1.08)
    ax.set_ylim(-0.05, 1.12)
    ax.set_xlabel(r"$x$", fontsize=9)
    ax.set_ylabel(r"$y$", fontsize=9)
    ax.set_title(
        r"$X \sim \mathrm{Unif}(0,1)$: strip height $=1-F(x)=P(X>x)$",
        fontsize=9,
        color=DARK_TEAL,
        pad=6,
    )
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=7)

    out = OUT_DIR / "expectation_cdf_region.png"
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    make_dice_pmf_cmf_plot()
    make_uniform_pdf_cdf_plot()
    make_expectation_cdf_plot()
