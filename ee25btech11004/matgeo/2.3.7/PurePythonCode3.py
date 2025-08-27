import numpy as np

import matplotlib.pyplot as plt

import sys

import numpy.linalg as LA

import math

vec1 = np.array([1,-2,-2])
vec2 = np.array([3,-6,2])

dot_product = vec1@vec2

norm1 = np.linalg.norm(vec1)
norm2 = np.linalg.norm(vec2)

cos = dot_product/(norm1*norm2)

angle = math.asin(cos)

print(angle*180/3.1415)

import numpy as np
import matplotlib.pyplot as plt


# 1. Set up the figure and 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 2. Define the plane equation: 2x + 3y + 4z = 12
#    We will solve for z: z = (12 - 2x - 3y) / 4

# 3. Create a grid of x and y values
#    np.linspace creates an array of evenly spaced numbers
x = np.linspace(-10, 10, 20)
y = np.linspace(-10, 10, 20)

#    np.meshgrid creates coordinate matrices from coordinate vectors
X, Y = np.meshgrid(x, y)

# 4. Calculate the corresponding Z values
Z = (X-2*Y- 1)/2
z1 = (6*Y - 3*X)/2

# 5. Plot the surface
#    `plot_surface` creates the 3D plane
#    `alpha` sets the transparency of the plane
#    `cmap` sets the color map
ax.plot_surface(X, Y, Z, alpha=1, cmap='Blues')
ax.plot_surface(X, Y, z1, alpha=1, cmap='Oranges')

# 6. Add labels and a title for clarity
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Plot of the planes')

# 7. Display the plot
plt.show()