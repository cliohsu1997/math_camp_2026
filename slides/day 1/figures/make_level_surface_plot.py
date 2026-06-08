"""Generate 3D surface with level curves for Day 1 slides."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.lines import Line2D
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# Hill: f(x, y) = 2 * exp(-0.35 * (x^2 + y^2)) + 0.25
x = np.linspace(-2.2, 2.2, 80)
y = np.linspace(-2.2, 2.2, 80)
X, Y = np.meshgrid(x, y)
Z = 2.0 * np.exp(-0.35 * (X**2 + Y**2)) + 0.25

c_level = 1.0
levels = np.linspace(0.4, 2.1, 8)

fig = plt.figure(figsize=(5.4, 4.6), dpi=200)
ax = fig.add_subplot(111, projection="3d")

surface = ax.plot_surface(
    X,
    Y,
    Z,
    cmap=cm.viridis,
    alpha=0.82,
    linewidth=0,
    antialiased=True,
    rstride=2,
    cstride=2,
)

# Level curves projected onto the base plane (z = z_min)
z_base = Z.min() - 0.08
ax.contour(
    X,
    Y,
    Z,
    levels=levels,
    zdir="z",
    offset=z_base,
    cmap=cm.viridis,
    linewidths=1.1,
)

# Highlight one level curve at z = c
ax.contour(
    X,
    Y,
    Z,
    levels=[c_level],
    zdir="z",
    offset=z_base,
    colors=["#EB811B"],
    linewidths=2.4,
)

# Horizontal slice plane at z = c
xx, yy = np.meshgrid(np.linspace(-2.2, 2.2, 2), np.linspace(-2.2, 2.2, 2))
zz = np.full_like(xx, c_level)
ax.plot_surface(
    xx,
    yy,
    zz,
    color="#EB811B",
    alpha=0.22,
    linewidth=0,
    shade=False,
)

# Slice curve on the surface (where f = c)
ax.contour(
    X,
    Y,
    Z,
    levels=[c_level],
    colors=["#EB811B"],
    linewidths=2.6,
)

ax.set_xlabel("$x$", fontsize=10, labelpad=4)
ax.set_ylabel("$y$", fontsize=10, labelpad=4)
ax.set_zlabel("$z$", fontsize=10, labelpad=2)
ax.tick_params(axis="z", pad=1)
ax.view_init(elev=28, azim=-52)
ax.set_box_aspect((1.0, 1.0, 0.55))
ax.set_zlim(z_base, Z.max() + 0.15)

legend_handles = [
    Line2D(
        [0],
        [0],
        color="#EB811B",
        lw=2.4,
        label=r"$z=c$ slice $\Rightarrow$ $\mathcal{L}_c$",
    ),
]

# Dedicated colorbar axis (3D axes do not support axes_grid dividers)
fig.subplots_adjust(left=0.0, right=0.82, top=0.96, bottom=0.20)
cbar_ax = fig.add_axes([0.84, 0.26, 0.035, 0.52])
cbar = fig.colorbar(
    surface,
    cax=cbar_ax,
    ticks=np.linspace(0.5, 2.0, 4),
)
cbar.set_label("$f(x,y)$", fontsize=10, labelpad=8)
cbar.ax.tick_params(labelsize=8)

fig.legend(
    handles=legend_handles,
    loc="upper center",
    bbox_to_anchor=(0.42, 0.04),
    fontsize=9,
    framealpha=0.92,
    borderpad=0.4,
    handlelength=1.8,
    ncol=1,
)
fig.savefig(
    "level_surface_3d.png",
    bbox_inches="tight",
    pad_inches=0.04,
    facecolor="white",
    transparent=False,
)
print("Saved level_surface_3d.png")
