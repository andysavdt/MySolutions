def multiply(a,b):
    #Base
    if a == 0 or b ==0 :
        return 0

    #Base 2
    if a == 1:
        return b

    #Reccursive activity
    return multiply(a-1, b) + b

def main():
    print("Multiplication of 3 and 4 is ", multiply(3,4))

if __name__ == "__main__":
    main()
