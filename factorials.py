def factorial(a):
    #reccursion
    if a >= 1 :
        return factorial(a-1)*a

    return 1

def main():
    print ("factorial of 4 is ",factorial(4))

if __name__ == "__main__":
    main()
