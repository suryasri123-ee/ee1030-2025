import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# -----------------------------
# Read magnitude and direction ratios from file
# vector.dat should contain: 14 2 3 -6
# -----------------------------
data = np.loadtxt("vector.dat")
magnitude, a, b, c = data

# Normalize direction ratios → direction cosines
d = np.sqrt(a**2 + b**2 + c**2)
l, m, n = a/d, b/d, c/d

# Vector components (scaled by magnitude)
x, y, z = magnitude * np.array([l, m, n])

# Angles with axes
alpha = np.degrees(np.arccos(l))
beta  = np.degrees(np.arccos(m))
gamma = np.degrees(np.arccos(n))

# -----------------------------
# Plot setup (one figure only)
# -----------------------------
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the main vector
ax.quiver(0, 0, 0, x, y, z, color='r', arrow_length_ratio=0.1, linewidth=2, label="Vector r")

# Plot projections on axes
ax.quiver(0, 0, 0, x, 0, 0, color='b', linestyle='dashed', arrow_length_ratio=0.05, label="x-component")
ax.quiver(0, 0, 0, 0, y, 0, color='g', linestyle='dashed', arrow_length_ratio=0.05, label="y-component")
ax.quiver(0, 0, 0, 0, 0, z, color='orange', linestyle='dashed', arrow_length_ratio=0.05, label="z-component")

# Function to draw arc in 3D
def plot_arc(ax, radius, angle, axis='x', color='k'):
    t = np.linspace(0, np.radians(angle), 50)
    if axis == 'x':
        xs, ys, zs = radius*np.cos(t), radius*np.sin(t), 0*t
    elif axis == 'y':
        xs, ys, zs = radius*np.cos(t), 0*t, radius*np.sin(t)
    else:  # z-axis
        xs, ys, zs = 0*t, radius*np.cos(t), radius*np.sin(t)
    ax.plot(xs, ys, zs, color=color, linewidth=1.2)

# Draw arcs for α, β, γ
plot_arc(ax, 3, alpha, axis='x', color='b')
plot_arc(ax, 3, beta, axis='y', color='g')
plot_arc(ax, 3, gamma, axis='z', color='orange')

# Label the angles
ax.text(3.5, 0.5, 0, f"α={alpha:.1f}°", color='b')
ax.text(0.5, 3.5, 0, f"β={beta:.1f}°", color='g')
ax.text(0.5, 0.5, 3.5, f"γ={gamma:.1f}°", color='orange')

# Axes labels & limits
ax.set_xlim([0, max(0, x) + 5])
ax.set_ylim([0, max(0, y) + 5])
ax.set_zlim([min(0, z) - 5, max(0, z) + 5])

ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("3D Vector Representation with Components & Angles")

ax.legend()

# Save the figure and show it (single figure only)
plt.savefig("vector_plot.png", dpi=300, bbox_inches='tight')
plt.show()

