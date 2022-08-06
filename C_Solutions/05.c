// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#include<stdio.h>

int fasterDivisible(int step){
    int val = step;

    // We only need to check division by these numbers. If any number is divisible by all of these, then it must be divisible by the other numbers due to their properties of division
    int check[] = {11, 13, 14, 16, 17, 18, 19, 20};

    // The check array is 8 integers long -- storing this for ease in traversal
    int CHECKLEN = 8;

    // We know that there is a number that is divisible by all numbers, so it will eventually return something. The infinite while loop ensures that we reach that number.
    while (1){
        int flag = 1;

        // If anything isn't divisible by one of the significant numbers, then the flag is set to false and we move onto the next number
        for (int i = 0; i < CHECKLEN; i++){
            if (val % check[i] != 0){
                flag = 0;
            }
        }

        if (flag == 1){
            return val;
        }

        val += step;
    }

    return 0;
}

int main(void){
    // We can use a step of 2520 because that is the least common multiple of 2-10
    printf("The smallest number divisible by 1 through 20 is %i\n", fasterDivisible(2520));

    return 0;
}
