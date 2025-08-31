#include <stdio.h>

// For 2D vectors; change n to 3 for 3D.
#define n 2

void find_S(double P[], double Q[], double S[]) {
    // S = (5P + 3Q) / 8
    for (int i = 0; i < n; i++) {
        S[i] = (5 * P[i] + 3 * Q[i]) / 8.0;
    }
}

int main() {
    double P[n], Q[n], S[n];

    // Input coordinates for P and Q
    printf("Enter coordinates for P (x y): ");
    for (int i = 0; i < n; i++) scanf("%lf", &P[i]);

    printf("Enter coordinates for Q (x y): ");
    for (int i = 0; i < n; i++) scanf("%lf", &Q[i]);

    find_S(P, Q, S);

    printf("Coordinates of S: (%.3lf, %.3lf)\n", S[0], S[1]);
    return 0;
}