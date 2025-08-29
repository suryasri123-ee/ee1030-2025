import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

A = np.array([4, 2, 0])
B = np.array([8, 4, 0])

P = A - 0.5 * (B - A)

extended_line = np.array([P, A, B])
extended_line_x = extended_line[:, 0]
extended_line_y = extended_line[:, 1]
extended_line_z = extended_line[:, 2]

ax.plot(extended_line_x, extended_line_y, extended_line_z, 'b--', alpha=0.7, label='Extended Line')
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], 'g-', linewidth=3, label='Segment AB')

ax.scatter(*A, color='red', s=100, label='Point A (4, 2, 0)')
ax.scatter(*B, color='blue', s=100, label='Point B (8, 4, 0)')
ax.scatter(*P, color='purple', s=100, label='Point P (2, 1, 0)')

ax.text(A[0], A[1], A[2], "A", fontsize=12, color='red')
ax.text(B[0], B[1], B[2], "B", fontsize=12, color='blue')
ax.text(P[0], P[1], P[2], "P", fontsize=12, color='purple')

midpoint = (A + P) / 2
ax.text(midpoint[0], midpoint[1], midpoint[2], "AP = 1/2 AB", fontsize=10, color='purple')

ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

ax.set_title('Point P on Extension of Segment AB (AP = 1/2 AB)', fontsize=14)

ax.grid(True)
ax.legend()

max_range = np.array([extended_line_x.max()-extended_line_x.min(), 
                      extended_line_y.max()-extended_line_y.min(), 
                      extended_line_z.max()-extended_line_z.min()]).max() / 2.0
mid_x = (extended_line_x.max()+extended_line_x.min()) * 0.5
mid_y = (extended_line_y.max()+extended_line_y.min()) * 0.5
mid_z = (extended_line_z.max()+extended_line_z.min()) * 0.5
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

ax.view_init(elev=20, azim=-60)

plt.tight_layout()
plt.show()