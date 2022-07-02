## The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
## We can see that 28 is the first triangle number to have over five divisors.
## What is the value of the first triangle number to have over five hundred divisors?

def triangular(divisors):
    i = 1
    while True:
        ## First, find the next triangular number
        #triangleNum = sum([x for x in range(1,i+1)])
        
        ## Better formula for finding a triangular number:
        triangleNum = i*(i+1)//2

        foundDivisors = []

        ## Now, find how many divisors it has -- only have to check every value up to the square root
        for n in range(1,int(triangleNum**.5)+1):
            if triangleNum%n == 0 and n not in foundDivisors:
                foundDivisors.append(n)
                
                ## This is done after the previous addition to ensure that we aren't adding duplicate divisors
                if triangleNum//n not in foundDivisors:
                    foundDivisors.append(triangleNum//n)

        if len(foundDivisors) > divisors:
            return triangleNum
        i += 1

print(triangular(500))