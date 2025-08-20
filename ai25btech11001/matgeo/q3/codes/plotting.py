from math import *
import sys   
#sys.path.insert(0, '/storage/emulated/0/Abhisek/Math    /Matrix theory/codes/codes/CoordGeo')        #path t    o my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from line.funcs import *
#from triangle.funcs import *
#from conics.funcs import circ_gen
#if using termux
import subprocess
import shlex
#end if
from mpl_toolkits.mplot3d import Axes3D

x, y, z = 10*cos(pi/4),10*cos(pi/3),10*cos(pi/3)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0, 0, 0, x, y, z, color='black', arrow_length_ratio=0.1)

e1=[1,0,0]
e2=[0,1,0]
e3=[0,0,1]

ax.plot([e1[0],x/10],[e1[1],y/10],[e1[2],z/10],'red')
ax.plot([e2[0],x/10*2],[e2[1]*2,y/10*2],[e2[2],z/10*2],'green')
ax.plot([e3[0],x/10*4],[e3[1],y/10*4],[e3[2]*4,z/10*4],'blue')

ax.text(e1[0],e1[1],e1[2],"45",color="red")
ax.text(e2[0],e2[1],e2[2],"60",color="green")
ax.text(e3[0],e3[1],e3[2],"60",color="blue")
ax.set_xlim([0, max(x, y, z)])
ax.set_ylim([0, max(x, y, z)])
ax.set_zlim([0, max(x, y, z)])
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')


plt.legend(loc='best')
plt.grid() # minor
#plt.axis('equal')

plt.savefig('../figs/img.png')
