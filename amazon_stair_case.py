'''
A person can climb either 1 or 2 steps, can you write the function which returns the number of the possible ways the person can reach the nth step?

eg if n is 3 he can reach in 3 ways: [0,1,2,3] ->[0,2,3] -> [0,1,3] and function should return 3

Solution

num_ways[0] = [0] --> 1
num_ways(1) = [0,1] --> [0] --> 1
num_ways(2) = [0,1,2] [0,2] --> [0,1],[0]
num_ways(3) = [0,1,2,3] [0,2,3] [0,1,3] --> [0,1,2] [0,2] [0,1]


num_ways(3) = num_ways(2)+ num_ways(1)
'''
def helper(n,memo):
    if n == 0 or n == 1:
        memo[n] = 1
        return 1
    print "something"
    if memo[n] !=0:
        return memo[n]
    memo[n] = helper(n-1,memo)+helper(n-2,memo)
    return memo[n]

def helper_bottom_up(n):
    if n == 0 or n == 1:
        return 1
    nums =[0]*(n+1)
    nums[0] = 1
    nums[1] = 1
    for i in range(2,n+1):
        nums[i] = nums[i-1]+nums[i-2]
    return nums[n]

def num_ways(n):
    #memo = [0]*(n+1)
    #return helper(n,memo)
    return helper_bottom_up(15)

print num_ways(15)
