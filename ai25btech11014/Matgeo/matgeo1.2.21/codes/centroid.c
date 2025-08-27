#include <stdio.h>

void centroid(double* A, double* B, double* G, double* C) {
    for (int i = 0; i < 3; i++) {
        C[i] = 3 * G[i] - A[i] - B[i];
    }
}


