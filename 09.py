## A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a**2 + b**2 = c**2
## There exists exactly one Pythagorean triplet for which a + b + c = 1000.
## Find the product abc.

## Brute-force method for calculating the triplet -- very inefficient, since it does far too many calculations to be any good
def specialTriplet(valSum):
    a = 1

    ## '-2' because b and c have to be at least 1
    while a <= valSum - 2:
        b = 1

        ## '-2' for same reason as above
        while b <= valSum - 2:
            c = (a**2 + b**2)**(.5)

            if sum([a, b, c]) == valSum:
                return a*b*c

            b += 1
        a += 1


## Using Euclid's formula, we can perform fewer calculations
## By adding time checks (time.time()), this method can be shown to be 120 times faster than the above brute-force method
def specialEuclid(valSum):
    ## By Euclid's formula, m and n are arbitrary numbers -- their relationship to 'a', 'b', and 'c' can be seen below
    n = 1

    ## We know that a value will eventually satisfy this condition, so we can infinitely loop
    while True:
        m = n + 1

        ## We know that 'b' (or any of the 'a', 'b', or 'c' values) cannot be greater than the sum -- therefore, we have our upper bound for m
        while 2*m*n < valSum:

            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2

            if sum([a, b, c]) == valSum: 
                return a*b*c

            m += 1
        n += 1


## Quick function to test the running times of each method
def timeTest():
    import time
    start = time.time()
    specialTriplet(1000)
    end = time.time()
    print("Took %f seconds for method 1" %(end - start))

    start = time.time()
    specialEuclid(1000)
    end = time.time()
    print("Took %f seconds for method 2" %(end-start))


print(specialTriplet(1000))
print(specialEuclid(1000))
#timeTest()

