#include <stdio.h>

// Function to find coordinates of P(0,b) and Q(c,0)
// given the midpoint (mx, my)
void findCoordinates(int mx, int my, int* c, int* b) {

    printf("Step 1: Rank relation between b and c\n");
    printf("Line: ux + vy + w = 0\n");
    printf("P = (0,b), Q = (c,0) lie on the line\n");
    printf("=> vb + w = 0,   uc + w = 0\n");
    printf("Subtracting: vb - uc = 0 => v b = u c (relation 1)\n\n");

    printf("Step 2: Midpoint relation\n");
    printf("Midpoint M = ( (0+c)/2, (b+0)/2 ) = (%d, %d)\n", mx, my);
    printf("=> c/2 = %d => c = %d\n", mx, 2*mx);
    printf("=> b/2 = %d => b = %d\n\n", my, 2*my);

    // Assign values using midpoint
    *c = 2 * mx;
    *b = 2 * my;

    printf("Step 3: Solve both relations\n");
    printf("Coordinates of P = (0,%d)\n", *b);
    printf("Coordinates of Q = (%d,0)\n\n", *c);
}

