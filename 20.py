## Find the sum of the digits in the number 100!

## functools is required to use the reduce function
import functools

def sumDig(n):
    ## First we create the factorial of 100! using lambda and reduce functions, then create a string of that number.
    ## Looping through the digits of the string is trivial, after which we just call the sum function
    return sum([int(x) for x in str(functools.reduce(lambda a, b: a*b, range(1,n+1)))])

print(sumDig(100))
