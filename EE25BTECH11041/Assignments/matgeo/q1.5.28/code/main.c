#include <stdio.h>

void trisec(double x1, double y1, double x2, double y2, double* a, double* b, double* c, double* d){
    *a= (x1+2*x2)/3;
    *b= (y1+2*y2)/3;
    *c= (2*x1+x2)/3;
    *d= (2*y1+y2)/3;
}