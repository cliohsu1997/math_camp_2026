"""IFT regularity condition figure for Day 2 section 2.1."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"


def _style_axis(ax: plt.Axes) -> None:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_xlabel(r"$x$", fontsize=11)
    ax.set_ylabel(r"$y$", fontsize=11)
    ax.tick_params(labelsize=9)


def _plot_good_case(ax: plt.Axes) -> None:
    """F = x + y - 1: nonzero slope, IFT applies."""
    x = np.linspace(-0.05, 2.05, 200)
    y = 1.0 - x
    x0, y0 = 0.8, 0.2
    slope = -1.0
    x_tan = np.linspace(x0 - 0.35, x0 + 0.35, 2)
    y_tan = y0 + slope * (x_tan - x0)

    ax.plot(x, y, color=DARK_TEAL, linewidth=2.4, zorder=3)
    ax.plot(
        x_tan,
        y_tan,
        linestyle="--",
        color=ACCENT,
        linewidth=1.8,
        zorder=2,
        label="tangent",
    )
    ax.plot(x0, y0, "o", color=DARK_TEAL, markersize=7, zorder=4)
    ax.annotate(
        r"$(x_0,y_0)$",
        xy=(x0, y0),
        xytext=(x0 + 0.10, y0 + 0.20),
        fontsize=9,
        color=DARK_TEAL,
    )
    ax.text(
        1.05,
        -0.42,
        r"$F_y=1\neq 0$:" + "\n" + r"finite slope $\frac{dy}{dx}=-1$",
        fontsize=9,
        ha="center",
        color=DARK_TEAL,
    )
    ax.set_title(
        r"$F(x,y)=x+y-1=0$",
        fontsize=10,
        color=DARK_TEAL,
    )
    ax.set_xlim(-0.15, 2.25)
    ax.set_ylim(-0.55, 1.35)
    _style_axis(ax)


def _plot_bad_case(ax: plt.Axes) -> None:
    """F = x - y^2: at (0,0), F_y=0 and the tangent is vertical."""
    y = np.linspace(-0.85, 0.85, 200)
    x = y ** 2
    y0 = 0.0
    y_tan = np.linspace(-0.75, 0.75, 2)
    x_tan = np.zeros_like(y_tan)

    ax.plot(x, y, color=ACCENT, linewidth=2.4, zorder=3)
    ax.plot(
        x_tan,
        y_tan,
        linestyle="--",
        color=DARK_TEAL,
        linewidth=1.8,
        zorder=2,
    )
    ax.plot(0.0, y0, "o", color=ACCENT, markersize=7, zorder=4)
    ax.annotate(
        r"$(0,0)$",
        xy=(0.0, 0.0),
        xytext=(0.14, -0.28),
        fontsize=9,
        color=ACCENT,
    )
    ax.text(
        0.62,
        -0.72,
        r"$F_y=0$ at origin:" + "\n"
        + "vertical tangent," + "\n"
        + r"$\frac{dy}{dx}=-F_x/F_y$ undefined",
        fontsize=9,
        ha="center",
        color=DARK_TEAL,
    )
    ax.set_title(
        r"$F(x,y)=x-y^2=0$",
        fontsize=10,
        color=ACCENT,
    )
    ax.set_xlim(-0.08, 0.95)
    ax.set_ylim(-0.95, 0.95)
    _style_axis(ax)


def make_ift_regularity_plot() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.8), dpi=220)

    _plot_good_case(axes[0])
    _plot_bad_case(axes[1])

    fig.suptitle(
        "Why the IFT needs $F_y \\neq 0$",
        fontsize=12,
        color=DARK_TEAL,
        y=1.02,
    )
    fig.tight_layout()

    out = Path(__file__).resolve().parent / "ift_regularity_condition.png"
    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    make_ift_regularity_plot()
