## A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
## Find the largest palindrome made from the product of two 3-digit numbers.

## Finding if a number is a palindrome by iterating through its values
def isPal(n):
    string = str(n)
    for i in range(len(string)):
        if string[i] != string[-i-1]:
            return False
    return True

## Checking every possible palindrome that could be formed by multiplication of two three-digit numbers
def largePal(n):
    num1 = 10**n - 1
    num2 = 10**n - 1
    maxPal = 0

    while num1 > 0:
        num2 = 10**n - 1
        
        while num2 > 0:
            ## Checking if the multiplication is greater than maxPal first to avoid calculating unnecessary palindromes
            if num1*num2 > maxPal and isPal(num1*num2):
                maxPal = num1*num2

            num2 -= 1
        num1 -= 1

    return maxPal

print(largePal(3))
