// By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#include<stdio.h>

// Creating an array that is large enough to hold every Fibonacci number that is needed for this problem -- will help to save time when performing the actual calculations
long fibTable[101];

// Calculating the Fibonacci sequence, using the fibTable to cache found results and avoid redundant calculations
long fib(int n){
    if (n <= 1){
        return (long)1;
    }

    // Redundancy check
    if (fibTable[n] != 0){
        return fibTable[n];
    }
    else{
        fibTable[n] = fib(n-1) + fib(n-2);
        return fibTable[n];
    }
}


// This function calls fib, then calculates the sum of even values below 4,000,000
long sumEven(long max){
    long f = fib(max);

    int i = 0;
    long sum = 0;

    // Moving through the fibTable until the values are above 4,000,000, adding all even values to the sum
    while(fibTable[i] < 4000000){
        if (fibTable[i] % 2 == 0){
            sum += fibTable[i];
        }
        i++;
    }
    return sum;
}


int main(void){
    // Initializing the fibTable with 0s to avoid garbage values
    for (int i = 0; i < 101; i++){
        fibTable[i] = 0;
    }
   

    // Finding up to the 100th Fibonacci number. Not a very scientific way for finding all Fibonacci numbers below 4,000,000, but we know that 4,000,000 will be less than fib(100) and this allows us to size an array to hold the values
    long answer = sumEven(100);
    printf("%li\n", answer);

    return 0;
}
