## The following iterative sequence is defined for the set of positive integers:
## n → n/2 (n is even)
## n → 3n + 1 (n is odd)
## Which starting number, under one million, produces the longest chain?

## Recursive solution for finding a Collatz sequence
def Collatz(n):
    if n == 1:
        return [n]
    if n%2 == 0:
        return [n] + Collatz(n//2)
    else:
        return [n] + Collatz(3*n+1)

## Straightforward -- albeit slow -- way of finding the longest sequence
def CollatzLength(n):
    return max([len(x) for x in [Collatz(y) for y in range(1,n)]])

print(CollatzLength(1000000))
