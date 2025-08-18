//Code by Darsh Gajare
//August 18, 2025
//Drawing bar graph and finding max and min
#include <stdio.h>
#include <stdlib.h>
// declaring function
void compare(char *colours[], int students[], int n);
void printBarGraph(char *colours[], int students[], int n);
// main function
int main()
{
	char *colours[] = {"Red", "Green", "Blue", "Yellow", "Orange"};
	int students[] = {43, 19, 55, 49, 34};
	int n=5;
	printBarGraph(colours, students,n);
	compare(colours,students,n);
	return 0;
}

// Finding most and least preferred colour
void compare(char *colours[], int students[], int n)
{
	int min, max;
	for(int i=1;i<n;i++)
	{
		if (students[i] > students[max])
			max=i;
		if (students[i] < students[min])
			min=i;
	}
	printf("Most preferred colour: %s \n", colours[max]);
	printf("Least preferred colour: %s \n", colours[min]);
}
//Printing Bar graph
void printBarGraph(char *colours[], int students[],int n)
{
	int i, j , maxheight;
	for(i=0;i<n;i++)
		if (students[i]>maxheight)
		{	maxheight = students[i];}
	for (i=maxheight;i>=1;i--)
	{
		for(j=0;j<n;j++){
			if(students[j]>=i)
				printf("\t*\t");
			else
				printf("\t \t");
		}
		printf("\n");
	}
	for (i=0;i<n;i++)
		printf("%-5s \t\t",colours[i]);
	printf("\n");
}
