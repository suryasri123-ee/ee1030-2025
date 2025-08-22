#include<stdio.h>
#include<math.h>
double calculate_lambda(double xp, double xq, double xr) {
    if (xr - xq == 0.0) {
        printf("Error: Division by zero. xr cannot be equal to xq.\n");
        return -1.0; // Return an error value
    }
    return (xp - xr) / (xr - xq);
}
