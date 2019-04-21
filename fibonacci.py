def fib(n,memo):
    if memo[n] !=0:
        return memo[n]
    if n == 1 or n ==2:
        result = 1
        memo[n] = 1
    else:
        result = fib(n-1,memo) + fib(n-2,memo)
    memo[n] = result
    return result

def fibboci(n):
    memo = [0]*(n+1)
    return fib(n,memo)
def main():
    print ("6th fibonacci element is ", fibboci(30))

if __name__ == "__main__":
    main()
