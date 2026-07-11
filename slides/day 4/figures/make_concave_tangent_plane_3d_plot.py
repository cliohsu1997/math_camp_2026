"""Concave surface in 3D lying below a tangent plane."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

DARK_TEAL = "#23373B"
PLANE_COLOR = "#E74C3C"
OUT_DIR = Path(__file__).resolve().parent


def f(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return 3.0 - (x - 1.0) ** 2 - (y - 1.0) ** 2


def grad(x0: float, y0: float) -> tuple[float, float]:
    fx = -2.0 * (x0 - 1.0)
    fy = -2.0 * (y0 - 1.0)
    return fx, fy


def tangent_plane(
    x: np.ndarray,
    y: np.ndarray,
    x0: float,
    y0: float,
) -> np.ndarray:
    z0 = f(x0, y0)
    fx, fy = grad(x0, y0)
    return z0 + fx * (x - x0) + fy * (y - y0)


def main() -> None:
    x0, y0 = 0.35, 0.75
    z0 = f(x0, y0)

    pad = 0.55
    x_grid = np.linspace(1.0 - pad, 1.0 + pad, 60)
    y_grid = np.linspace(1.0 - pad, 1.0 + pad, 60)
    X, Y = np.meshgrid(x_grid, y_grid)
    Z = f(X, Y)
    Z_plane = tangent_plane(X, Y, x0, y0)

    fig = plt.figure(figsize=(6.8, 5.0), dpi=220)
    ax = fig.add_subplot(111, projection="3d")

    ax.plot_surface(
        X,
        Y,
        Z,
        cmap=cm.viridis,
        alpha=0.55,
        linewidth=0,
        antialiased=True,
        rstride=2,
        cstride=2,
    )
    ax.plot_surface(
        X,
        Y,
        Z_plane,
        color=PLANE_COLOR,
        alpha=0.28,
        linewidth=0,
        antialiased=True,
        rstride=2,
        cstride=2,
    )

    ax.scatter(
        [x0],
        [y0],
        [z0],
        color="white",
        edgecolors=PLANE_COLOR,
        s=55,
        zorder=6,
    )

    ax.set_xlabel(r"$x$", fontsize=10, labelpad=0)
    ax.set_ylabel(r"$y$", fontsize=10, labelpad=0)
    ax.set_zlabel(r"$z=f(x,y)$", fontsize=10, labelpad=0)
    ax.tick_params(labelsize=8)
    ax.view_init(elev=30, azim=-52)
    ax.set_box_aspect((1.0, 1.0, 0.62))
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

    out = OUT_DIR / "concave_tangent_plane_3d.png"
    fig.subplots_adjust(left=0.0, right=1.0, top=1.0, bottom=0.0)
    fig.savefig(
        out,
        bbox_inches="tight",
        pad_inches=0.04,
        facecolor="white",
    )
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
