// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
// Find the sum of all the multiples of 3 or 5 below 1000.

#include<stdio.h>

// Finding all of the multiples of 'step' that are below 'max', returning the sum of those numbers
int findMults(int step, int max){
    int sum = 0;
    int i = step;

    while (i < max){
        sum += i;
        i += step;
    }

    return sum;
}

// Finding all of the multiples of 'b' that are divisible by 'a' below 'max', returning the sum of those numbers
int findBoth(int a, int b, int max){
    int sum = 0;
    int i = b;
    while (i < max){
        if (i%a == 0){
            sum += i;
        }
        i += b;
    }

    return sum;
}

// By finding the sum of the multiples of 3, then the sum of the multiples of both, and subtracting the multiples of both, we find the sum of all multiples of 3 or 5 below 1000
int main(){
    printf("The sum of multiples of 3 or 5 below 1000 is %d\n", (findMults(3,1000)+findMults(5,1000)-findBoth(3, 5, 1000)));

    return 0;
}
