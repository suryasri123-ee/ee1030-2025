import sys                            # for path to external scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# local imports
from libs.line.funcs import *
from libs.triangle.funcs import *
from libs.conics.funcs import circ_gen

# if using termux
import subprocess
import shlex
# end if

# Midpoint given
M = np.array(([2, -5])).reshape(-1,1)

# Let P = (0,b), Q = (c,0)
# From midpoint formula: (c/2, b/2) = (2, -5)
c = 4
b = -10

# Coordinates
P = np.array(([0,b])).reshape(-1,1)
Q = np.array(([c,0])).reshape(-1,1)

# Generating line PQ
x_PQ = line_gen(P,Q)

# Plotting the line
plt.plot(x_PQ[0,:], x_PQ[1,:], label='$PQ$')

# Plot midpoint
plt.scatter(M[0,:], M[1,:], color='red', label='Midpoint M')

# Labeling the coordinates
coords = np.block([[P,Q,M]])
vert_labels = ['P','Q','M']
plt.scatter(coords[0,:], coords[1,:])
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({coords[0,i]:.0f}, {coords[1,i]:.0f})',
                 (coords[0,i], coords[1,i]),
                 textcoords="offset points",
                 xytext=(20,-10),
                 ha='center')

# Axis styling
ax = plt.gca()
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.legend(loc='best')
plt.grid()
plt.axis('equal')

outfile = 'chapters/10/7/2/2/figs/fig.pdf'
plt.savefig(outfile)

# Save figure as PNG
outfile = 'chapters/10/7/2/2/figs/fig.png'
plt.savefig(outfile, dpi=300)

# Open image depending on system
try:
    import platform
    import subprocess, shlex

    if "termux" in platform.platform().lower():   # Android Termux
        subprocess.run(shlex.split(f"termux-open {outfile}"))
    else:                                        # Linux desktop
        subprocess.run(shlex.split(f"xdg-open {outfile}"))
except Exception as e:
    print(f"Could not auto-open file. Saved at {outfile}")

#else
#plt.show()

