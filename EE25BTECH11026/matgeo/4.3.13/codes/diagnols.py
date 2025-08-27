import ctypes
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp
mp.use('TkAgg')

# Load the shared C library
lib = ctypes.CDLL("./libdiagonals.so")

# Define function signature for C function
lib.get_square_diagonals.argtypes = [ctypes.c_double * 8, ctypes.c_double * 6]

def get_diagonals(vertices):
    """Call C function to compute diagonals of a square"""
    verts = (ctypes.c_double * 8)(*np.array(vertices).flatten())
    out = (ctypes.c_double * 6)()
    lib.get_square_diagonals(verts, out)
    return np.array(out[:]).reshape(2,3)  # [[A1,B1,C1],[A2,B2,C2]]

def format_equation(A, B, C):
    """
    Beautify line equation into readable string.
    Example: -1x + 1y + 0 -> -x + y = 0
    """
    terms = []

    # Ax term
    if A != 0:
        if A == 1:
            terms.append("x")
        elif A == -1:
            terms.append("-x")
        else:
            terms.append(f"{A:g}x")

    # By term
    if B != 0:
        sign = "+" if B > 0 and terms else ""
        if B == 1:
            terms.append(f"{sign}y")
        elif B == -1:
            terms.append(f"{sign}-y")
        else:
            terms.append(f"{sign}{B:g}y")

    # Constant term
    if C != 0:
        sign = "+" if C > 0 and terms else ""
        terms.append(f"{sign}{C:g}")

    if not terms:
        return "0 = 0"

    return " ".join(terms) + " = 0"

# Example: Square vertices (A,B,C,D)
vertices = [(0,0), (1,0), (1,1), (0,1)]
lines = get_diagonals(vertices)

eq1 = format_equation(*lines[0])
eq2 = format_equation(*lines[1])

print("Diagonal AC:", eq1)
print("Diagonal BD:", eq2)

# Plotting
square_x, square_y = zip(*vertices, vertices[0])
plt.plot(square_x, square_y, "b-", label="Square")

# Diagonal AC
plt.plot([vertices[0][0], vertices[2][0]], [vertices[0][1], vertices[2][1]], "r--", label=f"AC: {eq1}")

# Diagonal BD
plt.plot([vertices[1][0], vertices[3][0]], [vertices[1][1], vertices[3][1]], "g--", label=f"BD: {eq2}")

plt.legend(loc="upper right")
plt.gca().set_aspect("equal", adjustable="box")
plt.grid(True)
plt.savefig("/home/user/Matrix/Matgeo_assignments/4.3.13/figs/Figure_1")
plt.show()

