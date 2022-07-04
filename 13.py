numberFile = open("13.txt")
## Formatting the string input from the text file that contains the number
numbers = [int(x.replace('\n','')) for x in numberFile]

## A one-liner is able to find the sum of the numbers and return the first 10 digits by converting it back to a string
def firstTen(nums):
    return str(sum(nums))[0:11]

print(firstTen(numbers))
