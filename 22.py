## What is the total of all the name scores in the file?

names = open("p022_names.txt")

## Calculating the score of a name
def score(name):
    return sum([ord(ch)-64 for ch in name])

## Parsing each name, calculating its score and returning the sum
def parseNames(n):
    ## Converting the list of names into a usable format
    namesList = sorted(n.readline().replace('"', '').split(","))
    ## Score * index for every index in our list of names. Sum the resulting list and return it
    return sum([score(namesList[ind-1]) * ind for ind in range(1, len(namesList)+1)])

print(parseNames(names))
