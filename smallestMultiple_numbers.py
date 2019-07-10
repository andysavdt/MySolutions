#!/usr/bin/env python
import math
def prime_numbers_till_n(n):
    primes=[]
    #!/usr/bin/env python
    #primes.append(1)
    if n>=2 :
        if n%2 == 0:
            primes.append(2)

        for i in range(3,n+1,2):
            i_is_prime = True
            for j in range(1,len(primes)+1):
                if i%j == 0 and j !=1:
                    i_is_prime = False
                    break
                if j >= int(math.sqrt(i)):
                    break
            if i_is_prime:
                primes.append(i)


    return primes

def smallest_multiple_numbers(n):

    #Get primes in range of 1 to n here if nth number is prime then it is inclusive
    primes = prime_numbers_till_n(n)

    #plcae holder for the smallest multiple number
    product = 1 #As anything multipled by 1 is itself

    #Loginc to get the number of multiples required of the primes:
    for i in primes:
        temp = 1
        while (i*temp)<=n and i!=1:
            temp *=i
        product *= temp
    return product


#    for i in range (1, n+1):

def main():
    print(smallest_multiple_numbers(100))
    #print(prime_numbers())

if __name__ == "__main__":
    main()
