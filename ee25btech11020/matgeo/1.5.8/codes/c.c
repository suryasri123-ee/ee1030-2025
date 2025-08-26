#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main()
{
	double A[2]={2,3},B[2]={7,8},P[2]={4,5};
	double k[2];
	FILE *fptr;
	//k(P-B)=(A-P)
	for(int i=0;i<2;i++)
	{
		k[i]=(A[i]-P[i])/(P[i]-B[i]);
	}
	if(k[0]==k[1])
	{
		fptr=fopen("data.dat","w");
		fprintf(fptr,"k=%.02f",k[0]);
		fclose(fptr);
	}
	return 0;
}
