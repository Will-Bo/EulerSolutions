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


## Declaring n as 600851475143, then returning the highest prime factor
def main():
    n = 600851475143

    ## Generating every prime number below sqrt(n), then moving through them backwards to find the highest one
    for x in seiveParser(seiveOfEratosthenes(int(n**.5)))[::-1]:
        if n%x == 0:
            return x
    
print(main())
