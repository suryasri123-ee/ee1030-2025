import matplotlib.pyplot as plt
import numpy as np

# Define the points
points = [(2, 1), (0, 5), (-1, 2)]
labels = ['A(2,1)', 'B(0,5)', 'C(-1,2)']
colors = ['blue', 'orange', 'green']

plt.figure(figsize=(6, 6))

# Plot the points
for i, ((x, y), label, color) in enumerate(zip(points, labels, colors)):
    plt.scatter(x, y, color=color, s=100, zorder=5)
    plt.text(x + 0.1, y + 0.1, label, fontsize=12, fontweight='bold')

# Draw dashed lines connecting the points
# Line from B to A
plt.plot([0, 2], [5, 1], '--', color='gray', alpha=0.7, linewidth=1.5)
# Line from C to A  
plt.plot([-1, 2], [2, 1], '--', color='gray', alpha=0.7, linewidth=1.5)

# Set up the grid and axes
plt.grid(True, alpha=0.4, linestyle=':')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Set axis limits to match the reference image
plt.xlim(-2, 4)
plt.ylim(0, 7)

# Set tick marks
plt.xticks(np.arange(-2, 5, 1))
plt.yticks(np.arange(0, 8, 1))

# Add title
plt.title('Points A, B, C', fontsize=14, fontweight='bold', pad=20)

# Remove axis labels (x and y)
plt.xlabel('')
plt.ylabel('')

# Save the figure
plt.savefig('fig1.png', dpi=150, bbox_inches='tight')
plt.close()

print("Plot saved as fig1.png")

