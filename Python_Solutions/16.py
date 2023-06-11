## What is the sum of the digits of the number 2**1000?

## where s is the number 2, we just have to loop through digits -- easy with a list comprehension inside of a call to the sum() function
def main(s):
    return sum([int(x) for x in str(s**1000)])

print(main(2))
