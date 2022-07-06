## If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

## First, create some dictionaries with lengths that we'll need later
letters = {1: len('one'), 2: len('two'), 3: len('three'), 4: len('four'), 5: len('five'), 6: len('six'), 7: len('seven'), 8: len('eight'), 9: len('nine')}

## Lengths of "teen", "twenty", "thirty", etc.
prefixes = {0: 0, 1: 4, 2: 6, 3: 6, 4: 5, 5: 5, 6: 5, 7: 7, 8: 6, 9: 6}

irregular = {10: len('ten'), 11: len('eleven'), 12: len('twelve'), 13: len('thirteen'), 14: len('fourteen'), 15: len('fifteen'), 18: len('eighteen')}


## Length of the ones place (and hundreds, for applicable numbers)
def findOne(n):
    if n == 0:
        return n
    return letters[n]

def findTen(n):
    ## There are a few numbers in the teens that are irregular
    if n in irregular:
        return irregular[n]
    
    ## ex: "Twenty" + "six"
    return prefixes[n//10] + findOne(n%10)

def findHundred(n):
    additional = 0

    ## Only adding 'and' if the ones and tens place are no '00'
    if n%100 != 0:
        additional += len("and")

    ## ex: "one" + "hundred" + "and" + "twenty" + "six"
    return letters[n//100]+ len("hundred") + additional + findTen(n%100)

def findLetters(n):
    ## The program is only designed to decompose numbers below 1000, so this one is hard-coded
    if n == 1000:
        return len("onethousand")

    ## Redirecting numbers so we don't have to add 'len('hundred')' to the 'additional' variable in findHundred
    if n < 100:
        return findTen(n)

    return findHundred(n)

## Finding the length of every number between 1 and 1000 -- the general flow breaks down the largest digit (ex: hundreds place), then sends the remainder to other functions to find the tens, then the ones place
def main():
    return sum([findLetters(x) for x in range(1,1001)])

print("The number of letters to write out 1 to 1000 (inclusive) is " + str(main()))
