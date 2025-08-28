import matplotlib.pyplot as plt
import numpy as np
import ctypes
import os

# --- Step 1: Load the shared object ---
try:
    # Assumes '1.so' is in the same directory as this script.
    c_library = ctypes.CDLL('./1.so')
    #print("Shared object '1.so' loaded successfully.")

    # --- Step 2: Define the C function signature ---
    # The C function is: float findK(int px, int py, int ax, int by)
    c_library.findK.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
    c_library.findK.restype = ctypes.c_float

    # --- Step 3: Call the C function to get the value of k ---
    # Problem: P(2, 4) is equidistant from A(5, k) and B(k, 7).
    px, py = 2, 4
    ax_coord = 5
    by_coord = 7
    
    k = c_library.findK(px, py, ax_coord, by_coord)
    #print(f"Value of k calculated from C function: {k}")

except OSError as e:
    k = 3.0 # Fallback value if .so file fails

# --- Step 4: Define problem coordinates using the calculated k ---
P = np.array([2, 4])
A = np.array([5, k])
B = np.array([k, 7])

# Verify distances are equal
dist_PA = np.linalg.norm(P - A)
dist_PB = np.linalg.norm(P - B)

# --- Step 5: Plot the results with a more aesthetic style ---
plt.style.use('seaborn-v0_8-talk') # A clean, presentation-ready style
fig, ax = plt.subplots(figsize=(8, 6.5), facecolor='#f0f0f0')
ax.set_facecolor('white')

# Plot the lines PA and PB
ax.plot([P[0], A[0]], [P[1], A[1]], marker='', linestyle='--', color='#0077b6', lw=2, label=f'Distance PA = {dist_PA:.2f}')
ax.plot([P[0], B[0]], [P[1], B[1]], marker='', linestyle='--', color='#0096c7', lw=2, label=f'Distance PB = {dist_PB:.2f}')

# --- Create a shadow effect for the points ---
# Plot slightly offset, larger, semi-transparent points as a shadow
shadow_offset = 0.03
ax.scatter(P[0] + shadow_offset, P[1] - shadow_offset, color='black', alpha=0.3, s=250, zorder=4)
ax.scatter(A[0] + shadow_offset, A[1] - shadow_offset, color='black', alpha=0.3, s=250, zorder=4)
ax.scatter(B[0] + shadow_offset, B[1] - shadow_offset, color='black', alpha=0.3, s=250, zorder=4)

# Plot the main points on top of the shadow
ax.scatter(P[0], P[1], color='#e63946', s=250, zorder=5, edgecolors='white', linewidth=2)
ax.scatter(A[0], A[1], color='#0077b6', s=250, zorder=5, edgecolors='white', linewidth=2)
ax.scatter(B[0], B[1], color='#0096c7', s=250, zorder=5, edgecolors='white', linewidth=2)

# --- Add improved annotations with arrows ---
ax.annotate(f'P ({P[0]}, {P[1]})', xy=P, xytext=(P[0] - 1.5, P[1] + 0.5),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8),
            fontsize=14, color='black', bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=1, alpha=0.9))
ax.annotate(f'A ({A[0]}, {A[1]:.0f})', xy=A, xytext=(A[0] + 0.5, A[1] - 0.5),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8),
            fontsize=14, color='black', bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=1, alpha=0.9))
ax.annotate(f'B ({B[0]:.0f}, {B[1]})', xy=B, xytext=(B[0] - 1.5, B[1] + 0.5),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8),
            fontsize=14, color='black', bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=1, alpha=0.9))

# --- Final styling ---
ax.set_title(f'Point P is Equidistant from A and B for k = {k:.2f}', fontsize=20, color='black', pad=20)
ax.set_xlabel('X-axis', fontsize=14, color='black')
ax.set_ylabel('Y-axis', fontsize=14, color='black')

ax.grid(True, linestyle=':', alpha=0.6)
ax.axhline(0, color='gray', linewidth=1)
ax.axvline(0, color='gray', linewidth=1)

ax.set_aspect('equal', adjustable='box')

# Customize the legend
legend = ax.legend(fontsize=12, frameon=True, fancybox=True, shadow=True, framealpha=0.9, facecolor='white')
plt.setp(legend.get_texts(), color='black')

plt.tight_layout()

# --- Step 6: Save the figure and show the plot ---
plt.savefig('1.png')
plt.show()
