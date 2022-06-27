## 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
## What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

## Brute-force solution
def smallestDivisible(n):
    addition = n
    while True:
        if n%2 == 0 and n%3 == 0 and n%4 == 0 and n%5 == 0 and n%6 == 0 and n%7 == 0 and n%8 == 0 and n%9 == 0 and n%10 == 0 and n%11 == 0 and n%12 == 0 and n%13 == 0 and n%14 == 0 and n%15 == 0 and n%16 == 0 and n%17 == 0 and n%18 == 0 and n%19 == 0 and n%20 == 0:
            return n
        n += addition

## Using some ideas from the Internet, a much faster solution:
def fasterDivisible(n):
    ## You can iterate by the same number you start at, as long as it's a multiple of the final value (which 2520 and 20 are)
    addition = n
    ## You only need to check these numbers, all other cases are covered by these
    check = [11, 13, 14, 16, 17, 18, 19, 20]
    while True:
        if len([n for val in check if n%val != 0]) == 0:
            return n
        n += addition
    return None


#print(fasterDivisible(20))

## You can start at 2520 and step by 2520, since the number must be a multiple of the least common multiple of 2-10: 2520 (Credit: David Z on Stack Overflow)
print(fasterDivisible(2520))
