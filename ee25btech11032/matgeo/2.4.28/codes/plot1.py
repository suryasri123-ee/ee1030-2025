import ctypes
import numpy as np
import matplotlib.pyplot as plt
handc1 = ctypes.CDLL("./func.so")

handc1.midpoint.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_int
]

handc1.midpoint.restype = None
A = np.array([[-5],[-2]], dtype=np.float64).reshape(-1,1)
B = np.array([[4],[-2]], dtype=np.float64).reshape(-1,1)
M = np.zeros(2,dtype=np.float64).reshape(-1,1)

handc1.midpoint (
    A.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    B.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    M.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),2
)
AB = np.array([[9],[0]],dtype=np.float64)
theta = 90
handc1.rotate.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_double
]

handc1.rotate.restype = None

per = np.zeros(2,dtype=np.float64).reshape(-1,1)

handc1.rotate(
    AB.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    per.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),theta
)

Q = M + 2 / 9 * per

def line_cre(P: np.ndarray , Q: np.ndarray, str):
    handc2 = ctypes.CDLL("./line_gen.so")

    handc2.linegen.argtypes = [
        ctypes.POINTER(ctypes.c_double),
        ctypes.POINTER(ctypes.c_double),
        ctypes.POINTER(ctypes.c_double),
        ctypes.POINTER(ctypes.c_double),
        ctypes.c_int , ctypes.c_int
    ]

    handc2.linegen.restype = None
    n = 200
    X_l = np.zeros(n,dtype=np.float64)
    Y_l = np.zeros(n,dtype=np.float64)

    handc2.linegen (
        X_l.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        Y_l.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        P.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        Q.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        n,2
    )
    plt.plot([X_l[0],X_l[-1]],[Y_l[0],Y_l[-1]],str)



plt.figure()

line_cre(A,B,"g-")
line_cre(Q,M,"r-")

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
                 ha='center', va = 'bottom')

plt.xlim([-6,6])
plt.ylim([-4,2])
plt.xlabel('$x$')
plt.ylabel('$y$')
#plt.legend(loc='best')
plt.grid()

plt.title("Fig:2.4.28")
#plt.axis('equal')

plt.savefig("../figs/perpbisector1.png")
plt.show()

#plt.savefig('figs/triangle/ang-bisect.pdf')
#subprocess.run(shlex.split("termux-open figs/triangle/ang-bisect.pdf"))


