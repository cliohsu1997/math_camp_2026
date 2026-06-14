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


def _f_xy_rational(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    denom = x**2 + y**2
    return np.where(denom > 1e-14, x * y / denom, 0.0)


def make_partials_not_enough_plot() -> None:
    """Graph of f(x,y)=xy/(x^2+y^2): partials at (0,0) but no tangent plane."""
    from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

    pad = 0.85
    n = 120
    x_grid = np.linspace(-pad, pad, n)
    y_grid = np.linspace(-pad, pad, n)
    X, Y = np.meshgrid(x_grid, y_grid)
    Z = _f_xy_rational(X, Y)

    t_pos = np.linspace(0.08, pad, 80)
    t_neg = np.linspace(-pad, -0.08, 80)
    t_full = np.concatenate([t_neg, t_pos])

    z_diag = _f_xy_rational(t_full, t_full)
    z_axis = np.zeros_like(t_full)

    fig = plt.figure(figsize=(6.4, 5.2), dpi=220)
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(
        X,
        Y,
        Z,
        cmap="coolwarm",
        alpha=0.78,
        linewidth=0,
        antialiased=True,
        rstride=2,
        cstride=2,
    )

    # Candidate plane from partials: f_x(0,0)=f_y(0,0)=0 => z=0
    plane_x = np.linspace(-pad, pad, 2)
    plane_y = np.linspace(-pad, pad, 2)
    PX, PY = np.meshgrid(plane_x, plane_y)
    PZ = np.zeros_like(PX)
    ax.plot_surface(
        PX,
        PY,
        PZ,
        color="0.85",
        alpha=0.35,
        linewidth=0,
        shade=False,
    )

    ax.plot(
        t_full,
        t_full,
        z_diag,
        color=ACCENT,
        linewidth=2.8,
        label=r"$y=x$",
    )
    ax.plot(
        t_full,
        np.zeros_like(t_full),
        z_axis,
        color=DARK_TEAL,
        linewidth=2.8,
        label=r"$y=0$",
    )
    ax.scatter([0.0], [0.0], [0.0], color="white", edgecolors=DARK_TEAL, s=42, zorder=6)

    ax.set_xlim(-pad, pad)
    ax.set_ylim(-pad, pad)
    ax.set_zlim(-0.65, 0.65)
    ax.set_xlabel(r"$x$", fontsize=9, labelpad=0)
    ax.set_ylabel(r"$y$", fontsize=9, labelpad=0)
    ax.set_zlabel(r"$z$", fontsize=9, labelpad=2)
    ax.set_title(
        r"$f(x,y)=\frac{xy}{x^2+y^2}$, $f(0,0)=0$",
        fontsize=10,
        color=DARK_TEAL,
        pad=10,
    )
    ax.view_init(elev=28, azim=-52)
    ax.tick_params(labelsize=7)

    out = OUT_DIR / "partials_not_differentiable.png"
    fig.subplots_adjust(left=0.0, right=1.0, bottom=0.0, top=1.0)
    fig.savefig(out, bbox_inches="tight", facecolor="white", pad_inches=0.08)
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    make_abs_corner_plot()
    make_weierstrass_plot()
    make_partials_not_enough_plot()
