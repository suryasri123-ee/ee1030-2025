import numpy as np
import matplotlib.pyplot as plt

# Define the points of the quadrilateral
A = np.array([6, 2])
B = np.array([2, 1])
C = np.array([1, 5])
D = np.array([5, 6])

# Function to compute distance between two points
def distance(P, Q):
    return np.linalg.norm(P - Q)

# Compute the lengths of all four sides
AB = distance(A, B)
BC = distance(B, C)
CD = distance(C, D)
DA = distance(D, A)

# Compute the lengths of the diagonals
AC = distance(A, C)
BD = distance(B, D)

# Print side lengths
print("Side Lengths:")
print(f"AB = {AB:.2f}, BC = {BC:.2f}, CD = {CD:.2f}, DA = {DA:.2f}")

# Print diagonal lengths
print("\nDiagonal Lengths:")
print(f"AC = {AC:.2f}, BD = {BD:.2f}")

# Check if all sides are equal
all_sides_equal = np.allclose([AB, BC, CD, DA], AB, atol=1e-8)

# Check if both diagonals are equal
diagonals_equal = np.isclose(AC, BD, atol=1e-8)

# Final decision
print("\nChecks:")
print("All sides equal?", all_sides_equal)
print("Diagonals equal?", diagonals_equal)

if all_sides_equal and diagonals_equal:
    print("\n✅ The quadrilateral ABCD is a SQUARE.")
else:
    print("\n❌ The quadrilateral ABCD is NOT a square.")

# ------- Plotting -------
points = [A, B, C, D, A]  # Loop back to A to complete the quadrilateral
x = [p[0] for p in points]
y = [p[1] for p in points]

plt.figure(figsize=(6,6))
plt.plot(x, y, 'k-', linewidth=2)

# Mark points and labels
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'orange']
for pt, lbl, clr in zip(points[:-1], labels, colors):
    plt.plot(pt[0], pt[1], 'o', color=clr, markersize=8)
    plt.text(pt[0] + 0.2, pt[1] + 0.2, f'{lbl}({pt[0]},{pt[1]})', fontsize=12, color=clr)

# Draw diagonals
plt.plot([A[0], C[0]], [A[1], C[1]], 'r--', label='AC (Diagonal)', linewidth=1.5)
plt.plot([B[0], D[0]], [B[1], D[1]], 'b--', label='BD (Diagonal)', linewidth=1.5)

plt.title("Quadrilateral ABCD with Diagonals")
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
