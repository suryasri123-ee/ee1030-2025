import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given points
A = (-2, 3, 5)
B = (1, -4, 6)

# Internal division (2:3)
P = ((2*B[0] + 3*A[0]) / 5,
     (2*B[1] + 3*A[1]) / 5,
     (2*B[2] + 3*A[2]) / 5)

# External division (2:3)
Q = ((2*B[0] - 3*A[0]) / (2-3),
     (2*B[1] - 3*A[1]) / (2-3),
     (2*B[2] - 3*A[2]) / (2-3))

print("Internal Division Point:", P)
print("External Division Point:", Q)

# Plotting
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')

# Line segment AB
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], color='blue')

# Points with labels
def plot_point(pt, label, color):
    ax.scatter(*pt, color=color, s=60)
    ax.text(pt[0], pt[1], pt[2], f"{label}{pt}", fontsize=10)

plot_point(A, "A", "red")
plot_point(B, "B", "red")
plot_point(P, "P", "green")   # internal
plot_point(Q, "Q", "purple")  # external

# Labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Division of Line Segment')

# Adjust axes (zoom appropriately)
ax.set_xlim(-10, 5)
ax.set_ylim(-10, 20)
ax.set_zlim(0, 10)

plt.show()
