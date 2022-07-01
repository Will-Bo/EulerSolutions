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

## Wrapping the other functions into a sum call
def primeSummation(n):
    return sum(seiveParser(seiveOfEratosthenes(n)))

print(primeSummation(10))
print(primeSummation(2000000))
