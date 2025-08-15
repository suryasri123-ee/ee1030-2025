#include<stdio.h>

int main(){
	float A[2][2] = {{1,1},{-1,1}};
	float B[2]={180,44};
	float invA[2][2];
	float det;
	float X[2];

	det=A[0][0]*A[1][1] - A[0][1]*A[1][0];

	invA[0][0]= A[1][1] / det;
	invA[0][1]= -A[0][1] / det;
	invA[1][0]= -A[1][0] / det;
	invA[1][1]= A[0][0] / det;

	X[0]=invA[0][0]*B[0] + invA[0][1]*B[1];
	X[1]=invA[1][0]*B[0] + invA[1][1]*B[1];

	printf("Smaller angle = %.2f degrees\n",X[0]);
	printf("Larger angle = %.2f degrees\n",X[1]);

	return 0;
	}
