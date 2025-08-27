import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Points
A = np.array([2, 1])
B = np.array([0, 5])
C = np.array([-1, 2])

# Collinearity matrix [B-A  C-A]
M = sp.Matrix.hstack(sp.Matrix(B - A), sp.Matrix(C - A))
print("Collinearity matrix M =\n", np.array(M, dtype=int))
print("rank(M) =", M.rank())
print("Conclusion:", "Collinear" if M.rank() == 1 else "NOT collinear")

# Plot and save image
plt.figure(figsize=(4, 4))
pts = np.vstack([A, B, C])
plt.scatter(pts[:, 0], pts[:, 1], color=['tab:blue', 'tab:orange', 'tab:green'], s=80)
for (x, y), label in zip(pts, ['A(2,1)', 'B(0,5)', 'C(-1,2)']):
    plt.annotate(label, (x + 0.05, y + 0.05))  # <-- This must be indented

plt.plot([A[0], B[0]], [A[1], B[1]], 'k--', alpha=0.6)
plt.plot([A[0], C[0]], [A[1], C[1]], 'k--', alpha=0.6)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle=':')
plt.xlim(-2, 4)
plt.ylim(0, 7)
plt.title('Points A, B, C')
plt.tight_layout()
plt.savefig('fig1.png', dpi=150)

