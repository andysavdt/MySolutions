'''
Write a function which provides the number of ways the sring of integers can be decoded to alphabets

eg : 127 can be decoded to 1->a, 2->b, 7->g in one way and 12-> l, 7-> g. Which are possible 2 ways to decode 127, so function should return 2

no_ways(12345) -> a + no_ways(2345) or ab+ no_ways(345)

Lets consider edge case:
no_ways(12345) -> a + no_ways(2345) but considering first 2 numbers 12 points to l so l + no_ways(345)
Recursion fits here!

no_ways("12345") = no_ways("2345")+no_ways("345")

creating multiple strings in Recursion is not good!

Lets get the pointer passed instead?

no_of_ways("12345") = no_of_ways("12345",n-1) + no_of_ways("12345",n-2)

base cases

empty string? return 1

starts with 0 return 0

'''

def mediator(string,k,memo):
    if k == 0:
        return 1

    s = len(string) - k

    if string[s] == '0':
        return 0

    if memo[k]!= 0:
        return memo[k]
    result = mediator(string, k-1,memo)
    if 10<= int(string[s:s+2]) <=26 :
        result += mediator(string, k-2,memo)
    memo.insert(k,result)
    return memo[k]

def no_of_ways(string):
    memo = [0]*(len(string)+1)
    return mediator(string,len(string),memo)

print no_of_ways("1111234")
