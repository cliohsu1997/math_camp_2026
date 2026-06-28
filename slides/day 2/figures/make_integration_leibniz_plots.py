"""Integration, Leibniz rule, and Fubini figures for Day 2."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"
OUT_DIR = Path(__file__).resolve().parent


def make_riemann_area_plot() -> None:
    """Area under f(x)=0.6+0.5*sin(2x) as Riemann sum intuition."""
    a, b = 0.0, np.pi
    n = 8
    x_curve = np.linspace(a, b, 300)
    y_curve = 0.6 + 0.5 * np.sin(2.0 * x_curve)

    fig, ax = plt.subplots(figsize=(4.8, 3.4), dpi=220)
    ax.plot(x_curve, y_curve, color=DARK_TEAL, linewidth=2.4, zorder=3)
    ax.fill_between(x_curve, 0.0, y_curve, color=DARK_TEAL, alpha=0.12)

    xs = np.linspace(a, b, n + 1)
    dx = (b - a) / n
    for i in range(n):
        left = xs[i]
        height = 0.6 + 0.5 * np.sin(2.0 * (left + 0.5 * dx))
        ax.add_patch(
            plt.Rectangle(
                (left, 0.0),
                dx,
                height,
                facecolor=ACCENT,
                edgecolor="white",
                alpha=0.35,
                linewidth=0.8,
                zorder=2,
            )
        )

    ax.set_xlim(a - 0.05, b + 0.15)
    ax.set_ylim(0.0, 1.35)
    ax.set_xlabel(r"$x$", fontsize=10)
    ax.set_ylabel(r"$f(x)$", fontsize=10)
    ax.set_title(r"Integral $\approx$ sum of areas", fontsize=10, color=DARK_TEAL, pad=8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=8)

    out = OUT_DIR / "riemann_area.png"
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Wrote {out}")


def make_leibniz_fixed_limits_plot() -> None:
    """Same interval [0,2], integrand shifts with parameter theta."""
    x = np.linspace(0.0, 2.0, 300)
    t1, t2 = 0.8, 1.4
    f1 = t1 * np.exp(-0.8 * x)
    f2 = t2 * np.exp(-0.8 * x)

    fig, ax = plt.subplots(figsize=(4.8, 3.4), dpi=220)
    ax.fill_between(x, 0.0, f1, color=DARK_TEAL, alpha=0.20)
    ax.fill_between(x, 0.0, f2, color=ACCENT, alpha=0.18)
    ax.plot(x, f1, color=DARK_TEAL, linewidth=2.2, label=rf"$\theta={t1}$")
    ax.plot(x, f2, color=ACCENT, linewidth=2.2, label=rf"$\theta={t2}$")
    ax.axvline(0.0, color="0.45", linewidth=1.0)
    ax.axvline(2.0, color="0.45", linewidth=1.0, linestyle="--")
    ax.text(0.02, 0.92, r"$a$", fontsize=9, color="0.45", transform=ax.get_xaxis_transform())
    ax.text(0.96, 0.92, r"$b$", fontsize=9, color="0.45", transform=ax.get_xaxis_transform())

    ax.set_xlim(-0.05, 2.15)
    ax.set_ylim(0.0, 1.05)
    ax.set_xlabel(r"$x$", fontsize=10)
    ax.set_ylabel(r"$f(x,\theta)$", fontsize=10)
    ax.set_title(r"Fixed limits: $F(\theta)=\int_a^b f(x,\theta)\,dx$", fontsize=9.5, color=DARK_TEAL, pad=8)
    ax.legend(frameon=False, fontsize=8, loc="upper right")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=8)

    out = OUT_DIR / "leibniz_fixed_limits.png"
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Wrote {out}")


def make_leibniz_failure_step_plot() -> None:
    """Moving step: discontinuity shifts with theta; Leibniz regularity fails."""
    a, b = 0.0, 1.0
    t1, t2 = 0.35, 0.65
    x = np.linspace(a, b, 600)

    def step(xv: np.ndarray, t: float) -> np.ndarray:
        return (xv > t).astype(float)

    f1 = step(x, t1)
    f2 = step(x, t2)

    fig, ax = plt.subplots(figsize=(5.2, 3.4), dpi=220)

    ax.fill_between(x, 0.0, f1, color=DARK_TEAL, alpha=0.18, zorder=1)
    ax.fill_between(x, 0.0, f2, color=ACCENT, alpha=0.15, zorder=1)

    ax.plot(x, f1, color=DARK_TEAL, linewidth=2.2, drawstyle="steps-post", label=rf"$\theta={t1:.2f}$")
    ax.plot(x, f2, color=ACCENT, linewidth=2.2, drawstyle="steps-post", label=rf"$\theta={t2:.2f}$")

    for t, col in ((t1, DARK_TEAL), (t2, ACCENT)):
        ax.axvline(t, color=col, linewidth=1.0, linestyle=":", alpha=0.75, zorder=2)

    ax.annotate(
        "jump moves",
        xy=(0.5 * (t1 + t2), 0.5),
        xytext=(0.72, 0.78),
        fontsize=8.5,
        color=DARK_TEAL,
        arrowprops=dict(arrowstyle="->", color=DARK_TEAL, lw=1.1),
    )

    ax.set_xlim(-0.05, 1.08)
    ax.set_ylim(-0.08, 1.18)
    ax.set_xlabel(r"$x$", fontsize=10)
    ax.set_ylabel(r"$f(x,\theta)$", fontsize=10)
    ax.set_title(r"$f(x,\theta)=\mathbf{1}\{x>\theta\}$ on $[0,1]$", fontsize=9.5, color=DARK_TEAL, pad=8)
    ax.legend(frameon=False, fontsize=8.5, loc="lower left", bbox_to_anchor=(0.0, 0.14))
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=8)

    out = OUT_DIR / "leibniz_failure_step.png"
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white", pad_inches=0.06)
    plt.close(fig)
    print(f"Wrote {out}")


def make_leibniz_variable_limits_plot() -> None:
    """Leibniz rule: colored regions for d f/d theta and moving limits a', b'."""
    grey = "#B8B8B8"
    lower_color = "#E88888"
    upper_color = "#8EB8E8"
    curve_dark = "#1A1A1A"
    curve_light = "#7EC8E3"
    guide = "0.45"

    theta = 1.0
    d_theta = 0.32
    a_lim = 0.55
    b_lim = 3.45
    da = -0.28
    db = 0.32

    def f(x: np.ndarray, t: float) -> np.ndarray:
        return t * (0.85 + 0.55 * np.exp(-0.45 * x))

    x = np.linspace(0.0, 4.2, 300)
    f0 = f(x, theta)
    f1 = f(x, theta + d_theta)

    fig, ax = plt.subplots(figsize=(5.4, 3.6), dpi=220)

    a_new = a_lim + da
    b_new = b_lim + db

    mask_lower = (x >= min(a_new, a_lim)) & (x <= max(a_new, a_lim))
    mask_upper = (x >= min(b_lim, b_new)) & (x <= max(b_lim, b_new))
    mask_inner = (x >= a_lim) & (x <= b_lim)

    ax.fill_between(x[mask_lower], 0.0, f0[mask_lower], color=lower_color, alpha=0.55, zorder=1)
    ax.fill_between(x[mask_upper], 0.0, f0[mask_upper], color=upper_color, alpha=0.55, zorder=1)
    ax.fill_between(x[mask_inner], f0[mask_inner], f1[mask_inner], color=grey, alpha=0.55, zorder=2)

    fa = float(f(np.array([a_lim]), theta)[0])
    fb = float(f(np.array([b_lim]), theta)[0])

    ax.plot(x, f0, color=curve_dark, linewidth=2.4, zorder=4, label=rf"$f(x,\theta)$")
    ax.plot(x, f1, color=curve_light, linewidth=2.4, zorder=4, label=rf"$f(x,\theta+\Delta\theta)$")

    ax.axvline(a_lim, color=guide, linewidth=1.0, linestyle="--", zorder=3)
    ax.axvline(b_lim, color=guide, linewidth=1.0, linestyle="--", zorder=3)
    ax.plot(a_lim, fa, "o", color="white", markeredgecolor=curve_dark, markersize=5, zorder=5)
    ax.plot(b_lim, fb, "o", color="white", markeredgecolor=curve_dark, markersize=5, zorder=5)

    ax.axvline(a_new, color=guide, linewidth=0.9, linestyle=":", alpha=0.85, zorder=3)
    ax.axvline(b_new, color=guide, linewidth=0.9, linestyle=":", alpha=0.85, zorder=2)

    y_arrow_a = -0.06
    y_arrow_b = -0.20
    ax.annotate(
        "",
        xy=(a_new, y_arrow_a),
        xytext=(a_lim, y_arrow_a),
        arrowprops=dict(arrowstyle="<->", color=curve_dark, lw=1.2),
        zorder=6,
    )
    ax.annotate(
        "",
        xy=(b_new, y_arrow_b),
        xytext=(b_lim, y_arrow_b),
        arrowprops=dict(arrowstyle="<->", color=curve_dark, lw=1.2),
        zorder=6,
    )
    ax.text(0.5 * (a_lim + a_new), y_arrow_a - 0.11, r"$a'(\theta)$", ha="center", fontsize=9, color=curve_dark)
    ax.text(0.5 * (b_lim + b_new), y_arrow_b - 0.11, r"$b'(\theta)$", ha="center", fontsize=9, color=curve_dark)

    x_mid = 0.5 * (a_lim + b_lim)
    y_mid = 0.5 * (float(f(np.array([x_mid]), theta)[0]) + float(f(np.array([x_mid]), theta + d_theta)[0]))
    ax.text(x_mid, y_mid, r"$\partial f/\partial\theta$", ha="center", va="center", fontsize=9.5, color=curve_dark)

    ax.text(a_lim, -0.02, r"$a$", ha="center", fontsize=9.5, color=guide)
    ax.text(b_lim, -0.02, r"$b$", ha="center", fontsize=9.5, color=guide)
    ax.set_xlabel(r"$x$", fontsize=10)
    ax.set_ylabel(r"$f$", fontsize=10)
    ax.set_xlim(-0.05, 4.35)
    ax.set_ylim(-0.38, 2.05)
    ax.legend(frameon=False, fontsize=8.5, loc="upper right")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=8)

    out = OUT_DIR / "leibniz_variable_limits.png"
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white", pad_inches=0.06)
    plt.close(fig)
    print(f"Wrote {out}")


def make_fubini_triangle_plot() -> None:
    """Triangle D: 0<=x<=1, 0<=y<=x; two slice directions."""
    tri_x = np.array([0.0, 1.0, 1.0, 0.0])
    tri_y = np.array([0.0, 0.0, 1.0, 0.0])

    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.3), dpi=220)

    for ax, title, vertical_slices in zip(
        axes,
        ["y inner: 0 to x", "x inner: y to 1"],
        [False, True],
    ):
        ax.fill(tri_x, tri_y, color=DARK_TEAL, alpha=0.15, zorder=1)
        ax.plot([0, 1, 1, 0, 0], [0, 0, 1, 0, 0], color=DARK_TEAL, lw=2.0, zorder=3)

        if vertical_slices:
            for y in (0.22, 0.52, 0.82):
                x_left = y
                ax.plot([x_left, 1.0], [y, y], color=ACCENT, lw=1.4, zorder=2)
                ax.annotate(
                    "",
                    xy=(1.0, y),
                    xytext=(x_left, y),
                    arrowprops=dict(arrowstyle="->", color=ACCENT, lw=1.2),
                )
        else:
            for x in (0.25, 0.55, 0.85):
                ax.plot([x, x], [0.0, x], color=ACCENT, lw=1.4, zorder=2)
                ax.annotate(
                    "",
                    xy=(x, x),
                    xytext=(x, 0.0),
                    arrowprops=dict(arrowstyle="->", color=ACCENT, lw=1.2),
                )

        ax.set_xlim(-0.05, 1.12)
        ax.set_ylim(-0.05, 1.12)
        ax.set_aspect("equal")
        ax.set_xlabel(r"$x$", fontsize=8)
        ax.set_ylabel(r"$y$", fontsize=8)
        ax.set_title(title, fontsize=9, color=DARK_TEAL, pad=6)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.tick_params(labelsize=7)

    fig.suptitle(
        r"Triangle $D$: $0 \leq x \leq 1$, $0 \leq y \leq x$",
        fontsize=10,
        color=DARK_TEAL,
        y=1.02,
    )
    out = OUT_DIR / "fubini_triangle.png"
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white", pad_inches=0.06)
    plt.close(fig)
    print(f"Wrote {out}")


def make_fubini_parabola_line_plot() -> None:
    """Region between y=x^2 and y=x; two slice directions."""
    x_curve = np.linspace(0.0, 1.0, 200)
    y_parab = x_curve ** 2
    y_line = x_curve

    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.3), dpi=220)

    for ax, title, vertical_slices in zip(
        axes,
        [r"$y$ inner: $x^2$ to $x$", r"$x$ inner: $y$ to $\sqrt{y}$"],
        [False, True],
    ):
        ax.fill_between(x_curve, y_parab, y_line, color=DARK_TEAL, alpha=0.15, zorder=1)
        ax.plot(x_curve, y_parab, color=DARK_TEAL, lw=2.0, zorder=3, label=r"$y=x^2$")
        ax.plot(x_curve, y_line, color=DARK_TEAL, lw=2.0, zorder=3, label=r"$y=x$")

        if vertical_slices:
            for y in (0.16, 0.36, 0.64):
                x_left = y
                x_right = np.sqrt(y)
                ax.plot([x_left, x_right], [y, y], color=ACCENT, lw=1.4, zorder=2)
                ax.annotate(
                    "",
                    xy=(x_right, y),
                    xytext=(x_left, y),
                    arrowprops=dict(arrowstyle="->", color=ACCENT, lw=1.2),
                )
        else:
            for x in (0.25, 0.55, 0.85):
                ax.plot([x, x], [x ** 2, x], color=ACCENT, lw=1.4, zorder=2)
                ax.annotate(
                    "",
                    xy=(x, x),
                    xytext=(x, x ** 2),
                    arrowprops=dict(arrowstyle="->", color=ACCENT, lw=1.2),
                )

        ax.set_xlim(-0.05, 1.12)
        ax.set_ylim(-0.05, 1.12)
        ax.set_aspect("equal")
        ax.set_xlabel(r"$x$", fontsize=8)
        ax.set_ylabel(r"$y$", fontsize=8)
        ax.set_title(title, fontsize=9, color=DARK_TEAL, pad=6)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.tick_params(labelsize=7)

    fig.suptitle(
        r"Region $D$: $x^2 \leq y \leq x$ on $0 \leq x \leq 1$",
        fontsize=10,
        color=DARK_TEAL,
        y=1.02,
    )
    out = OUT_DIR / "fubini_parabola_line.png"
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white", pad_inches=0.06)
    plt.close(fig)
    print(f"Wrote {out}")


def make_fubini_order_plot() -> None:
    """Two orders of integration over a rectangle."""
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.2), dpi=220)

    for ax, title, horizontal in zip(
        axes,
        [r"Inner in $x$, then $y$", r"Inner in $y$, then $x$"],
        [True, False],
    ):
        rect = plt.Rectangle((0.1, 0.15), 0.75, 0.65, fill=False, edgecolor=DARK_TEAL, lw=2.0)
        ax.add_patch(rect)
        if horizontal:
            for y in (0.28, 0.48, 0.68):
                ax.plot([0.1, 0.85], [y, y], color=ACCENT, lw=1.4)
                ax.annotate("", xy=(0.85, y), xytext=(0.1, y), arrowprops=dict(arrowstyle="->", color=ACCENT, lw=1.2))
        else:
            for x in (0.25, 0.45, 0.65):
                ax.plot([x, x], [0.15, 0.80], color=ACCENT, lw=1.4)
                ax.annotate("", xy=(x, 0.80), xytext=(x, 0.15), arrowprops=dict(arrowstyle="->", color=ACCENT, lw=1.2))
        ax.text(0.48, 0.48, r"$f(x,y)$", ha="center", va="center", fontsize=11, color=DARK_TEAL)
        ax.set_xlim(0.0, 1.0)
        ax.set_ylim(0.0, 1.0)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(title, fontsize=9.5, color=DARK_TEAL, pad=6)

    fig.suptitle(r"Fubini: $\iint f(x,y)\,dx\,dy=\iint f(x,y)\,dy\,dx$", fontsize=10, color=DARK_TEAL, y=1.02)
    out = OUT_DIR / "fubini_order.png"
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Wrote {out}")


def make_ibp_rectangle_plot() -> None:
    """Rectangle xy split into area under y=f(x) and area left of the curve."""
    green = "#3D9A6E"
    red = "#E88888"
    curve_blue = "#2563EB"

    def f(x: np.ndarray) -> np.ndarray:
        return (x ** 2) / 2.8

    x0 = 2.35
    y0 = float(f(np.array([x0]))[0])

    x_curve = np.linspace(0.0, x0 + 0.35, 200)
    y_curve = f(x_curve)

    y_fill = np.linspace(0.0, y0, 200)
    x_inverse = np.sqrt(2.8 * y_fill)

    fig, ax = plt.subplots(figsize=(4.9, 3.7), dpi=220)

    ax.fill_between(
        x_curve[x_curve <= x0],
        0.0,
        f(x_curve[x_curve <= x0]),
        color=green,
        alpha=0.45,
        zorder=1,
    )
    ax.fill_betweenx(
        y_fill,
        0.0,
        x_inverse,
        color=red,
        alpha=0.45,
        zorder=1,
    )

    ax.plot(x_curve, y_curve, color=curve_blue, linewidth=2.6, zorder=3)
    ax.plot([x0, x0], [0.0, y0], color="0.35", linewidth=1.0, linestyle="--", zorder=2)
    ax.plot([0.0, x0], [y0, y0], color="0.35", linewidth=1.0, linestyle="--", zorder=2)
    ax.plot(x0, y0, "o", color="white", markeredgecolor=curve_blue, markersize=6, zorder=4)

    ax.annotate("", xy=(x0, -0.18), xytext=(0.0, -0.18), arrowprops=dict(arrowstyle="<->", color="0.25", lw=1.0))
    ax.text(0.5 * x0, -0.34, r"$x$", ha="center", va="top", fontsize=10, color="0.25")
    ax.annotate("", xy=(-0.18, y0), xytext=(-0.18, 0.0), arrowprops=dict(arrowstyle="<->", color="0.25", lw=1.0))
    ax.text(-0.34, 0.5 * y0, r"$y$", ha="right", va="center", fontsize=10, color="0.25", rotation=90)

    ax.text(0.95 * x0, 0.55 * y0, r"$y=f(x)$", fontsize=9.5, color=curve_blue, ha="right")
    ax.text(0.55 * x0, 0.22 * f(np.array([0.55 * x0]))[0], r"$\int y\,dx$", fontsize=10, color=green, ha="center")
    ax.text(0.22 * np.sqrt(2.8 * (0.55 * y0)), 0.55 * y0, r"$\int x\,dy$", fontsize=10, color="#C0392B", ha="center")

    ax.set_xlim(-0.55, x0 + 0.55)
    ax.set_ylim(-0.15, y0 + 0.45)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])

    out = OUT_DIR / "ibp_rectangle.png"
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white", pad_inches=0.08)
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    make_riemann_area_plot()
    make_leibniz_fixed_limits_plot()
    make_leibniz_failure_step_plot()
    make_leibniz_variable_limits_plot()
    make_fubini_triangle_plot()
    make_fubini_parabola_line_plot()
    make_ibp_rectangle_plot()
