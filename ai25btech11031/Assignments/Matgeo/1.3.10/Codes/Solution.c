#include <stdio.h>

void find_y_and_ratio() {
    double x1=1, y1=2, x2=2, y2=3;
    double xp=8, yp;
    double k;

    // solve for ratio using x-coordinate
    k = (xp - x1) / (x2 - xp);

    // solve for y-coordinate
    yp = (k*y2 + y1) / (k+1);

    printf("Ratio = %.2f : 1\n", k);
    printf("y = %.2f\n", yp);
}

int main() {
    find_y_and_ratio();
    return 0;
}