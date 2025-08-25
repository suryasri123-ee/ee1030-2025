import ctypes

lib = ctypes.CDLL('./libdiff.so')

lib.find_mag_diffvector.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.find_mag_diffvector.restype = ctypes.c_double

a = 2.0
b = 3.0
dot = 4.0

diff = lib.find_mag_diffvector(a, b, dot)
print(f"The magnitude of difference vector of a and b is: {diff:.4f}")

