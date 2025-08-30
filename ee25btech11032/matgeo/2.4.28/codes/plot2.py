import math
import sys 
sys.path.insert(0, '/home/kartik-lahoti/matgeo/codes/CoordGeo')
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from line.funcs import *
#from triangle.funcs import *
#from conics.funcs import circ_gen


#if using termux
#import subprocess
#import shlex



A = np.array([-5,-2]).reshape(-1,1)
B = np.array([4,-2]).reshape(-1,1)
M = (A+B)/2
AB = np.array([9,0]).reshape(-1,1)
theta = 90
theta = np.deg2rad(theta)
x,y = AB
x_1 = np.cos(theta)*x - np.sin(theta)*y
y_1 = np.sin(theta)*x + np.cos(theta)*y
per = np.array([x_1,y_1]).reshape(-1,1)

Q = M +2/9*per

def plot_it(P,Q,str):
    x_l = line_gen_num(P,Q,20)
    plt.plot(x_l[0,:],x_l[1,:] , str )

plt.figure()

plot_it(A,B,"g-")
plot_it(M,Q,"r-")



coords = np.block([[A,B,M,Q]])
plt.scatter(coords[0,:],coords[1,:])
vert_labels = ['A','B','M','Q']
#for i , txt in enumerate(vert_labels):
 #   plt.annotate(txt,(coords[0,i],coords[1,i]),textcoords="offset points", xytext=(0,10),ha='center')
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({coords[0,i]:.1f}, {coords[1,i]:.1f})',
                 (coords[0,i], coords[1,i]),
                 textcoords="offset points",
                 xytext=(20,0),
                 ha='center',va ='bottom')
plt.xlim([-6,6])
plt.ylim([-4,2])
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()

plt.title("Fig:2.4.28")
#plt.axis('equal')

plt.savefig("../figs/perpbisector2.png")
plt.show()

#plt.savefig('figs/triangle/ang-bisect.pdf')
#subprocess.run(shlex.split("termux-open figs/triangle/ang-bisect.pdf"))

