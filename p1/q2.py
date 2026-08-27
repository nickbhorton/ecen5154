import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler


plt.rcParams.update(
    {
        "axes.grid": False,
        "axes.edgecolor": "black",
        "xtick.major.size": 0,
        "ytick.major.size": 0,
        "font.size": 12,
        "text.color": "black",
        "axes.labelcolor": "black",
        "axes.labelsize": 14,
        "legend.frameon": False,
        "lines.linewidth": 2.5,
    }
)
alpha1 = 0.8


def f(x):
    return np.sin(2.0 * np.pi * x)


def dfdx(x):
    return 2.0 * np.pi * np.cos(2.0 * np.pi * x)


def dfdx_FD(x, h):
    return (f(x + h) - f(x)) / h


def dfdx_CD(x, h):
    return (f(x + h) - f(x - h)) / (2.0 * h)


def dfdx_BD(x, h):
    return (f(x) - f(x - h)) / h


def relative_error(expected, measured):
    return np.abs(expected - measured) / np.abs(expected)


x = np.pi / 5
h = np.logspace(-10, -1, 1000)

fig, ax = plt.subplots(figsize=(7, 7), dpi=150)
ax.plot(
    1.0 / h,
    relative_error(dfdx(x), dfdx_FD(x, h)),
    label="Forward Difference",
    alpha=alpha1,
)
ax.plot(
    1.0 / h,
    relative_error(dfdx(x), dfdx_CD(x, h)),
    label="Central Difference",
    alpha=alpha1,
)
ax.plot(
    1.0 / h,
    relative_error(dfdx(x), dfdx_BD(x, h)),
    label="Backward Difference",
    alpha=alpha1,
)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("Inverse Step Size (1/m)")
ax.set_ylabel("Relative Error")
ax.legend()
plt.show()
fig.savefig("plots/fd_fig1.png")
