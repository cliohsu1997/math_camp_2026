"""Lagrangian duality geometry: supporting lines in the (u, t) plane."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"
CLOUD_FILL = "#23373B"
CLOUD_ALPHA = 0.15
OUT_DIR = Path(__file__).resolve().parent


def _cloud_points() -> np.ndarray:
    """Achievable (u, t) pairs — mildly non-convex cloud."""
    rng = np.random.default_rng(7)
    u = np.concatenate(
        [
            rng.uniform(-2.2, 0.8, 80),
            rng.uniform(-1.5, -0.2, 40),
        ]
    )
    t = 0.6 * u**2 + 0.35 * u + 1.8 + 0.25 * rng.standard_normal(len(u))
    return np.column_stack([u, t])


def _support_line(u: np.ndarray, lam: float, g: float) -> np.ndarray:
    return -lam * u + g


def main() -> None:
    pts = _cloud_points()
    u_lo, u_hi = -2.5, 1.0
    t_lo, t_hi = 0.2, 3.8

    # Primal optimum: min t among u <= 0
    feas = pts[pts[:, 0] <= 0]
    p_star_idx = int(np.argmin(feas[:, 1]))
    p_star = feas[p_star_idx]

    lam_hi = 2.0
    g_hi = float(np.min(pts[:, 1] + lam_hi * pts[:, 0]))
    lam_lo = 0.5
    g_lo = float(np.min(pts[:, 1] + lam_lo * pts[:, 0]))

    lams = np.linspace(0.2, 2.5, 200)
    gs = [float(np.min(pts[:, 1] + lam * pts[:, 0])) for lam in lams]
    best_i = int(np.argmax(gs))
    lam_star = lams[best_i]
    d_star = gs[best_i]

    fig, ax = plt.subplots(figsize=(7.2, 5.8))
    ax.set_facecolor("white")
    fig.patch.set_facecolor("white")

    ax.scatter(
        pts[:, 0],
        pts[:, 1],
        s=18,
        c=CLOUD_FILL,
        alpha=0.45,
        edgecolors="none",
        zorder=2,
        label=r"achievable $(u,t)$",
    )

    u_line = np.linspace(u_lo, u_hi, 2)
    ax.axvline(0, color="#888888", lw=1.0, ls=":", zorder=1)
    ax.text(0.06, t_hi - 0.15, r"$u=0$", fontsize=10, color="#666666")

    u_plot = np.linspace(u_lo, u_hi, 2)
    for lam, g, ls, lw, label in [
        (lam_hi, g_hi, "--", 1.4, rf"$\lambda={lam_hi:.1f}$, $g={g_hi:.2f}$"),
        (lam_lo, g_lo, "--", 1.4, rf"$\lambda={lam_lo:.1f}$, $g={g_lo:.2f}$"),
        (lam_star, d_star, "-", 2.2, rf"best $\lambda$, $d^*={d_star:.2f}$"),
    ]:
        color = ACCENT if lam == lam_star else "#aaaaaa"
        ax.plot(
            u_plot,
            _support_line(u_plot, lam, g),
            color=color,
            lw=lw,
            ls=ls,
            zorder=4 if lam == lam_star else 3,
        )
        if lam == lam_star:
            ax.plot(0, d_star, "o", color=ACCENT, ms=8, zorder=6)
            ax.text(0.12, d_star + 0.08, r"$d^*$", fontsize=11, color=ACCENT)

    ax.plot(p_star[0], p_star[1], "o", color=DARK_TEAL, ms=9, zorder=6)
    ax.text(
        p_star[0] + 0.08,
        p_star[1] - 0.2,
        r"$p^*$",
        fontsize=11,
        color=DARK_TEAL,
        fontweight="bold",
    )

    # Shade feasible region u <= 0
    ax.axvspan(u_lo, 0, color=CLOUD_FILL, alpha=0.06, zorder=0)
    ax.text(-1.6, t_lo + 0.15, r"feasible $u \leq 0$", fontsize=9.5, color=DARK_TEAL)

    ax.set_xlim(u_lo, u_hi)
    ax.set_ylim(t_lo, t_hi)
    ax.set_xlabel(r"constraint value $u = f_1(x)$", fontsize=11)
    ax.set_ylabel(r"objective $t = f_0(x)$", fontsize=11)
    ax.set_title(
        r"Dual = highest intercept of a supporting line $t + \lambda u = g$",
        fontsize=11.5,
        color=DARK_TEAL,
        pad=10,
    )
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    out = OUT_DIR / "lagrange_geometry.png"
    fig.savefig(out, dpi=180, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
