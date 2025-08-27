#include <stdio.h>
int main(void) {
int Ax = 2, Ay = 1;
int Bx = 0, By = 5;
int Cx = -1, Cy = 2;


// Columns of M: B-A and C-A
int m11 = Bx - Ax; // -2
int m21 = By - Ay; //  4
int m12 = Cx - Ax; // -3
int m22 = Cy - Ay; //  1

// For 2x2, rank=2 iff det != 0
int det = m11 * m22 - m12 * m21;

printf("Matrix M = [[%d, %d],[%d, %d]]\n", m11, m12, m21, m22);
printf("det(M) = %d\n", det);

if (det != 0) {
    printf("rank(M) = 2 -> Points are NOT collinear.\n");
} else if (m11 != 0 || m21 != 0 || m12 != 0 || m22 != 0) {
    printf("rank(M) = 1 -> Points are collinear.\n");
} else {
    printf("rank(M) = 0 (degenerate).\n");
}
return 0;
}
