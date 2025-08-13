//EE25BTECH11062 - Problem 2.2.148
//Percentage of Bangles

#include <stdio.h>

int main(void){
	float gold = 20.0;
	float silver = 10.0;
	float total = gold + silver;
	printf("Percentages in tabular form : \n");
	printf("Type \t Percentage \n");
	printf("Gold \t %.2f\n", gold/total * 100);
	printf("Silver \t %.2f\n", silver/total*100);
	return 0;
}
