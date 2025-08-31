import matplotlib.pyplot as plt

# Step 1: Assume coordinates for P and Q
P = (0, 0)
Q = (4, 0)

# Step 2: Find coordinates of R (divides PQ in ratio 3:1)
R_x = (3 * Q[0] + 1 * P[0]) / 4
R_y = (3 * Q[1] + 1 * P[1]) / 4
R = (R_x, R_y)

# Step 3: Find coordinates of S (midpoint of PR)
S_x = (P[0] + R[0]) / 2
S_y = (P[1] + R[1]) / 2
S = (S_x, S_y)

# Step 4: Plot all points
plt.figure(figsize=(6, 4))
plt.plot([P[0], Q[0]], [P[1], Q[1]], 'k-', label='PQ')
plt.plot([P[0], R[0]], [P[1], R[1]], 'g--', label='PR')
plt.scatter(*P, color='blue', label='P (0,0)')
plt.scatter(*Q, color='red', label='Q (4,0)')
plt.scatter(*R, color='orange', label='R')
plt.scatter(*S, color='purple', label='S')

# Annotate points
plt.text(P[0], P[1]+0.2, 'P', ha='center')
plt.text(Q[0], Q[1]+0.2, 'Q', ha='center')
plt.text(R[0], R[1]+0.2, 'R', ha='center')
plt.text(S[0], S[1]+0.2, 'S', ha='center')

plt.legend()
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Points P, Q, R, S on Line Segment')
plt.axis('equal')
plt.savefig("graph.png") 
plt.show()
