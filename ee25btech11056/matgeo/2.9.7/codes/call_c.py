import ctypes
import numpy as np
import sys
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL("./libpoints.so")
lib.triple_product.restype = ctypes.c_double
lib.triple_product.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]

# Default vectors (if no args provided)
a = np.array([2.0, 1.0, 3.0], dtype=np.double)
b = np.array([-1.0, 2.0, 1.0], dtype=np.double)
c = np.array([3.0, 1.0, 2.0], dtype=np.double)

# If user provides command-line arguments → override
if len(sys.argv) == 10:  # script + 9 numbers
    a = np.array([float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])], dtype=np.double)
    b = np.array([float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6])], dtype=np.double)
    c = np.array([float(sys.argv[7]), float(sys.argv[8]), float(sys.argv[9])], dtype=np.double)

# Call C function
res = lib.triple_product(a.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                         b.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                         c.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))

print(f"Scalar Triple Product (from C): {res}")

# ---- Visualization using matplotlib ----
cross_bc = np.cross(b, c)

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

