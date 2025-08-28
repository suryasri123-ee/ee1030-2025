
import matplotlib.pyplot as plt
from call_c_program import get_points  # make sure this file is named correctly

points = get_points()
xs, ys = zip(*points)

# Plot AB line
plt.plot(xs[:2], ys[:2], "b-", label="Line AB")

# Plot points
plt.scatter(xs, ys, color="red", zorder=5)

# Annotate points
labels = ["A(1,-5)", "B(-4,5)", "C(-1.5,0)"]
for (x, y), label in zip(points, labels):
    plt.text(x+0.1, y+0.1, label, fontsize=10)

plt.axhline(0, color="gray", linewidth=0.5)
plt.axvline(0, color="gray", linewidth=0.5)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Points A, B, and Midpoint C")
plt.legend()
plt.grid(True)

# ✅ Save to file
plt.savefig("points_plot.png")  

# Show on screen (optional)
plt.show()

