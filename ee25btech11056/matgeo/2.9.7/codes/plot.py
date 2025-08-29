import numpy as np
import matplotlib.pyplot as plt

# Vectors
a = np.array([2, 1, 3])
b = np.array([-1, 2, 1])
c = np.array([3, 1, 2])

# Scalar triple product
res = np.dot(a, np.cross(b, c))
print(f"Scalar Triple Product (using NumPy): {res}")

# Cross product b × c
cross_bc = np.cross(b, c)

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.quiver(0, 0, 0, a[0], a[1], a[2], color='blue', label='a', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, b[0], b[1], b[2], color='red', label='b', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, c[0], c[1], c[2], color='green', label='c', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, cross_bc[0], cross_bc[1], cross_bc[2],
          color='purple', label='b × c', arrow_length_ratio=0.1)

ax.set_title(f"Scalar Triple Product = {res:.2f}")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.legend()

plt.savefig("vectors.png", dpi=300, bbox_inches="tight")
plt.show()

