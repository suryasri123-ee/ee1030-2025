import ctypes
import matplotlib.pyplot as plt
import numpy as np

# --- Part 1: Interfacing with the C Function ---

# Load the shared library
try:
    solver_lib = ctypes.CDLL('./1.5.24.so')
except OSError as e:
    print("Error loading shared library. Did you compile 1.5.24.c?")
    print(e)
    exit()

# Define the argument and return types for the C function
solver_lib.findCoordinates.argtypes = [
    ctypes.c_int, ctypes.c_int,
    ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)
]
solver_lib.findCoordinates.restype = None

# Input midpoint
midpoint_x, midpoint_y = 2, -5

# --- Part 2: Relations from math ---

print("Step 1: Rank relation between b and c")
print("Line: ux + vy + w = 0")
print("P = (0,b), Q = (c,0) lie on the line")
print("=> vb + w = 0,   uc + w = 0")
print("Subtracting: vb - uc = 0 => v b = u c (relation 1)\n")

print("Step 2: Midpoint relation")
print("Midpoint M = ( (0+c)/2, (b+0)/2 ) = (2, -5)")
print("=> c/2 = 2 => c = 4")
print("=> b/2 = -5 => b = -10 (relation 2)\n")

# --- Part 3: Call the C solver for verification ---

c_val, b_val = ctypes.c_int(), ctypes.c_int()
solver_lib.findCoordinates(
    ctypes.c_int(midpoint_x),
    ctypes.c_int(midpoint_y),
    ctypes.byref(c_val),
    ctypes.byref(b_val)
)

c = c_val.value
b = b_val.value

# Define coordinates
P = (0, b)
Q = (c, 0)
M = (midpoint_x, midpoint_y)

print("Step 3: Solve both relations")
print(f"Coordinates of P = {P}")
print(f"Coordinates of Q = {Q}\n")

# --- Part 4: Plotting the Result ---

x_points = np.array([P[0], Q[0]])
y_points = np.array([P[1], Q[1]])

plt.figure(figsize=(8,7))
plt.plot(x_points, y_points, 'b-', label=f'Line PQ')
plt.plot(P[0], P[1], 'go', markersize=10, label=f'P = {P}')
plt.plot(Q[0], Q[1], 'ro', markersize=10, label=f'Q = {Q}')
plt.plot(M[0], M[1], 'm*', markersize=12, label=f'M = {M}')

# Annotate points
plt.text(P[0] + 0.2, P[1], f'P{P}', fontsize=12)
plt.text(Q[0] + 0.2, Q[1], f'Q{Q}', fontsize=12)
plt.text(M[0] + 0.2, M[1], f'M{M}', fontsize=12)

# Formatting
plt.title('Line Intercepting Axes with Midpoint Condition', fontsize=16)
plt.axhline(0, color='black', linewidth=0.7)
plt.axvline(0, color='black', linewidth=0.7)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.axis('equal')
plt.show()

