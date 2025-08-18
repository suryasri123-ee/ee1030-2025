//Code by Venkata Sai

//August 18, 2025

//find the mean of given data

// To check technique of a teacher is effective or not

#include <stdio.h>

float mean(int *arr,int n);

int main()
{
    int a[]={10,15,12,20,9};
    int n=sizeof(a)/sizeof(*a);
    printf("Mean of Quaterly Test=%f\n",mean(a,n));
    int b[]={15,18,16,21,15};
    n = sizeof(b)/sizeof(*b);
    printf("Mean of Half Yearly Test=%f\n",mean(b,n));
    printf("Net increase in mean=%f\n",mean(b,n)-mean(a,n));
    printf("Effective!\n");
}

float mean(int *arr,int n)
{
    int sum=0;
   for( int i=0;i<n;i++)
   {
   sum =sum+arr[i];
   }
   return (float)sum/n;

}

