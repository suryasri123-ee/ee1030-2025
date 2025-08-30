#include <math.h>
void midpoint(double *A , double *B , double *M , int m )
{
    
    for ( int i = 0 ; i < m ; i++ )
    {
        M[i] = (A[i]+B[i])/ 2.0 ;
    }
    
}

void rotate(double *IN , double *OP , double theta )
{
    theta = M_PI / 180.0 * theta ; // converting to radian
    OP[0] = cos(theta)*IN[0] - sin(theta)*IN[1] ; 
    OP[1] = sin(theta) * IN[0] + cos(theta) * IN[1] ; 
}
