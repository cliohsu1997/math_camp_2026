"""Farkas' Lemma geometry: cone S = {Mx - y : x, y >= 0} in R^2."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"
CONE_FILL = "#23373B"
CONE_ALPHA = 0.28
S_FILL = "#EB811B"
S_ALPHA = 0.28
OUT_DIR = Path(__file__).resolve().parent


def _in_s(v1: np.ndarray, v2: np.ndarray, s: np.ndarray, tol: float = 1e-9) -> bool:
    if np.all(s <= tol):
        return True
    m = np.column_stack([v1, v2])
    xgrid = np.linspace(0.0, 22.0, 55)
    pairs = np.array([[x1, x2] for x1 in xgrid for x2 in xgrid])
    k_pts = (m @ pairs.T).T
    return bool(np.any(np.all(k_pts >= s - tol, axis=1)))


def _s_membership_grid(
    v1: np.ndarray,
    v2: np.ndarray,
    x_lo: float,
    y_lo: float,
    x_hi: float,
    y_hi: float,
    n: int = 260,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Grid mask: 1 inside S, 0 outside."""
    xs = np.linspace(x_lo, x_hi, n)
    ys = np.linspace(y_lo, y_hi, n)
    m = np.column_stack([v1, v2])
    xgrid = np.linspace(0.0, 22.0, 55)
    pairs = np.array([[x1, x2] for x1 in xgrid for x2 in xgrid])
    k_pts = (m @ pairs.T).T

    s_xx, s_yy = np.meshgrid(xs, ys)
    s_pts = np.column_stack([s_xx.ravel(), s_yy.ravel()])
    dominated = (
        (k_pts[None, :, :] >= s_pts[:, None, :] - 1e-9).all(axis=2).any(axis=1)
    )
    z = dominated.reshape(len(ys), len(xs)).astype(float)
    return xs, ys, z


def _cone_wedge(
    v1: np.ndarray,
    v2: np.ndarray,
    scale: float,
    n_arc: int = 40,
) -> np.ndarray:
    a1 = np.arctan2(v1[1], v1[0])
    a2 = np.arctan2(v2[1], v2[0])
    if a2 < a1:
        a2 += 2.0 * np.pi
    angles = np.linspace(a1, a2, n_arc)
    rays = np.column_stack([np.cos(angles), np.sin(angles)])
    norms = np.linalg.norm(rays, axis=1, keepdims=True)
    rays = rays / np.maximum(norms, 1e-12)
    boundary = rays * scale
    return np.vstack([np.zeros(2), boundary, np.zeros(2)])


def _southwest_shadows(
    v1: np.ndarray,
    v2: np.ndarray,
    scale: float,
    x_lo: float,
    y_lo: float,
    n_samples: int = 14,
) -> list[np.ndarray]:
    """
    Sample rectangles showing free disposal: from each cone point, move SW.
    Each polygon is the SW orthant relative to a point on the cone boundary.
    """
    a1 = np.arctan2(v1[1], v1[0])
    a2 = np.arctan2(v2[1], v2[0])
    if a2 < a1:
        a2 += 2.0 * np.pi

    polys: list[np.ndarray] = []
    for ang in np.linspace(a2, a1, n_samples):
        d = np.array([np.cos(ang), np.sin(ang)])
        d = d / np.linalg.norm(d)
        m = np.column_stack([v1, v2])
        lo, hi = 0.0, scale
        for _ in range(40):
            mid = 0.5 * (lo + hi)
            p = mid * d
            try:
                x = np.linalg.solve(m, p)
                if np.all(x >= -1e-10):
                    lo = mid
                else:
                    hi = mid
            except np.linalg.LinAlgError:
                hi = mid
        p = lo * d
        polys.append(
            np.array(
                [
                    [x_lo, y_lo],
                    [p[0], y_lo],
                    [p[0], p[1]],
                    [x_lo, p[1]],
                    [x_lo, y_lo],
                ]
            )
        )
    return polys


def main() -> None:
    v1 = np.array([-2.0, 1.0])
    v2 = np.array([-1.0, -1.0])
    q = np.array([1.0, 1.0])
    z = np.array([1.0, 0.0])

    x_lo, y_lo = -3.2, -3.0
    x_hi, y_hi = 2.2, 3.2

    assert not _in_s(v1, v2, q)
    assert z @ v1 <= 0 and z @ v2 <= 0 and z @ q > 0

    xs, ys, zgrid = _s_membership_grid(v1, v2, x_lo, y_lo, x_hi, y_hi)
    cone = _cone_wedge(v1, v2, scale=2.8)
    sw_polys = _southwest_shadows(v1, v2, scale=2.8, x_lo=x_lo, y_lo=y_lo)

    fig, ax = plt.subplots(figsize=(7.2, 6.2))
    ax.set_facecolor("white")
    fig.patch.set_facecolor("white")

    # Layer 1: overlapping SW orthants from sample cone points (pedagogical).
    for poly in sw_polys:
        ax.add_patch(
            Polygon(
                poly,
                closed=True,
                facecolor=S_FILL,
                edgecolor=S_FILL,
                linewidth=0.4,
                alpha=0.07,
                zorder=1,
            )
        )

    # Layer 2: exact membership fill for all of S.
    ax.contourf(
        xs,
        ys,
        zgrid,
        levels=[0.5, 1.5],
        colors=[S_FILL],
        alpha=S_ALPHA,
        zorder=2,
    )

    # Layer 3: cone K_M on top.
    ax.add_patch(
        Polygon(
            cone,
            closed=True,
            facecolor=CONE_FILL,
            edgecolor=DARK_TEAL,
            linewidth=1.0,
            alpha=CONE_ALPHA,
            zorder=3,
        )
    )

    for v, label in [(v1, r"$v_1$"), (v2, r"$v_2$")]:
        ax.annotate(
            "",
            xy=v * 1.05,
            xytext=(0, 0),
            arrowprops=dict(
                arrowstyle="-|>",
                color=DARK_TEAL,
                lw=2.0,
                mutation_scale=14,
            ),
            zorder=5,
        )
        ax.text(
            v[0] * 1.12,
            v[1] * 1.12,
            label,
            fontsize=13,
            color=DARK_TEAL,
            ha="center",
            va="center",
        )

    ax.plot(q[0], q[1], "o", color=ACCENT, markersize=10, zorder=6)
    ax.text(
        q[0] + 0.15,
        q[1] + 0.18,
        r"$q \notin S$",
        fontsize=12,
        color=ACCENT,
        fontweight="bold",
    )

    y_line = np.linspace(y_lo, y_hi, 2)
    ax.plot([0.0, 0.0], y_line, color=ACCENT, lw=1.8, ls="--", zorder=5)
    ax.text(0.12, 2.55, r"$z^{\top} x = 0$", fontsize=11, color=ACCENT)

    ax.annotate(
        "",
        xy=(0.55, 0.0),
        xytext=(0.05, 0.0),
        arrowprops=dict(
            arrowstyle="-|>",
            color=ACCENT,
            lw=1.6,
            mutation_scale=12,
        ),
        zorder=5,
    )
    ax.text(0.62, 0.22, r"$z \geq 0$", fontsize=11, color=ACCENT)

    ax.text(
        -2.05,
        -2.35,
        r"$S = K_M +$ SW shadow",
        fontsize=10.5,
        color=DARK_TEAL,
        ha="center",
    )
    ax.text(
        -1.35,
        0.55,
        r"$K_M$",
        fontsize=11,
        color=DARK_TEAL,
        alpha=0.85,
    )

    ax.set_xlim(x_lo, x_hi)
    ax.set_ylim(y_lo, y_hi)
    ax.set_aspect("equal")
    ax.axhline(0, color="#cccccc", lw=0.8, zorder=0)
    ax.axvline(0, color="#cccccc", lw=0.8, zorder=0)
    ax.set_xlabel(r"$s_1$", fontsize=11)
    ax.set_ylabel(r"$s_2$", fontsize=11)
    ax.set_title(
        r"Farkas: $q \notin S$ $\Rightarrow$ separating $z \geq 0$",
        fontsize=12,
        color=DARK_TEAL,
        pad=10,
    )
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    out = OUT_DIR / "farkas_geometry.png"
    fig.savefig(out, dpi=180, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
