// File: solver.c
void findCoordinates(int mx, int my, int* c_ptr, int* b_ptr) {
    // Calculate c from the x-coordinate of the midpoint
    *c_ptr = 2 * mx;

    // Calculate b from the y-coordinate of the midpoint
    *b_ptr = 2 * my;
}
