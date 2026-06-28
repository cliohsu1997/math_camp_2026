"""Tilted triangle with tilted sliding hyperplanes for FTLP notes."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent / "sliding_hyperplane.png"

# Tilted triangle P
vertices = np.array([[0.0, 0.0], [4.0, 1.0], [1.0, 3.0]])
tri = np.vstack([vertices, vertices[0]])

# Objective c = (1, 2): maximize x1 + 2*x2
c = np.array([1.0, 2.0])
c_hat = c / np.linalg.norm(c)
values = vertices @ c
opt_idx = int(np.argmax(values))
opt = vertices[opt_idx]
M = float(values[opt_idx])

fig, ax = plt.subplots(figsize=(7.8, 5.0))

ax.fill(tri[:, 0], tri[:, 1], color="#d6e8f7", edgecolor="#1f4e79", linewidth=2)
ax.plot(vertices[:, 0], vertices[:, 1], "o", color="#1f4e79", markersize=7)

x_line = np.linspace(-0.5, 5.0, 200)
for t, style, lw in [(4.0, "--", 1.2), (M, "-", 2.0)]:
    y_line = (t - c[0] * x_line) / c[1]
    ax.plot(x_line, y_line, color="#c44e52", linestyle=style, linewidth=lw)
    label_x = 4.35
    label_y = (t - c[0] * label_x) / c[1]
    ax.text(
        label_x,
        label_y + 0.12,
        rf"$H_t$, $t={int(t)}$",
        color="#c44e52",
        fontsize=11,
    )

opt_x = int(round(opt[0]))
opt_y = int(round(opt[1]))
ax.annotate(
    rf"$({opt_x},{opt_y})$ optimal",
    xy=(opt[0], opt[1]),
    xytext=(2.0, 1.15),
    arrowprops=dict(arrowstyle="->", color="#333333"),
    fontsize=11,
)

# Direction of c: longer arrow + dashed extension line
origin = np.array([0.55, 0.35])
arrow_len = 1.35
tip = origin + arrow_len * c_hat
ax.annotate(
    "",
    xy=tip,
    xytext=origin,
    arrowprops=dict(
        arrowstyle="-|>",
        color="#2d6a4f",
        linewidth=2.5,
        mutation_scale=14,
    ),
)
ext = origin + np.array([-0.55, -0.55]) * c_hat
ax.plot(
    [ext[0], tip[0] + 0.25 * c_hat[0]],
    [ext[1], tip[1] + 0.25 * c_hat[1]],
    color="#2d6a4f",
    linestyle=":",
    linewidth=1.4,
)
ax.text(
    tip[0] + 0.08,
    tip[1] + 0.05,
    r"$\mathbf{c}=(1,2)^T$",
    color="#2d6a4f",
    fontsize=12,
)

# Show H_t is orthogonal to c (at a point on the dashed hyperplane)
meet_x = 2.0
meet_y = (4.0 - c[0] * meet_x) / c[1]
meet = np.array([meet_x, meet_y])
perp = np.array([-c_hat[1], c_hat[0]])
tick_half = 0.22
ax.plot(
    [meet[0] - tick_half * perp[0], meet[0] + tick_half * perp[0]],
    [meet[1] - tick_half * perp[1], meet[1] + tick_half * perp[1]],
    color="#6b6b6b",
    linewidth=1.5,
)
ax.text(meet[0] - 0.55, meet[1] + 0.35, r"$H_t \perp \mathbf{c}$", fontsize=10, color="#6b6b6b")

ax.set_xlim(-0.5, 5.0)
ax.set_ylim(-0.3, 3.5)
ax.set_xlabel(r"$x_1$")
ax.set_ylabel(r"$x_2$")
ax.set_title(
    r"Tilted triangle: $H_t=\{x_1+2x_2=t\}$ touches $P$ at $t=M=7$"
)
ax.set_aspect("equal", adjustable="box")
ax.grid(True, alpha=0.25)
fig.tight_layout()
fig.savefig(OUT, dpi=160)
plt.close(fig)
print(f"Wrote {OUT}")
