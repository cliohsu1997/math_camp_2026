"""Concave and convex functions with chords — dual panel."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

DARK_TEAL = "#23373B"
CHORD_COLOR = "#C0392B"
ENDPOINT_COLOR = "#2980B9"
MID_CURVE_COLOR = "#27AE60"
MID_CHORD_COLOR = "#E67E22"
CHORD_LABEL = r"$\lambda f(x) + (1-\lambda)f(y)$"
CURVE_LABEL = r"$f(\lambda x + (1-\lambda)y)$"
OUT_DIR = Path(__file__).resolve().parent


def concave_y(x: np.ndarray) -> np.ndarray:
    return -0.8 * (x - 0.5) ** 2 + 2.0


def convex_y(x: np.ndarray) -> np.ndarray:
    return 0.6 * (x - 0.8) ** 2 + 0.5


def add_chord_label(ax, x_left, y_left, x_right, y_right) -> None:
    x_label = 0.55 * x_left + 0.45 * x_right
    y_label = 0.55 * y_left + 0.45 * y_right
    ax.annotate(
        CHORD_LABEL,
        xy=(x_label, y_label),
        xytext=(8, -16),
        textcoords="offset points",
        fontsize=9,
        color=CHORD_COLOR,
        ha="left",
        va="top",
    )


def plot_concave_chord(ax) -> None:
    x_grid = np.linspace(-1.5, 2.5, 400)
    ax.plot(x_grid, concave_y(x_grid), color=DARK_TEAL, lw=2.5, zorder=3)

    x_left = -0.8
    x_right = 1.8
    lam = 0.5
    x_mid = lam * x_left + (1.0 - lam) * x_right

    y_left = concave_y(x_left)
    y_right = concave_y(x_right)
    y_mid = concave_y(x_mid)
    y_chord_mid = lam * y_left + (1.0 - lam) * y_right

    ax.plot(
        [x_left, x_right],
        [y_left, y_right],
        color=CHORD_COLOR,
        lw=2.0,
        ls="--",
        zorder=2,
    )
    ax.plot(x_left, y_left, "o", color=ENDPOINT_COLOR, ms=7, zorder=4)
    ax.plot(x_right, y_right, "o", color=ENDPOINT_COLOR, ms=7, zorder=4)
    ax.plot(x_mid, y_mid, "o", color=MID_CURVE_COLOR, ms=7, zorder=5)
    ax.plot(
        x_mid,
        y_chord_mid,
        "o",
        color=MID_CHORD_COLOR,
        ms=7,
        fillstyle="none",
        markeredgewidth=2.0,
        zorder=5,
    )
    ax.vlines(x_mid, y_chord_mid, y_mid, color=MID_CURVE_COLOR, lw=1.5, ls=":", zorder=4)
    add_chord_label(ax, x_left, y_left, x_right, y_right)
    ax.annotate(
        CURVE_LABEL,
        xy=(x_mid, y_mid),
        xytext=(10, 8),
        textcoords="offset points",
        fontsize=9,
        color=MID_CURVE_COLOR,
        ha="left",
        va="bottom",
    )
    ax.set_title("Concave", fontsize=11, fontweight="bold", color=DARK_TEAL, pad=6)
    style_axis(ax)


def plot_convex_chord(ax) -> None:
    x_grid = np.linspace(-1.5, 2.5, 400)
    ax.plot(x_grid, convex_y(x_grid), color=DARK_TEAL, lw=2.5, zorder=3)

    x_left = -0.4
    x_right = 2.0
    lam = 0.5
    x_mid = lam * x_left + (1.0 - lam) * x_right

    y_left = convex_y(x_left)
    y_right = convex_y(x_right)
    y_mid = convex_y(x_mid)
    y_chord_mid = lam * y_left + (1.0 - lam) * y_right

    ax.plot(
        [x_left, x_right],
        [y_left, y_right],
        color=CHORD_COLOR,
        lw=2.0,
        ls="--",
        zorder=2,
    )
    ax.plot(x_left, y_left, "o", color=ENDPOINT_COLOR, ms=7, zorder=4)
    ax.plot(x_right, y_right, "o", color=ENDPOINT_COLOR, ms=7, zorder=4)
    ax.plot(x_mid, y_mid, "o", color=MID_CURVE_COLOR, ms=7, zorder=5)
    ax.plot(
        x_mid,
        y_chord_mid,
        "o",
        color=MID_CHORD_COLOR,
        ms=7,
        fillstyle="none",
        markeredgewidth=2.0,
        zorder=5,
    )
    ax.vlines(x_mid, y_mid, y_chord_mid, color=MID_CURVE_COLOR, lw=1.5, ls=":", zorder=4)
    add_chord_label(ax, x_left, y_left, x_right, y_right)
    ax.annotate(
        CURVE_LABEL,
        xy=(x_mid, y_mid),
        xytext=(10, -12),
        textcoords="offset points",
        fontsize=9,
        color=MID_CURVE_COLOR,
        ha="left",
        va="top",
    )
    ax.set_title("Convex", fontsize=11, fontweight="bold", color=DARK_TEAL, pad=6)
    style_axis(ax)


def style_axis(ax) -> None:
    ax.set_xlim(-1.5, 2.5)
    ax.set_ylim(0, 3)
    ax.set_xlabel(r"$x$", fontsize=10)
    ax.set_ylabel(r"$f(x)$", fontsize=10)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=8)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(9.5, 3.6), dpi=220)

    plot_concave_chord(axes[0])
    plot_convex_chord(axes[1])

    out = OUT_DIR / "concave_chords.png"
    fig.tight_layout()
    fig.savefig(
        out,
        bbox_inches="tight",
        facecolor="white",
        pad_inches=0.08,
    )
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
