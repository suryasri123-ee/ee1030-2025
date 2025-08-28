#include <stdio.h>

int main() {
    // Define points
    double Ax = 1.0, Ay = -5.0;
    double Bx = -4.0, By = 5.0;

    // Midpoint (C divides AB in 1:1 ratio)
    double Cx = (Ax + Bx) / 2.0;
    double Cy = (Ay + By) / 2.0;

    // Print points
    printf("%f %f\n", Ax, Ay);
    printf("%f %f\n", Bx, By);
    printf("%f %f\n", Cx, Cy);

    return 0;
}

