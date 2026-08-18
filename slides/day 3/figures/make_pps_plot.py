"""Producer-theory figures: technology, isoprofit, shifts, tangency."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"
FILL_ALPHA = 0.12
OUT_DIR = Path(__file__).resolve().parent

P1 = 1.0
P2 = 2.0
LABOR_STAR = 4.0
PI_STAR = 4.0


def production_output(
    labor: np.ndarray,
) -> np.ndarray:
    """y2 = f(L) with f(L) = 2 sqrt(L)."""
    return 2.0 * np.sqrt(
        np.clip(
            labor,
            0.0,
            None,
        )
    )


def _frontier_arrays() -> tuple[np.ndarray, np.ndarray]:
    labor = np.linspace(
        0.0,
        6.5,
        400,
    )
    y1 = -labor
    y2 = production_output(labor)
    return y1, y2


def _star_point() -> tuple[float, float]:
    y1_star = -LABOR_STAR
    y2_star = float(
        production_output(
            np.array([LABOR_STAR])
        )[0]
    )
    return y1_star, y2_star


def _draw_pps(
    ax: plt.Axes,
) -> None:
    y1, y2_frontier = _frontier_arrays()
    verts = np.column_stack(
        [
            y1,
            y2_frontier,
        ]
    )
    lower = np.column_stack(
        [
            y1[::-1],
            np.zeros_like(y1),
        ]
    )
    region = np.vstack(
        [
            verts,
            lower,
        ]
    )
    ax.add_patch(
        Polygon(
            region,
            closed=True,
            facecolor=DARK_TEAL,
            edgecolor="none",
            alpha=FILL_ALPHA,
            zorder=1,
        )
    )
    ax.plot(
        y1,
        y2_frontier,
        color=DARK_TEAL,
        linewidth=2.8,
        zorder=3,
        label=r"frontier $y_2=2\sqrt{-y_1}$",
    )
    ax.annotate(
        "Y",
        xy=(
            -4.8,
            1.05,
        ),
        fontsize=14,
        color=DARK_TEAL,
        ha="center",
        va="center",
    )


def _isoprofit_line(
    ax: plt.Axes,
    pi: float,
    color: str,
    linestyle: str,
    linewidth: float,
    label: str,
) -> None:
    y1_line = np.linspace(
        -7.5,
        1.2,
        200,
    )
    y2_line = (
        pi
        - P1 * y1_line
    ) / P2
    ax.plot(
        y1_line,
        y2_line,
        color=color,
        linewidth=linewidth,
        linestyle=linestyle,
        zorder=4,
        label=label,
    )


def _style_axes(
    ax: plt.Axes,
    title: str,
) -> None:
    ax.axhline(
        0.0,
        color="0.4",
        linewidth=1.0,
        zorder=2,
    )
    ax.axvline(
        0.0,
        color="0.4",
        linewidth=1.0,
        zorder=2,
    )
    ax.set_xlim(
        -7.8,
        1.6,
    )
    ax.set_ylim(
        -0.5,
        6.0,
    )
    ax.set_xlabel(
        r"input $y_1\leq 0$",
        fontsize=12,
        color=DARK_TEAL,
    )
    ax.set_ylabel(
        r"output $y_2\geq 0$",
        fontsize=12,
        color=DARK_TEAL,
    )
    ax.set_title(
        title,
        fontsize=12,
        color=DARK_TEAL,
        pad=10,
    )
    ax.tick_params(
        labelsize=9,
        colors=DARK_TEAL,
    )
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(DARK_TEAL)
    ax.spines["bottom"].set_color(DARK_TEAL)
    ax.grid(
        True,
        alpha=0.2,
        linewidth=0.6,
    )


def _save(
    fig: plt.Figure,
    name: str,
) -> None:
    out = OUT_DIR / name
    fig.subplots_adjust(
        left=0.12,
        right=0.97,
        bottom=0.14,
        top=0.90,
    )
    fig.savefig(
        out,
        bbox_inches="tight",
        facecolor="white",
        pad_inches=0.12,
    )
    plt.close(fig)
    print(
        f"Wrote {out}"
    )


def make_technology_plot() -> None:
    fig, ax = plt.subplots(
        figsize=(6.4, 5.0),
        dpi=220,
    )
    _draw_pps(ax)
    _style_axes(
        ax,
        "Technology: feasible plans $Y$",
    )
    ax.legend(
        loc="upper left",
        frameon=False,
        fontsize=9,
    )
    _save(
        fig,
        "pps_technology.png",
    )


def make_one_isoprofit_plot() -> None:
    fig, ax = plt.subplots(
        figsize=(6.4, 5.0),
        dpi=220,
    )
    specs = [
        (
            0.0,
            "#C4A574",
            ":",
            1.8,
            r"$\pi=0$",
        ),
        (
            2.0,
            "#E0A15A",
            "--",
            2.1,
            r"$\pi=2$",
        ),
        (
            4.0,
            ACCENT,
            "--",
            2.5,
            r"$\pi=4$",
        ),
        (
            6.0,
            "#9A3B12",
            "-.",
            2.1,
            r"$\pi=6$",
        ),
    ]
    for (
        pi,
        color,
        style,
        width,
        label,
    ) in specs:
        _isoprofit_line(
            ax,
            pi,
            color,
            style,
            width,
            label,
        )
        intercept = pi / P2
        ax.plot(
            0.0,
            intercept,
            "o",
            color=color,
            markersize=7,
            zorder=6,
            markeredgecolor="white",
            markeredgewidth=1.2,
        )
    ax.annotate(
        "higher profit",
        xy=(
            0.05,
            3.15,
        ),
        xytext=(
            0.15,
            4.55,
        ),
        fontsize=10,
        color=ACCENT,
        arrowprops={
            "arrowstyle": "->",
            "color": ACCENT,
            "lw": 1.2,
        },
    )
    _style_axes(
        ax,
        r"Isoprofit family: $y_1+2y_2=\pi$ (no technology yet)",
    )
    ax.legend(
        loc="upper left",
        frameon=False,
        fontsize=9,
    )
    _save(
        fig,
        "pps_isoprofit.png",
    )


def make_isoprofit_shift_plot() -> None:
    fig, ax = plt.subplots(
        figsize=(6.4, 5.0),
        dpi=220,
    )
    _draw_pps(ax)
    specs = [
        (
            0.0,
            "#C4A574",
            ":",
            1.8,
            r"$\pi=0$",
        ),
        (
            2.0,
            "#E0A15A",
            "--",
            2.1,
            r"$\pi=2$",
        ),
        (
            4.0,
            ACCENT,
            "--",
            2.5,
            r"$\pi=4$",
        ),
        (
            6.0,
            "#9A3B12",
            "-.",
            2.1,
            r"$\pi=6$ (not in $Y$)",
        ),
    ]
    for (
        pi,
        color,
        style,
        width,
        label,
    ) in specs:
        _isoprofit_line(
            ax,
            pi,
            color,
            style,
            width,
            label,
        )
    ax.annotate(
        "higher profit",
        xy=(
            0.05,
            3.15,
        ),
        xytext=(
            0.15,
            4.55,
        ),
        fontsize=10,
        color=ACCENT,
        arrowprops={
            "arrowstyle": "->",
            "color": ACCENT,
            "lw": 1.2,
        },
    )
    _style_axes(
        ax,
        "Parallel isoprofits: higher intercept means higher $\\pi$",
    )
    ax.legend(
        loc="upper left",
        frameon=False,
        fontsize=8,
    )
    _save(
        fig,
        "pps_isoprofit_shift.png",
    )


def _draw_slope_triangle(
    ax: plt.Axes,
    y1_star: float,
    y2_star: float,
) -> None:
    dy1 = -2.0
    dy2 = 1.0
    x_end = y1_star + dy1
    y_end = y2_star + dy2
    ax.plot(
        [
            y1_star,
            x_end,
        ],
        [
            y2_star,
            y2_star,
        ],
        color="0.45",
        linewidth=1.4,
        zorder=5,
    )
    ax.plot(
        [
            x_end,
            x_end,
        ],
        [
            y2_star,
            y_end,
        ],
        color="0.45",
        linewidth=1.4,
        zorder=5,
    )
    ax.annotate(
        r"$\Delta y_1$",
        xy=(
            y1_star + 0.5 * dy1,
            y2_star - 0.28,
        ),
        fontsize=9,
        color="0.35",
        ha="center",
    )
    ax.annotate(
        r"$\Delta y_2$",
        xy=(
            x_end - 0.35,
            y2_star + 0.5 * dy2,
        ),
        fontsize=9,
        color="0.35",
        ha="right",
        va="center",
    )


def make_tangency_plot() -> None:
    fig, ax = plt.subplots(
        figsize=(6.4, 5.0),
        dpi=220,
    )
    _draw_pps(ax)
    _isoprofit_line(
        ax,
        PI_STAR,
        ACCENT,
        "--",
        2.5,
        r"isoprofit $y_1+2y_2=4$",
    )
    y1_star, y2_star = _star_point()
    intercept = PI_STAR / P2
    _draw_slope_triangle(
        ax,
        y1_star,
        y2_star,
    )
    ax.plot(
        y1_star,
        y2_star,
        "o",
        color=ACCENT,
        markersize=10,
        zorder=6,
        markeredgecolor="white",
        markeredgewidth=2.0,
    )
    ax.plot(
        0.0,
        intercept,
        "o",
        color=ACCENT,
        markersize=8,
        zorder=6,
        markeredgecolor="white",
        markeredgewidth=1.5,
    )
    ax.annotate(
        r"$y^*=(-4,4)$",
        xy=(
            y1_star,
            y2_star,
        ),
        xytext=(
            -1.5,
            5.25,
        ),
        fontsize=11,
        color=ACCENT,
        arrowprops={
            "arrowstyle": "->",
            "color": ACCENT,
            "lw": 1.2,
        },
    )
    ax.annotate(
        r"$\pi/p_2=2$",
        xy=(
            0.0,
            intercept,
        ),
        xytext=(
            0.25,
            intercept + 1.05,
        ),
        fontsize=10,
        color=ACCENT,
    )
    _style_axes(
        ax,
        "Profit-maximizing plan: highest isoprofit that meets $Y$",
    )
    ax.legend(
        loc="upper left",
        frameon=False,
        fontsize=9,
    )
    _save(
        fig,
        "pps_tangency.png",
    )


def make_slope_match_plot() -> None:
    fig, ax = plt.subplots(
        figsize=(6.4, 5.0),
        dpi=220,
    )
    _draw_pps(ax)
    _isoprofit_line(
        ax,
        PI_STAR,
        ACCENT,
        "--",
        2.5,
        r"isoprofit slope $-p_1/p_2$",
    )
    y1_star, y2_star = _star_point()
    _draw_slope_triangle(
        ax,
        y1_star,
        y2_star,
    )
    ax.plot(
        y1_star,
        y2_star,
        "o",
        color=ACCENT,
        markersize=10,
        zorder=6,
        markeredgecolor="white",
        markeredgewidth=2.0,
    )
    ax.annotate(
        r"$y^*$",
        xy=(
            y1_star,
            y2_star,
        ),
        xytext=(
            -2.4,
            5.15,
        ),
        fontsize=11,
        color=ACCENT,
        arrowprops={
            "arrowstyle": "->",
            "color": ACCENT,
            "lw": 1.2,
        },
    )
    ax.annotate(
        r"slope $= -1/2 = -p_1/p_2$",
        xy=(
            -5.6,
            4.55,
        ),
        fontsize=10,
        color=ACCENT,
    )
    _style_axes(
        ax,
        r"Tangency: MRT $= p_1/p_2$",
    )
    ax.legend(
        loc="upper left",
        frameon=False,
        fontsize=9,
    )
    _save(
        fig,
        "pps_slope_match.png",
    )


if __name__ == "__main__":
    make_technology_plot()
    make_one_isoprofit_plot()
    make_isoprofit_shift_plot()
    make_tangency_plot()
    make_slope_match_plot()
