## By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
## What is the 10 001st prime number?

from math import sqrt

def genPrimes(n):
    prime = 0
    number = 2
    while prime < n:
        ## You only have to check up to the square root of the number that you're looking at
        lastCheck = sqrt(number)

        isPrime = True
        i = 2
        while i <= lastCheck:
            if number % i == 0:
                i += 1
                isPrime = False
                ## Break out of the while loop early to save on useless iterations
                break
            i += 1
        if isPrime:
            prime += 1

        number += 1
    ## To correct the final += 1 that occurs after the final prime is found
    number -= 1
    return number

print(genPrimes(10001))

