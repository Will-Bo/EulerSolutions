## The prime factors of 13195 are 5, 7, 13 and 29.
## What is the largest prime factor of the number 600851475143?

## Solution #1 -- Use a Sieve of Eratosthenes to create all prime numbers below sqrt(600851475143), then iterate backwards through that list to find the largest prime factor


## Takes in a boolean array and returns the indices of True elements, effectively giving us the prime     numbers from our Seive function
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
        
        ## Marking every possible composite number in the array as False, leaving only prime numbers a    s True
        if arr[i] == True:
            j = i**2
            k = 0
            while j <= n:
                arr[j] = False
                k += 1
                j = i**2 + k*i

    return arr

## Runner function for Solution #1
def solution1Runner(n):
    ## Generating every prime number below sqrt(n), then moving through them backwards to find the highest one
    for x in seiveParser(seiveOfEratosthenes(int(n**.5)))[::-1]:
        if n%x == 0:
            return x


## Solution #2 -- Actually generate prime factorization and find the largest element
def primeFactor(n):

    factors = []

    ## Taking out every factor of 2
    while n%2 == 0:
        factors.append(2)
        n = n/2

    ## Moving through every odd number and factoring it out. Anything left by this process (moving up through 3, 5, etc.) will be prime
    for i in range(3, int(n**.5) + 1, 2):
        while n%i == 0:
            factors.append(i)
            n = n/i

    ## Maybe the resulting n is still a prime factor
    if n > 2:
        factors.append(n)

    return factors

## Returning the greatest prime factor
def findGPF(factors):
    return max(factors)


## Calling the runners for solutions #1 and #2
def main():
    n = 600851475143
    print("Solution #1:",solution1Runner(n))
    print("Solution #2:",findGPF(primeFactor(n)))

main()


## This function tests how long each solution takes -- showing that Solution #2 is roughly 20 times faster than Solution #1 on my computer (.5 ms versus .026 ms)
def timeTest():
    n = 600851475143
    from time import time
    start = time()
    print("Solution #1 of",solution1Runner(n),"takes",time()-start,"milliseconds")
    start = time()
    print("Solution #2 of",findGPF(primeFactor(n)),"takes",time()-start,"milliseconds")

#timeTest()
