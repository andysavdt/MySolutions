#!/usr/bin/env python
# a -> 1 b-2 and so on to z -26
# write a function to find the number of possibility of decodes can happen for a given number
# Example 111 gives possible decodes as 'aaa', 'ka', 'ak' then number of possibilies are 3

# reccursion
def helper(data, k):
    if k == 0:#false
        return 1

    s = len(data) - k
    if data[s] == '0':#false
        return 0


    result = helper(data , k-1)#Called Helper again
    if k>=2 and int(data[s:s+2]) <=26 :#
        print("value of k is", k)
        result += helper(data , k-2)
    return result

def num_ways(data):
    #memo = [None]*(len(data)+1)
    return helper(data, len(data))

def main():
    print ("Possibilities of getting the decoded vaues are: ",num_ways("123123123"))
    #aaa or ka or ak
if __name__ == "__main__":
    main()
