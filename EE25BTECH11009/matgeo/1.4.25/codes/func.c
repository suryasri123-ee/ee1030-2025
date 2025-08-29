
void section(double *P , double *Q , double *R , int m)
{
	for (int i = 0 ; i < m ; i++)
	{
		R[i] = (Q[i] - 2 * P[i] )/(1-2) ;
	}
}

void line_gen (double *X, double *Y , double *A , double *B , int n , int m )
{
    double temp[m] ; 
    for (int i = 0 ; i < m ; i++)
    {
        temp [ i ] = (B[i]- A[i]) /(double) n ; 
    }
    for (int i = 0 ; i <= n ; i++ )
    {
        X[i] = A[0] + temp[0] * i ; 
        Y[i] = A[1] + temp[1] * i ;
    }
}
