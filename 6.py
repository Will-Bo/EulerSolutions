## Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

## Finding the sum of the squares could be quite expensive computationally, as that's a lot of squaring! However, a formula derived from the difference of cubes equation makes this much faster
def sumOfSquares(n):
    return (n*(n+1)*(2*n+1))/6

## Not excessively expensive to do this calculation iteratively
def squareOfSum(n):
    total = 0
    for i in range(1,n+1):
        total += i

    return total**2

## This formula is even better than iterating through the n numbers! Derived from grouping values in the sum: n/2 groups of numbers whose sums are all n+1
def betterSquareOfSum(n):
    return ((n*(n+1))/2)**2


def difference(n):
    return squareOfSum(n)-sumOfSquares(n)

def betterDifference(n):
    return betterSquareOfSum(n)-sumOfSquares(n)

print(difference(100))
print(betterDifference(100))
