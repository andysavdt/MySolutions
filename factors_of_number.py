#!/usr/bin/env python

import math

def prime_factors(n):
    #Define the list
    factors = []
    two_count = 0
    while n % 2 == 0:
        if two_count == 0:
            factors.append(2)
        else:
            two_count += 1

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n)+1),2) :
        # while i divides n , print i and divide n
        while n % i== 0:
            factors.append(i)
            n = n / i
        if n <=i:
            break
    if n >2 :
        factors.append(n)
    return factors
def main() :
    print (prime_factors(6008514751432))
    print (max (prime_factors(600851475143)))

if __name__ == "__main__":
    main()
