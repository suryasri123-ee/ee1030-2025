import matplotlib as mp
mp.use("TkAgg")
import numpy as np
import matplotlib.pyplot as plt

def line_equation_cartesian(point, direction):
    """
    Returns line equation in Cartesian form: Ax + By + C = 0
    given a point and a direction vector.
    """
    x0, y0 = point
    a, b = direction
    
    # Normal vector
    A, B = -b, a
    C = -(A*x0 + B*y0)
    return A, B, C

def diagonals_of_square(vertices):
    """
    Given 4 vertices of a square (in order), compute equations of diagonals in Cartesian form.
    """
    A, B, C, D = vertices
    
    # Diagonals are AC and BD
    AC_dir = (C[0]-A[0], C[1]-A[1])
    BD_dir = (D[0]-B[0], D[1]-B[1])
    
    line1 = line_equation_cartesian(A, AC_dir)
    line2 = line_equation_cartesian(B, BD_dir)
    
    return line1, line2

def format_equation(A, B, C):
    """
    Beautify line equation into readable string.
    Example: -1x + 1y + 0 -> -x + y = 0
    """
    terms = []

    # Handle Ax term
    if A != 0:
        if A == 1:
            terms.append("x")
        elif A == -1:
            terms.append("-x")
        else:
            terms.append(f"{A}x")

    # Handle By term
    if B != 0:
        sign = "+" if B > 0 and terms else ""
        if B == 1:
            terms.append(f"{sign}y")
        elif B == -1:
            terms.append(f"{sign}-y")
        else:
            terms.append(f"{sign}{B}y")

    # Handle C constant term
    if C != 0:
        sign = "+" if C > 0 and terms else ""
        terms.append(f"{sign}{C}")

    # In case all are zero
    if not terms:
        return "0 = 0"

    return " ".join(terms) + " = 0"

def plot_square_and_diagonals(vertices, line1, line2):
    """
    Plot square and its diagonals with equations shown on the plot.
    """
    A, B, C, D = vertices
    square_x = [A[0], B[0], C[0], D[0], A[0]]
    square_y = [A[1], B[1], C[1], D[1], A[1]]
    
    plt.plot(square_x, square_y, 'b-', label='Square')
    
    # Plot diagonals
    plt.plot([A[0], C[0]], [A[1], C[1]], 'r--', label='Diagonal AC')
    plt.plot([B[0], D[0]], [B[1], D[1]], 'g--', label='Diagonal BD')
    
    # Equations
    eq1 = format_equation(*line1)
    eq2 = format_equation(*line2)
    
    # Midpoints of diagonals
    mid_AC = ((A[0]+C[0])/2, (A[1]+C[1])/2)
    mid_BD = ((B[0]+D[0])/2, (B[1]+D[1])/2)
    
    # Place texts with slight offsets to avoid overlap
    plt.text(mid_AC[0]+0.05, mid_AC[1]+0.05, eq1, color='red', fontsize=10, ha='left')
    plt.text(mid_BD[0]-0.15, mid_BD[1]-0.1, eq2, color='green', fontsize=10, ha='right')
    
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend(loc="upper right")
    plt.grid(True)
    plt.savefig("/home/user/Matrix/Matgeo_assignments/4.3.13/figs/Figure_1")
    plt.show()

# Example input: square with vertices (in order A, B, C, D)
vertices = [(0,0), (1,0), (1,1), (0,1)]

# Compute diagonal equations
line1, line2 = diagonals_of_square(vertices)

print("Equation of diagonal AC:", format_equation(*line1))
print("Equation of diagonal BD:", format_equation(*line2))

# Plot with equations
plot_square_and_diagonals(vertices, line1, line2)

