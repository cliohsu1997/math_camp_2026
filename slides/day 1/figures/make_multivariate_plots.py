"""Contour gradient and tangent-plane figures for Day 1 section 1.8."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"


def f(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return 2.0 * np.exp(-0.35 * (x**2 + y**2)) + 0.25


def grad(x: float, y: float) -> tuple[float, float]:
    expo = np.exp(-0.35 * (x**2 + y**2))
    fx = -1.4 * x * expo
    fy = -1.4 * y * expo
    return fx, fy


def make_gradient_contour_plot() -> None:
    x = np.linspace(-2.0, 2.0, 200)
    y = np.linspace(-2.0, 2.0, 200)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    x0, y0 = 0.85, 0.55
    fx0, fy0 = grad(x0, y0)
    g = np.array([fx0, fy0])
    g_norm = np.linalg.norm(g)
    g_unit = g / g_norm

    # Tangent to level curve: perpendicular to gradient in the plane
    tangent = np.array([-fy0, fx0])
    tangent = tangent / np.linalg.norm(tangent)

    fig, ax = plt.subplots(figsize=(5.4, 4.8), dpi=220)
    levels = np.linspace(0.45, 2.05, 10)
    ax.contour(X, Y, Z, levels=levels, colors="0.55", linewidths=0.9)
    c_val = f(x0, y0)
    ax.contour(
        X,
        Y,
        Z,
        levels=[c_val],
        colors=[ACCENT],
        linewidths=2.2,
    )

    scale_g = 0.72
    scale_t = 0.55
    ax.add_patch(
        FancyArrowPatch(
            (x0, y0),
            (x0 + scale_g * g_unit[0], y0 + scale_g * g_unit[1]),
            arrowstyle="-|>",
            mutation_scale=12,
            linewidth=2.4,
            color=DARK_TEAL,
            zorder=5,
        )
    )
    ax.plot(
        [
            x0 - scale_t * tangent[0],
            x0 + scale_t * tangent[0],
        ],
        [
            y0 - scale_t * tangent[1],
            y0 + scale_t * tangent[1],
        ],
        color=ACCENT,
        linewidth=2.0,
        linestyle="--",
        zorder=4,
    )
    ax.plot(x0, y0, "o", color="white", markersize=7, markeredgecolor=DARK_TEAL, zorder=6)
    ax.annotate(
        r"$P$",
        (x0, y0),
        textcoords="offset points",
        xytext=(6, 6),
        fontsize=11,
    )
    label_frac = 0.90
    ax.annotate(
        r"$\nabla f$ (uphill)",
        (
            x0 + label_frac * scale_g * g_unit[0],
            y0 + label_frac * scale_g * g_unit[1],
        ),
        textcoords="offset points",
        xytext=(-8, -10),
        fontsize=10,
        color=DARK_TEAL,
        ha="center",
    )
    ax.annotate(
        r"tangent to $\mathcal{L}_c$",
        (x0 + scale_t * tangent[0], y0 + scale_t * tangent[1]),
        textcoords="offset points",
        xytext=(5, -12),
        fontsize=9,
        color=ACCENT,
    )
    ax.annotate(
        r"$\mathcal{L}_c$",
        (1.35, 1.05),
        fontsize=10,
        color=ACCENT,
    )

    # Right-angle mark between gradient and tangent
    corner = 0.14
    v1 = corner * g_unit
    v2 = corner * tangent
    ax.plot(
        [x0 + v1[0], x0 + v1[0] + v2[0], x0 + v2[0]],
        [y0 + v1[1], y0 + v1[1] + v2[1], y0 + v2[1]],
        color="0.35",
        linewidth=1.0,
        zorder=3,
    )

    ax.set_xlabel("$x$", fontsize=11)
    ax.set_ylabel("$y$", fontsize=11)
    ax.set_aspect("equal")
    ax.set_xlim(-1.75, 1.75)
    ax.set_ylim(-1.55, 1.55)

    legend_handles = [
        Line2D([0], [0], color=DARK_TEAL, lw=2.4, label=r"$\nabla f$"),
        Line2D(
            [0],
            [0],
            color=ACCENT,
            lw=2.0,
            ls="--",
            label=r"tangent to $\mathcal{L}_c$",
        ),
        Line2D([0], [0], color=ACCENT, lw=2.2, label=r"level curve $\mathcal{L}_c$"),
    ]
    ax.legend(
        handles=legend_handles,
        loc="lower left",
        fontsize=9,
        framealpha=0.92,
        borderaxespad=0.6,
    )
    fig.subplots_adjust(left=0.10, right=0.98, top=0.96, bottom=0.12)
    fig.savefig(
        "gradient_contour.png",
        bbox_inches="tight",
        pad_inches=0.04,
        facecolor="white",
    )
    plt.close(fig)
    print("Saved gradient_contour.png")


def _box_label_3d(
    ax,
    x: float,
    y: float,
    z: float,
    text: str,
    *,
    color: str = "black",
    fontsize: float = 10,
) -> None:
    ax.text(
        x,
        y,
        z,
        text,
        fontsize=fontsize,
        color=color,
        ha="center",
        va="center",
        bbox=dict(
            boxstyle="square,pad=0.35",
            facecolor="white",
            edgecolor=color,
            linewidth=1.4,
            alpha=0.97,
        ),
        zorder=10,
    )


def _f_td(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Simple hill: easy partials at (0.5, 0.5) with f_x = f_y = -1."""
    return 2.0 - x**2 - y**2


def make_total_differential_3d_plot() -> None:
    """L-path: $(x_0,y_0)$ -> $(x_0+\\Delta x,y_0)$ along $x$, then to $(x_0+\\Delta x,y_0+\\Delta y)$ along $y$."""
    x0, y0 = 0.5, 0.5
    dx, dy = 0.2, 0.2
    z0 = _f_td(x0, y0)
    z1 = _f_td(x0 + dx, y0)
    z2 = _f_td(x0 + dx, y0 + dy)

    pad = 0.10
    x_grid = np.linspace(x0 - pad, x0 + dx + pad, 45)
    y_grid = np.linspace(y0 - pad, y0 + dy + pad, 45)
    X, Y = np.meshgrid(x_grid, y_grid)
    Z = _f_td(X, Y)

    xs = np.linspace(x0, x0 + dx, 30)
    ys = np.linspace(y0, y0 + dy, 30)
    z_floor = Z.min() - 0.08

    fig = plt.figure(figsize=(6.8, 5.6), dpi=220)
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(
        X,
        Y,
        Z,
        cmap=cm.viridis,
        alpha=0.50,
        linewidth=0,
        antialiased=True,
        rstride=2,
        cstride=2,
    )

    # xy-plane L-path: first $\Delta x$, then $\Delta y$
    ax.plot(
        [x0, x0 + dx],
        [y0, y0],
        [z_floor, z_floor],
        color="0.45",
        linewidth=1.4,
        linestyle="--",
        alpha=0.85,
    )
    ax.plot(
        [x0 + dx, x0 + dx],
        [y0, y0 + dy],
        [z_floor, z_floor],
        color="0.45",
        linewidth=1.4,
        linestyle="--",
        alpha=0.85,
    )

    # Leg 1: hold $y=y_0$, move $x_0 \to x_0+\Delta x$
    ax.plot(
        xs,
        np.full_like(xs, y0),
        _f_td(xs, y0),
        color=DARK_TEAL,
        linewidth=3.0,
    )
    # Leg 2: hold $x=x_0+\Delta x$, move $y_0 \to y_0+\Delta y$
    ax.plot(
        np.full_like(ys, x0 + dx),
        ys,
        _f_td(x0 + dx, ys),
        color=ACCENT,
        linewidth=3.0,
    )

    ax.scatter([x0], [y0], [z0], color="white", edgecolors=DARK_TEAL, s=58, zorder=6)
    ax.scatter([x0 + dx], [y0], [z1], color="white", edgecolors=DARK_TEAL, s=48, zorder=6)
    ax.scatter([x0 + dx], [y0 + dy], [z2], color="white", edgecolors=ACCENT, s=58, zorder=6)
    ax.scatter([x0], [y0], [z_floor], color="white", edgecolors="0.45", s=36, zorder=5)
    ax.scatter([x0 + dx], [y0 + dy], [z_floor], color="white", edgecolors="0.45", s=36, zorder=5)

    z_lbl = z_floor + 0.02

    # Shadow (floor): endpoints and steps along the dashed path
    _box_label_3d(ax, x0, y0, z_lbl, r"$(x_0,y_0)$", color="0.35", fontsize=9.5)
    _box_label_3d(ax, x0 + 0.5 * dx, y0, z_lbl, r"$\Delta x$", color=DARK_TEAL, fontsize=10)
    _box_label_3d(ax, x0 + dx, y0 + 0.5 * dy, z_lbl, r"$\Delta y$", color=ACCENT, fontsize=10)
    _box_label_3d(
        ax,
        x0 + dx,
        y0 + dy,
        z_lbl,
        r"$(x_0{+}\Delta x,y_0{+}\Delta y)$",
        color="0.35",
        fontsize=9,
    )

    # Surface: output changes on the two legs
    _box_label_3d(
        ax,
        x0 + 0.5 * dx,
        y0,
        0.5 * (z0 + z1) + 0.05,
        r"$f_x\,\Delta x$",
        color=DARK_TEAL,
        fontsize=10,
    )
    _box_label_3d(
        ax,
        x0 + dx,
        y0 + 0.5 * dy,
        0.5 * (z1 + z2) + 0.05,
        r"$f_y\,\Delta y$",
        color=ACCENT,
        fontsize=10,
    )

    ax.set_xlabel("$x$", fontsize=10, labelpad=0)
    ax.set_ylabel("$y$", fontsize=10, labelpad=0)
    ax.set_zlabel("$z$", fontsize=10, labelpad=0)
    ax.tick_params(labelsize=8)
    ax.view_init(elev=34, azim=-50)
    ax.set_box_aspect((1.0, 1.0, 0.62))
    ax.set_xlim(x0 - pad, x0 + dx + pad)
    ax.set_ylim(y0 - pad, y0 + dy + pad)
    ax.set_zlim(z_floor - 0.02, Z.max() + 0.05)
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

    fig.subplots_adjust(left=0.0, right=1.0, top=1.0, bottom=0.0)
    fig.savefig(
        "total_differential_3d.png",
        bbox_inches="tight",
        pad_inches=0.02,
        facecolor="white",
    )
    plt.close(fig)
    print("Saved total_differential_3d.png")


if __name__ == "__main__":
    make_gradient_contour_plot()
    make_total_differential_3d_plot()
