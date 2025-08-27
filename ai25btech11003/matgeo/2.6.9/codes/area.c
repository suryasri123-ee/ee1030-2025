#include <stdio.h>
#include <stdlib.h>


double **createMat(int m, int n) {
    double **mat = (double **)malloc(m * sizeof(double *));
    if (!mat) {
        perror("Allocation failed");
        exit(EXIT_FAILURE);
    }
    for (int i = 0; i < m; i++) {
        mat[i] = (double *)malloc(n * sizeof(double));
        if (!mat[i]) {
            perror("Allocation failed");
            for (int k = 0; k < i; k++) free(mat[k]);
            free(mat);
            exit(EXIT_FAILURE);
        }
    }
    return mat;
}


void freeMat(double **mat, int m) {
    for (int i = 0; i < m; i++) {
        free(mat[i]);
    }
    free(mat);
}

int main() {
    int m = 3, n = 3;
    double **mat = createMat(m, n);

    
    mat[0][0] = 3; mat[0][1] = 0; mat[0][2] = 1;
    mat[1][0] = 7; mat[1][1] = 0; mat[1][2] = 1;
    mat[2][0] = 8; mat[2][1] = 4; mat[2][2] = 1;

    
    double det = mat[0][0]*(mat[1][1]*mat[2][2] - mat[1][2]*mat[2][1])
               - mat[0][1]*(mat[1][0]*mat[2][2] - mat[1][2]*mat[2][0])
               + mat[0][2]*(mat[1][0]*mat[2][1] - mat[1][1]*mat[2][0]);

    double area = 0.5 * (det >= 0 ? det : -det);

    printf("Area of the triangle is %.2lf sq.units. \n", area);

    freeMat(mat, m);
    return 0;
}

