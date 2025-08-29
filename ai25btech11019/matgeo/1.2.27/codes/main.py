import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

horizontal = 10.0  # northward (horizontal component), in m/s
vertical = 30.0    # downward (vertical component), in m/s

theta_rad = np.arctan(horizontal / vertical)
theta_deg = np.degrees(theta_rad)

print(f"Horizontal component (north) = {horizontal:.1f} m/s")
print(f"Vertical component (down)   = {vertical:.1f} m/s\n")
print(f"tan(theta) = {horizontal:.1f} / {vertical:.1f} = {horizontal/vertical:.2f}")
print(f"theta = arctan({horizontal/vertical:.2f}) ≈ {theta_deg:.2f} degrees\n")
print("Conclusion: In her frame the rain comes from slightly ahead (from the south and above),")
print("so she should tilt the umbrella forward (toward the direction of motion, i.e., south)")
print(f"by {theta_deg:.2f} degrees from the vertical.")
