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

## Solution #2
## Generating prime numbers more efficiently -- generate a number of prime numbers find the nth prime number. 
def betterGenPrimes(n):
    ## The first time, we only generate the primes below 200,000. This is a reasonable bet that most people will want a prime that is less than this number
    try:

        tmp = seiveParser(seiveOfEratosthenes(200000))[n-1]
        if tmp is not None:
            return tmp
    except:
    ## If we don't find our desired prime below 200,000, we generate all primes below 1,000,000 and tries to find it in that
        return seiveParser(seiveOfEratosthenes(1000000))[n-1]

## seive of Eratosthenes from Problem 10:
## Takes in a boolean array and returns the indices of True elements, effectively giving us the prime numbers from our Seive function
def seiveParser(arr):
    ret = []

    for i in range(2,len(arr)):
        if arr[i] == True:
            ret.append(i)

    return ret

## Implementation of the sieve of Eratosthenes
def seiveOfEratosthenes(n):
    arr = [True]*(n+1)

    ## The upper bound of any prime check is the square root of the number that we are checking up to
    upperBound = int(n**.5)

    ## We want the upper bound to be included in our loop
    for i in range(2, upperBound+1):

        ## Marking every possible composite number in the array as False, leaving only prime numbers as True
        if arr[i] == True:
            j = i**2
            k = 0
            while j <= n:
                arr[j] = False
                k += 1
                j = i**2 + k*i

    return arr

print(betterGenPrimes(10001))

## Checking the run time of the functions, just to see how they compare
## As we can see from the output, using a Seive to find the primes takes about half as much time as the original solution for the 10001st prime
## Using much higher numbers (ex: finding the 50,000th prime), the Seive solution becomes much faster than the original
def timeIt():
    print("Times:")
    import time

    start_time = time.time()
    genPrimes(10001)
    print("Original: %f" %(time.time()-start_time))

    start_time = time.time()
    betterGenPrimes(10001)
    print("Using Seive: %f" %(time.time() - start_time))

#timeIt()
