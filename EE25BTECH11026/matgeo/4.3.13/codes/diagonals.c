#include <stdio.h>

typedef struct {
    double A, B, C;  // Line coefficients Ax + By + C = 0
} Line;

// Function to compute line equation given two points (x1,y1), (x2,y2)
Line line_from_points(double x1, double y1, double x2, double y2) {
    Line l;
    l.A = y1 - y2;
    l.B = x2 - x1;
    l.C = (x1 * y2) - (x2 * y1);
    return l;
}

// Function to compute diagonals of a square
void diagonals_of_square(double vertices[4][2], Line *diag1, Line *diag2) {
    // vertices order: A, B, C, D
    // Diagonals: AC and BD
    *diag1 = line_from_points(vertices[0][0], vertices[0][1],
                              vertices[2][0], vertices[2][1]);
    *diag2 = line_from_points(vertices[1][0], vertices[1][1],
                              vertices[3][0], vertices[3][1]);
}

// Export function for Python
__attribute__((visibility("default"))) 
void get_square_diagonals(double vertices[4][2], double *out) {
    Line d1, d2;
    diagonals_of_square(vertices, &d1, &d2);

    // Store results in array: [A1, B1, C1, A2, B2, C2]
    out[0] = d1.A;
    out[1] = d1.B;
    out[2] = d1.C;
    out[3] = d2.A;
    out[4] = d2.B;
    out[5] = d2.C;
}

