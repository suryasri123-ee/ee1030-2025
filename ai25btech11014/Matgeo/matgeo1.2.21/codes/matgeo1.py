import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared object
lib = ctypes.CDLL("./libcentroid.so")

# Define the function prototype
lib.centroid.argtypes = [ctypes.POINTER(ctypes.c_double)] * 4

# Define input vectors
A = np.array([3.0, -5.0, 7.0])
B = np.array([-1.0, 7.0, -6.0])
G = np.array([1.0, 1.0, 1.0])
C = np.zeros(3)

# Convert to ctypes
A_ct = A.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
B_ct = B.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
G_ct = G.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
C_ct = C.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

# Call the C function
lib.centroid(A_ct, B_ct, G_ct, C_ct)

print("Coordinates of point C:", C)

# Plotting the triangle and centroid
triangle = np.block([[A.reshape(3,1), B.reshape(3,1), C.reshape(3,1), A.reshape(3,1)]])
G = G.reshape(3,1)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(triangle[0], triangle[1], triangle[2], 'k-', label='Triangle ABC')
ax.scatter(*A, color='red', label='A')
ax.scatter(*B, color='green', label='B')
ax.scatter(*C, color='blue', label='C')
ax.scatter(*G.flatten(), color='purple', label='Centroid G', s=60)

ax.text(*A, 'A', fontsize=10)
ax.text(*B, 'B', fontsize=10)
ax.text(*C, 'C', fontsize=10)
ax.text(*G.flatten(), 'G', fontsize=10)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.tight_layout()
plt.savefig("triangle_centroid.png")
plt.show()
