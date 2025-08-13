//EE25BTECH11062 - Prob 3.2.58
//Write 4 more numbers in following pattern

#include <stdio.h>

int main(void){
	printf("The next 4 numbers in the series are : \n");
	for(int i = 4; i < 8; i++){
		printf("%d/%d \t", -i, 4*i); 
	}
	printf("\n");
	return 0;
}
