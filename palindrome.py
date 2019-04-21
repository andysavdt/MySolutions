#!/usr/bin/env python


def is_palindrome(number):
    temp = number
    rev = 0
    while temp>0:
        rev = rev * 10 + temp % 10
        temp = int(temp /10)
    return (rev == number)

def largest_palindrome():
    large_pal = 0
    #print multiples
    for i in range(990,99,-11):
        #print large_pal
        for j in range (999,99,-1):
            #print large_pal
            product = i*j
            if large_pal < product and is_palindrome(product):
                print ("i = %d, j = %d", i , j)
                large_pal = product
    return large_pal
def main():
    print (largest_palindrome())

if __name__ == "__main__":
    main()
