#include <stdio.h>

int main() {
    // Define column matrices
    double A[2] = {5, -6};   // myvec{5 \\ -6}
    double B[2] = {-1, -4};  // myvec{-1 \\ -4}
    double P[2];             // intersection point

    double lambda = 1.0/6.0;
    double mu = 5.0/6.0;

    // Compute P = λA + μB
    P[0] = lambda*A[0] + mu*B[0];
    P[1] = lambda*A[1] + mu*B[1];

    printf("λ = %lf, μ = %lf\n", lambda, mu);
    printf("Intersection point P = myvec{%lf \\\\ %lf}\n", P[0], P[1]);
    printf("Ratio AP:PB = 5:1\n");

    return 0;
}

