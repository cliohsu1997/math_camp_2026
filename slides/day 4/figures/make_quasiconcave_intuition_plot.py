"""Quasiconcave upper contour sets as a filled equal-height map."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

DARK_TEAL = "#23373B"
BLUE = "#2E86C1"
OUT_DIR = Path(__file__).resolve().parent


def main():
    fig, ax = plt.subplots(
        figsize=(6.5, 5),
        dpi=220,
    )

    x_grid = np.linspace(
        0,
        3,
        240,
    )
    y_grid = np.linspace(
        0,
        3,
        240,
    )
    x_mesh, y_mesh = np.meshgrid(
        x_grid,
        y_grid,
    )

    # Hill-shaped quasiconcave function. Upper contour sets are disks.
    center = np.array(
        [
            1.5,
            1.5,
        ]
    )
    z_mesh = np.exp(
        -(
            (x_mesh - center[0]) ** 2
            + (y_mesh - center[1]) ** 2
        )
        / 0.75
    )

    levels = [
        0.10,
        0.25,
        0.40,
        0.55,
        0.70,
        0.85,
        1.00,
    ]
    ax.contourf(
        x_mesh,
        y_mesh,
        z_mesh,
        levels=levels,
        cmap="Blues",
        alpha=0.90,
        zorder=1,
    )
    contours = ax.contour(
        x_mesh,
        y_mesh,
        z_mesh,
        levels=levels[1:-1],
        colors=BLUE,
        linewidths=1.3,
        zorder=2,
    )
    ax.clabel(
        contours,
        inline=True,
        fontsize=8,
        fmt=r"$f=%.2g$",
    )

    # Two points in the same upper contour set S_0.55, with segment inside it.
    point_x = np.array(
        [
            1.00,
            1.35,
        ]
    )
    point_y = np.array(
        [
            1.95,
            1.60,
        ]
    )
    segment = np.linspace(
        point_x,
        point_y,
        80,
    )
    midpoint = (
        0.5 * point_x
        + 0.5 * point_y
    )

    ax.plot(
        segment[:, 0],
        segment[:, 1],
        "--",
        color="black",
        lw=2.2,
        zorder=5,
    )
    ax.plot(
        point_x[0],
        point_x[1],
        "o",
        color=DARK_TEAL,
        ms=8,
        zorder=6,
    )
    ax.text(
        point_x[0] - 0.23,
        point_x[1] - 0.13,
        r"$\mathbf{x}$",
        fontsize=11,
        color=DARK_TEAL,
        fontweight="bold",
    )
    ax.plot(
        point_y[0],
        point_y[1],
        "o",
        color=DARK_TEAL,
        ms=8,
        zorder=6,
    )
    ax.text(
        point_y[0] + 0.08,
        point_y[1] + 0.04,
        r"$\mathbf{y}$",
        fontsize=11,
        color=DARK_TEAL,
        fontweight="bold",
    )
    ax.plot(
        midpoint[0],
        midpoint[1],
        "s",
        color="#E74C3C",
        ms=7,
        zorder=6,
    )

    # Keep the defining set away from the figure center.
    ax.text(
        0.10,
        2.86,
        r"$S_t=\{\mathbf{x}: f(\mathbf{x})\geq t\}$",
        fontsize=10,
        color=DARK_TEAL,
        bbox=dict(
            facecolor="white",
            edgecolor="none",
            alpha=0.85,
            pad=2.0,
        ),
        zorder=7,
    )

    ax.set_xlim(
        0,
        3,
    )
    ax.set_ylim(
        0,
        3,
    )
    ax.set_xlabel(r"$x_1$", fontsize=11)
    ax.set_ylabel(r"$x_2$", fontsize=11)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_aspect("equal")

    out = OUT_DIR / "quasiconcave_intuition.png"
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
