#!/usr/bin/env python
import math
def is_prime(n):
    primes=[]
    #!/usr/bin/env python
    #primes.append(1)
    is_prime = True
    if n == 2:
        return is_prime
    if n>2 :
        if n%2 == 0:
            is_prime = False
        else:
            for i in range(3, n+1 , 2):
                if i > int(math.sqrt(n)):
                    break
                if n%i == 0:
                    is_prime = False
                    break
                    #print is_prime
                    #print primes
    return is_prime

def nth_prime_number(n):

    #Get place holder for the counter
    if n==1:
        return 2
    counter =1
    check_prime = 3
    while counter < n:
        #print "number"
        #print counter
        if is_prime(check_prime):
            #print "prime %d",check_prime
            counter += 1
            #print counter
        check_prime += 1
    else:
        return check_prime-1




#    for i in range (1, n+1):

def main():
    print(nth_prime_number(10001))
    #print(prime_numbers())

if __name__ == "__main__":
    main()
