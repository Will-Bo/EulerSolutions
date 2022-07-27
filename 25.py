## What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

## Returns the index of the first Fibonacci number that has "n" digits
def fibToDigits(n):
    first = 1
    second = 1

    ## Index of the current Fibonacci number
    ind = 1

    ## Generating the Fibonacci sequence
    while len(str(first)) < n:
        tmp = first
        first = second
        second += tmp
        ind += 1

    return ind

## Running the initial 3-digit test
print(fibToDigits(3))

## Finding the real 1000-digit answer
print("The index of the first term in the Fibonacci sequence to contain 1000 digits is",end=' ')
print(fibToDigits(1000))
