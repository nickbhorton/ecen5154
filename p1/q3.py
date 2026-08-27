import numpy as np
import matplotlib.pyplot as plt

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

# cmap = plt.colormaps['jet']
# color_array = cmap(np.linspace(0, 1, len(x)))

def L(xs, x, k):
    result = 1.0
    for i in range(len(xs)):
        if i != k:
            result *= (x - xs[i]) / (xs[k] - xs[i])
    return result


x = np.array([0.5, 1.0, 4.0, 8.0, 9.0, 10.0])
y = np.array([1.4770, 1.4560, 1.2347, 0.6750, 0.7155, 1.0])

x_interp = np.linspace(0, 10, 201)
fig, ax = plt.subplots(figsize=(7,7), dpi=150)

for i in [0, 3, 4]:
    ax.scatter(x, [L(x, x_k, i) for x_k in x], 100, alpha=0.5, edgecolors='none')
    ax.plot(x_interp, L(x, x_interp, i), label=f"$L_{i}(x)$", alpha=0.8)

ax.legend()
plt.show()
