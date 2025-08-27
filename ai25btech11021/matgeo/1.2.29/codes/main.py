import numpy as np
import matplotlib.pyplot as plt

# Wind velocity (ground frame), NE direction at 72 km/h
W = np.array([72/np.sqrt(2), 72/np.sqrt(2)])  # [East, North]

# Boat velocity (ground frame), north at 51 km/h
V = np.array([0, 51])  # [East, North]

# Relative wind (wind seen from boat)
R = W - V

# Calculate angle of relative wind
angle_deg = np.degrees(np.arctan2(R[1], R[0]))

print("Wind vector W =", W)
print("Boat vector V =", V)
print("Relative wind R =", R)
print("Angle of relative wind =", angle_deg, "degrees")

# Create plot
plt.figure(figsize=(6,6))
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)

# Plot vectors
plt.quiver(0,0, W[0], W[1], angles='xy', scale_units='xy', scale=1, color='blue', label="Wind (ground)")
plt.quiver(0,0, V[0], V[1], angles='xy', scale_units='xy', scale=1, color='green', label="Boat (ground)")
plt.quiver(0,0, R[0], R[1], angles='xy', scale_units='xy', scale=1, color='red', label="Relative Wind")

# Labels
plt.text(W[0], W[1], " W", fontsize=12)
plt.text(V[0], V[1], " V", fontsize=12)
plt.text(R[0], R[1], " R", fontsize=12)

plt.xlim(-10,80)
plt.ylim(-10,80)
plt.xlabel("East (+x)")
plt.ylabel("North (+y)")
plt.title("Relative Wind Seen from Boat")
plt.legend()
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()