#include <stdio.h>

// Function to compute scalar triple product: a · (b × c)
double triple_product(double a[3], double b[3], double c[3]) {
  double cross[3];

  // Cross product b × c
  cross[0] = b[1] * c[2] - b[2] * c[1];
  cross[1] = b[2] * c[0] - b[0] * c[2];
  cross[2] = b[0] * c[1] - b[1] * c[0];

  // Dot product a · (b × c)
  double result = a[0] * cross[0] + a[1] * cross[1] + a[2] * cross[2];
  return result;
}
