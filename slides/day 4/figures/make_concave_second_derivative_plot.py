"""Concave function: FOC at peak and decreasing tangent slopes (f'' <= 0)."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

DARK_TEAL = "#23373B"
TANGENT_LEFT = "#E74C3C"
TANGENT_PEAK = "#27AE60"
TANGENT_RIGHT = "#9B59B6"
OUT_DIR = Path(__file__).resolve().parent


def concave_y(x: np.ndarray) -> np.ndarray:
    return -0.8 * (x - 0.5) ** 2 + 2.0


def concave_slope(x0: float) -> float:
    return -1.6 * (x0 - 0.5)


def main() -> None:
    fig, ax = plt.subplots(figsize=(7.0, 4.0), dpi=220)

    x = np.linspace(-1.5, 2.5, 400)
    ax.plot(x, concave_y(x), color=DARK_TEAL, lw=2.5, zorder=3)

    tangent_specs = [
        (-0.8, TANGENT_LEFT, r"$f'(x)>0$"),
        (0.5, TANGENT_PEAK, r"$f'(x^*)=0$"),
        (1.8, TANGENT_RIGHT, r"$f'(x)<0$"),
    ]

    for x0, color, slope_label in tangent_specs:
        y0 = concave_y(x0)
        slope = concave_slope(x0)
        tangent = y0 + slope * (x - x0)

        ax.plot(x, tangent, color=color, lw=2.0, ls="--", alpha=0.85, zorder=2)
        ax.plot(x0, y0, "o", color=color, ms=7, zorder=4)

        label_y = y0 + 0.22 if x0 == 0.5 else y0 + 0.18
        ax.annotate(
            slope_label,
            xy=(x0, y0),
            xytext=(x0, label_y),
            fontsize=10,
            color=color,
            ha="center",
            va="bottom",
        )

    ax.annotate(
        "FOC",
        xy=(0.5, concave_y(0.5)),
        xytext=(0.95, 2.35),
        fontsize=10,
        color=TANGENT_PEAK,
        ha="left",
        arrowprops=dict(arrowstyle="->", color=TANGENT_PEAK, lw=1.2),
    )

    ax.annotate(
        r"$f''(x)\leq 0$: tangent slope decreases in $x$",
        xy=(1.6, 0.55),
        fontsize=10,
        color=DARK_TEAL,
        ha="center",
    )

    ax.set_xlim(-1.5, 2.5)
    ax.set_ylim(0, 3)
    ax.set_xlabel(r"$x$", fontsize=11)
    ax.set_ylabel(r"$f(x)$", fontsize=11)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=9)

    out = OUT_DIR / "concave_second_derivative.png"
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white", pad_inches=0.08)
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
