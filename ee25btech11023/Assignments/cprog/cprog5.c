//Code by Venkata Sai

//August 18, 2025

//Expressing a number as product of prime factors


#include <stdio.h>

void primefactorization(int n) {
    printf("%d = ", n);
    int first = 1;
    for (int i = 2; i * i <= n; i++) {
        int count = 0;
        while (n % i == 0) {
            count++;
            n /= i;
        }
        if (count > 0) {
            if (!first) printf(" * ");
            printf("%d^%d", i, count);
            first = 0;
        }
    }
    if (n > 1) {
        if (!first) printf(" * ");
        printf("%d^1", n);
    }
    printf("\n");
}

int main() {
    int number=432;
     primefactorization(number);
    return 0;
}
