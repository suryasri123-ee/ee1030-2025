import matplotlib.pyplot as plt

# Define the vertices
A = (3, 0)
B = (7, 0)
C = (8, 4)

# Function to calculate area using the Shoelace formula
def triangle_area(A, B, C):
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0

# Calculate area
area = triangle_area(A, B, C)
print(f"Area of triangle ABC: {area:.2f}")

# Prepare points for plotting (repeat the first point at the end to close the triangle)
x = [A[0], B[0], C[0], A[0]]
y = [A[1], B[1], C[1], A[1]]

# Plot triangle sides
plt.plot(x, y, 'r-', linewidth=2)
# Mark vertices
plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], color='blue', zorder=5)
# Label vertices
for point, label in zip([A, B, C], ['A', 'B', 'C']):
    plt.text(point[0], point[1], label, fontsize=12, ha='left', va='bottom')
plt.title(f'Triangle ABC with area = {area:.2f}')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.savefig('fig1.png')
plt.close()

