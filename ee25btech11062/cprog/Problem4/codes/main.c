// EE25BTECH11062 - Problem 5.2.31
// Math Library

#include <stdio.h>
#include <math.h>

int main(void){
	float numerator = pow(2,3) * pow(3,4) * 4;
	float denominator = 3 * 32;
	float answer = numerator/denominator;
	printf("The answer is : %.2f\n", answer);
	return 0;
}
