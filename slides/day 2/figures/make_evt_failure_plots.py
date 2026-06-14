"""EVT failure examples for Day 2 section 2.2."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

DARK_TEAL = "#23373B"
ACCENT = "#EB811B"
OUT_DIR = Path(__file__).resolve().parent


def _style_axis(ax, title: str, xlabel: str = r"$x$") -> None:
    ax.set_title(title, fontsize=9, color=DARK_TEAL, pad=6)
    ax.set_xlabel(xlabel, fontsize=8)
    ax.set_ylabel(r"$f(x)$", fontsize=8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=7)


def make_evt_failure_plot() -> None:
    fig, axes = plt.subplots(1, 3, figsize=(9.2, 3.0), dpi=220)

    # 1) Not closed: f(x)=x on (0,1), supremum 1 not attained
    ax = axes[0]
    x = np.linspace(0.02, 0.98, 200)
    ax.plot(x, x, color=DARK_TEAL, linewidth=2.2)
    ax.plot(0.0, 0.0, marker="o", mfc="white", mec=DARK_TEAL, ms=6, zorder=4)
    ax.plot(1.0, 1.0, marker="o", mfc="white", mec=ACCENT, ms=6, zorder=4)
    ax.axhline(1.0, color=ACCENT, linestyle=":", linewidth=1.2, alpha=0.8)
    ax.set_xlim(-0.05, 1.08)
    ax.set_ylim(-0.05, 1.12)
    _style_axis(ax, r"Not closed: $(0,1)$")

    # 2) Not bounded: f(x)=x on [0,infty), no maximum
    ax = axes[1]
    x = np.linspace(0.0, 3.2, 200)
    ax.plot(x, x, color=DARK_TEAL, linewidth=2.2)
    ax.set_xlim(-0.05, 3.35)
    ax.set_ylim(-0.05, 3.45)
    _style_axis(ax, r"Not bounded: $[0,\infty)$")

    # 3) Not continuous: f(x)=x on [0,1), f(1)=0; value 1 not attained
    ax = axes[2]
    x = np.linspace(0.0, 0.98, 200)
    ax.plot(x, x, color=DARK_TEAL, linewidth=2.2)
    ax.plot(1.0, 0.0, marker="o", color=DARK_TEAL, ms=6, zorder=4)
    ax.plot(1.0, 1.0, marker="o", mfc="white", mec=ACCENT, ms=6, zorder=4)
    ax.axhline(1.0, color=ACCENT, linestyle=":", linewidth=1.2, alpha=0.8)
    ax.set_xlim(-0.05, 1.12)
    ax.set_ylim(-0.08, 1.12)
    _style_axis(ax, r"Not continuous on $[0,1]$")

    fig.tight_layout(w_pad=1.2)
    out = OUT_DIR / "evt_failures.png"
    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    make_evt_failure_plot()
