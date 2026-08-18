"""Fixed-point figures for Day 3 section 3.1."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"
OUT_DIR = Path(__file__).resolve().parent


def _style_axes(
    ax: plt.Axes,
    title: str,
) -> None:
    ax.set_xlim(
        0.0,
        1.0,
    )
    ax.set_ylim(
        0.0,
        1.0,
    )
    ax.set_aspect(
        "equal",
        adjustable="box",
    )
    ax.set_xlabel(
        r"$x$",
        fontsize=10,
    )
    ax.set_ylabel(
        r"$T(x)$",
        fontsize=10,
    )
    ax.set_title(
        title,
        fontsize=10,
        color=DARK_TEAL,
        pad=8,
    )
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=8)


def _plot_diagonal(
    ax: plt.Axes,
) -> None:
    ax.plot(
        [0.0, 1.0],
        [0.0, 1.0],
        color="0.55",
        linewidth=1.8,
        linestyle="--",
        zorder=2,
        label=r"$y=x$",
    )


def make_brouwer_fixed_point_plot() -> None:
    """Continuous T on [0,1]: T(x)=x+0.1*sin(4*pi*x) crosses y=x several times."""
    x = np.linspace(
        0.0,
        1.0,
        400,
    )
    y = (
        x
        + 0.10 * np.sin(4.0 * np.pi * x)
    )

    fig, ax = plt.subplots(
        figsize=(4.8, 3.9),
        dpi=220,
    )
    _plot_diagonal(ax)
    ax.plot(
        x,
        y,
        color=DARK_TEAL,
        linewidth=2.4,
        zorder=3,
        label=r"$y=T(x)$",
    )

    crossings = []
    for i in range(len(x) - 1):
        diff0 = y[i] - x[i]
        diff1 = y[i + 1] - x[i + 1]
        if diff0 == 0.0:
            crossings.append(x[i])
        elif (
            diff0 * diff1 < 0.0
        ):
            crossings.append(
                0.5 * (x[i] + x[i + 1])
            )

    interior = [
        xc
        for xc in crossings
        if 0.02 < xc < 0.98
    ][:3]
    label_offsets = [
        (0.04, 0.08),
        (-0.10, -0.10),
        (0.04, 0.08),
    ]
    for j, xc in enumerate(interior):
        ax.plot(
            xc,
            xc,
            "o",
            color=ACCENT,
            markersize=7,
            zorder=5,
        )
        dx, dy = label_offsets[j % len(label_offsets)]
        ax.annotate(
            rf"$x^*_{j + 1}$",
            xy=(xc, xc),
            xytext=(xc + dx, xc + dy),
            fontsize=9,
            color=ACCENT,
        )

    _style_axes(
        ax,
        r"Multiple fixed points possible",
    )
    ax.legend(
        loc="upper center",
        bbox_to_anchor=(0.5, -0.14),
        ncol=2,
        fontsize=8,
        frameon=False,
        handlelength=2.2,
    )

    out = OUT_DIR / "fixed_point_brouwer.png"
    fig.tight_layout()
    fig.savefig(
        out,
        bbox_inches="tight",
        facecolor="white",
        pad_inches=0.12,
    )
    plt.close(fig)
    print(f"Wrote {out}")


def make_brouwer_hypothesis_failures() -> None:
    """Non-compact and non-convex domains: continuous T with no fixed point."""
    fig, axes = plt.subplots(
        1,
        2,
        figsize=(9.2, 3.9),
        dpi=220,
    )

    ax_open = axes[0]
    _plot_diagonal(ax_open)
    x_open = np.linspace(
        0.02,
        0.98,
        300,
    )
    ax_open.plot(
        x_open,
        0.5 * x_open,
        color=DARK_TEAL,
        linewidth=2.4,
        zorder=3,
        label=r"$T(x)=x/2$",
    )
    ax_open.plot(
        0.0,
        0.0,
        "o",
        markersize=8,
        markerfacecolor="white",
        markeredgecolor=ACCENT,
        markeredgewidth=1.8,
        zorder=5,
    )
    ax_open.annotate(
        r"$0\notin K$",
        xy=(0.0, 0.0),
        xytext=(0.10, 0.18),
        fontsize=9,
        color=ACCENT,
        arrowprops={
            "arrowstyle": "->",
            "color": ACCENT,
            "lw": 1.2,
        },
    )
    _style_axes(
        ax_open,
        r"Not compact: $K=(0,1)$",
    )
    ax_open.legend(
        loc="upper left",
        fontsize=8,
        frameon=False,
    )

    ax_gap = axes[1]
    _plot_diagonal(ax_gap)
    left = np.linspace(
        0.0,
        0.35,
        80,
    )
    right = np.linspace(
        0.65,
        1.0,
        80,
    )
    ax_gap.plot(
        left,
        left + 0.65,
        color=DARK_TEAL,
        linewidth=2.4,
        zorder=3,
        label=r"$T$ swaps pieces",
    )
    ax_gap.plot(
        right,
        right - 0.65,
        color=DARK_TEAL,
        linewidth=2.4,
        zorder=3,
    )
    ax_gap.axvspan(
        0.35,
        0.65,
        color="0.90",
        zorder=0,
    )
    ax_gap.annotate(
        r"gap: not convex",
        xy=(0.50, 0.08),
        ha="center",
        fontsize=8,
        color="0.35",
    )
    _style_axes(
        ax_gap,
        r"Not convex: two intervals",
    )
    ax_gap.legend(
        loc="upper left",
        fontsize=8,
        frameon=False,
    )

    out = OUT_DIR / "brouwer_compact_convex_fail.png"
    fig.tight_layout()
    fig.savefig(
        out,
        bbox_inches="tight",
        facecolor="white",
        pad_inches=0.12,
    )
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    make_brouwer_fixed_point_plot()
    make_brouwer_hypothesis_failures()
