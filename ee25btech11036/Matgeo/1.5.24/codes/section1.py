import sys                            # for path to external scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

# local imports
from libs.line.funcs import *
from libs.triangle.funcs import *
from libs.conics.funcs import circ_gen

# --- Step 1: Rank relation ---
print("Step 1: Rank relation between b and c")
print("General line: ux + vy + w = 0")
print("Points: P = (0,b), Q = (c,0)")
print("=> vb + w = 0,   uc + w = 0")
print("Subtracting => v b = u c   (Relation 1)\n")

# --- Step 2: Midpoint relation ---
print("Step 2: Midpoint relation")
M = np.array(([2, -5])).reshape(-1,1)
print("Midpoint M = ((0+c)/2, (b+0)/2) = (2, -5)")
c = 2 * M[0,0]
b = 2 * M[1,0]
print(f"c/2 = 2  =>  c = {c}")
print(f"b/2 = -5 =>  b = {b}   (Relation 2)\n")

# --- Step 3: Solve both relations ---
P = np.array(([0,b])).reshape(-1,1)
Q = np.array(([c,0])).reshape(-1,1)

print("Step 3: Solve both relations")
print(f"Coordinates of P = (0, {b})")
print(f"Coordinates of Q = ({c}, 0)\n")

# --- Step 4: Plotting ---
x_PQ = line_gen(P,Q)
plt.plot(x_PQ[0,:], x_PQ[1,:], label='$PQ$')

# Mark points
coords = np.block([[P,Q,M]])
vert_labels = ['P','Q','M']
plt.scatter(coords[0,:], coords[1,:], color=['green','red','magenta'])
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({coords[0,i]:.0f},{coords[1,i]:.0f})',
                 (coords[0,i], coords[1,i]),
                 textcoords="offset points", xytext=(20,-10), ha='center')

# Axis styling
ax = plt.gca()
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.legend(loc='best')
plt.grid()
plt.axis('equal')

# Save figure as PDF
outfile_pdf = 'chapters/10/7/2/2/figs/fig.pdf'
plt.savefig(outfile_pdf)

# Save figure as PNG
outfile_png = 'chapters/10/7/2/2/figs/fig.png'
plt.savefig(outfile_png, dpi=300)

# Open image depending on system
try:
    import platform, subprocess, shlex
    if "termux" in platform.platform().lower():   # Android Termux
        subprocess.run(shlex.split(f"termux-open {outfile_png}"))
    else:                                        # Linux desktop
        subprocess.run(shlex.split(f"xdg-open {outfile_png}"))
except Exception as e:
    print(f"Could not auto-open file. Saved at {outfile_png}")

