#include<stdio.h>
#include<math.h>

double find_magnitude(int result[3])
{
	double mag;
	mag=sqrt(pow(result[0],2)+pow(result[1],2)+pow(result[2],2));
	return mag;

}

void sum_of_vectors(int a[3], int b[3], int c[3], int result[3])
{
    for(int i = 0; i < 3; i++)
    {
        result[i] = a[i] + b[i] + c[i];
    }
}


