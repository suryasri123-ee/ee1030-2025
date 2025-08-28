import matplotlib.pyplot as plt
import numpy as np

# Define the coordinates directly
points = {
    'A(2,1)': (2, 1),
    'B(0,5)': (0, 5),
    'C(-1,2)': (-1, 2)
}

# Extract data for plotting
labels = list(points.keys())
xs = [coord[0] for coord in points.values()]
ys = [coord[1] for coord in points.values()]
colors = ['blue', 'orange', 'green']

plt.figure(figsize=(6, 6))

# Plot each point with its label
for (label, (x, y)), color in zip(points.items(), colors):
    plt.scatter(x, y, color=color, s=100, zorder=5)
    plt.text(x + 0.1, y + 0.1, label, fontsize=12, fontweight='bold')

# Draw dashed lines connecting B→A and C→A
plt.plot([0, 2], [5, 1], '--', color='gray', alpha=0.7, linewidth=1.5)
plt.plot([-1, 2], [2, 1], '--', color='gray', alpha=0.7, linewidth=1.5)

# Grid and axes
plt.grid(True, alpha=0.4, linestyle=':')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Axis limits and ticks
plt.xlim(-2, 4)
plt.ylim(0, 7)
plt.xticks(np.arange(-2, 5, 1))
plt.yticks(np.arange(0, 8, 1))

# Title and axis labels
plt.title('Points A, B, C', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('')
plt.ylabel('')

# Save the figure
plt.savefig('fig1.png', dpi=150, bbox_inches='tight')
plt.close()

