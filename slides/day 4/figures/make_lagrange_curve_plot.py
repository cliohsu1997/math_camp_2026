"""3D surface with equality constraint curve for Lagrange geometry."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"
OUT_DIR = Path(__file__).resolve().parent


def main() -> None:
    x = np.linspace(-0.5, 2.5, 80)
    y = np.linspace(-0.5, 2.5, 80)
    X, Y = np.meshgrid(x, y)
    Z = -(X - 1.0) ** 2 - (Y - 1.0) ** 2 + 3.0

    theta = np.linspace(0.0, 2.0 * np.pi, 200)
    xc = 1.0 + np.cos(theta)
    yc = 1.0 + np.sin(theta)
    zc = -(xc - 1.0) ** 2 - (yc - 1.0) ** 2 + 3.0

    fig = plt.figure(figsize=(6.2, 4.8), dpi=200)
    ax = fig.add_subplot(111, projection="3d")

    ax.plot_surface(
        X,
        Y,
        Z,
        cmap=cm.viridis,
        alpha=0.78,
        linewidth=0,
        antialiased=True,
        rstride=2,
        cstride=2,
    )
    ax.plot(
        xc,
        yc,
        zc,
        color=ACCENT,
        linewidth=3.0,
        label=r"$h(x,y)=0$",
    )

    z_base = Z.min() - 0.15
    ax.plot(
        xc,
        yc,
        np.full_like(xc, z_base),
        color=DARK_TEAL,
        linewidth=1.8,
        linestyle="--",
        alpha=0.7,
    )

    ax.set_xlabel(r"$x$", fontsize=9, labelpad=2)
    ax.set_ylabel(r"$y$", fontsize=9, labelpad=2)
    ax.set_zlabel(r"$z=f(x,y)$", fontsize=9, labelpad=2)
    ax.set_title(
        r"$f=-(x-1)^2-(y-1)^2+3$ with $h(x,y)=(x-1)^2+(y-1)^2-1=0$",
        fontsize=10,
        color=DARK_TEAL,
        pad=10,
    )
    ax.view_init(elev=28, azim=-58)
    ax.tick_params(labelsize=7)

    out = OUT_DIR / "lagrange_curve_3d.png"
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
