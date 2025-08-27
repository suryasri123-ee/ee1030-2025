#include <stdio.h>
#include <math.h>

int main() {
    // Wind (NE at 72 km/h)
    double W_x = 72 * cos(M_PI/4);
    double W_y = 72 * sin(M_PI/4);

    // Boat (North at 51 km/h)
    double V_x = 0;
    double V_y = 51;

    // Relative wind = Wind - Boat
    double R_x = W_x - V_x;
    double R_y = W_y - V_y;

    printf("Relative wind: (%.2f, %.2f)\n", R_x, R_y);
    return 0;
}