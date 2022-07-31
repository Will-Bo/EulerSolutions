// What is the largest prime factor of the number 600851475143 ?

#include<stdio.h>
#include<math.h>

// A struct to store the factorization. Not necessary for this solution, but would be useful if we wanted to do anything else with the prime factorization of this number
typedef struct{
    long greatest;
    long factors[9000];
}
factorization;

factorization primeFactor(long n){
    // Keeping the factorization list and greatest value in a struct. 
    factorization f;
    // Keeping an index for the factorization list
    int count = 0;

    // Processing all factors of 2 of the number
    while(n%2 == 0){
        if (f.factors[count] != 2){
            f.factors[count] = 2;
            count++;
        }

        n = n/2;
    }

    // Processing all non-2 factors of the number
    for(int i = 3; i <= (int)(pow(n, .5)); i += 2){
        while(n%i == 0){
            if(f.factors[count] != i){
                f.factors[count] = i;
                count++;
            }
            n = n/i;
        }
    }

    // If there is possibly anything left after that pass, it must also be prime. This will be our largest prime factor, if it exists (see comment above return statement)
    if (n > 2){
        f.factors[count] = n;
        count++;
    }

    // We know that the greatest prime factor will be the last factor that was processed, meaning that we can just check the last item that was added to factors
    f.greatest = f.factors[count-1];

    return f;

}

int main(void){
    printf("The largest prime factor of 13195 is: %i\n",primeFactor(13195).greatest);
    printf("The largest prime factor of 600851475143 is: %li\n",primeFactor(600851475143).greatest);

    return 0;
}
