"""One-dimensional quasiconcave function showing the segment inequality."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

DARK_TEAL = "#23373B"
CHORD = "#EB811B"
POINT1 = "#E74C3C"
POINT2 = "#27AE60"
MIDPOINT = "#8E44AD"
OUT_DIR = Path(__file__).resolve().parent


def f(x):
    """Single-peaked quasiconcave function that is not concave."""
    return 2 - np.sqrt(np.abs(x))


def main():
    fig, ax = plt.subplots(
        figsize=(8, 4.5),
        dpi=220,
    )

    grid = np.linspace(
        -2.2,
        2.2,
        500,
    )
    values = f(grid)

    ax.plot(
        grid,
        values,
        color=DARK_TEAL,
        lw=2.5,
        zorder=3,
    )

    # Choose endpoints with different heights.
    x_val = -1.70
    y_val = 0.80
    lam = 0.55
    z_val = (
        lam * x_val
        + (1 - lam) * y_val
    )

    f_x = f(x_val)
    f_y = f(y_val)
    f_z = f(z_val)
    chord_z = (
        lam * f_x
        + (1 - lam) * f_y
    )
    min_f = min(f_x, f_y)

    # Endpoints and chord.
    ax.plot(
        [x_val, y_val],
        [f_x, f_y],
        "--",
        color=CHORD,
        lw=2,
        zorder=2,
    )
    ax.plot(
        x_val,
        f_x,
        "o",
        color=POINT1,
        ms=9,
        zorder=5,
    )
    ax.text(
        x_val - 0.28,
        f_x + 0.06,
        r"$f(x)$",
        fontsize=11,
        color=POINT1,
        fontweight="bold",
    )
    ax.plot(
        y_val,
        f_y,
        "o",
        color=POINT2,
        ms=9,
        zorder=5,
    )
    ax.text(
        y_val + 0.08,
        f_y + 0.04,
        r"$f(y)$",
        fontsize=11,
        color=POINT2,
        fontweight="bold",
    )

    # Peak.
    ax.plot(
        0,
        f(0),
        "*",
        color=DARK_TEAL,
        ms=13,
        zorder=6,
    )
    ax.text(
        0.08,
        f(0) + 0.02,
        r"$x^*$",
        fontsize=12,
        color=DARK_TEAL,
        fontweight="bold",
    )

    # Point z = lambda x + (1-lambda)y on the curve and on the chord.
    ax.plot(
        z_val,
        f_z,
        "s",
        color=MIDPOINT,
        ms=8,
        zorder=6,
    )
    ax.plot(
        z_val,
        chord_z,
        "o",
        color=CHORD,
        ms=7,
        zorder=6,
    )
    ax.plot(
        [z_val, z_val],
        [chord_z, f_z],
        ":",
        color="gray",
        lw=1.5,
        zorder=1,
    )
    ax.annotate(
        r"$\lambda f(x)+(1-\lambda)f(y)$",
        xy=(
            z_val,
            chord_z,
        ),
        xytext=(
            1.10,
            1.75,
        ),
        fontsize=10,
        color=CHORD,
        fontweight="bold",
        arrowprops=dict(
            arrowstyle="->",
            color=CHORD,
            lw=1.2,
        ),
        bbox=dict(
            facecolor="white",
            edgecolor="none",
            alpha=0.85,
            pad=1.5,
        ),
    )

    # Quasiconcavity lower bound.
    ax.axhline(
        min_f,
        color="#555555",
        lw=1.3,
        ls="-.",
        alpha=0.7,
    )
    ax.annotate(
        r"$\min\{f(x),f(y)\}$",
        xy=(
            1.75,
            min_f,
        ),
        xytext=(
            1.05,
            0.22,
        ),
        fontsize=10,
        color="#555555",
        arrowprops=dict(
            arrowstyle="->",
            color="#555555",
            lw=1.0,
        ),
        bbox=dict(
            facecolor="white",
            edgecolor="none",
            alpha=0.85,
            pad=1.5,
        ),
    )
    ax.set_xlim(
        -2.2,
        2.2,
    )
    ax.set_ylim(
        -0.12,
        2.20,
    )
    ax.set_xlabel(r"$x$", fontsize=11)
    ax.set_ylabel(r"$f(x)$", fontsize=11)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    out = OUT_DIR / "quasiconcave_1d.png"
    fig.tight_layout()
    fig.savefig(
        out,
        bbox_inches="tight",
        facecolor="white",
        pad_inches=0.1,
    )
    plt.close()
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
