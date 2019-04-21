#!/usr/bin/env python

def num_ways_x(n):
    if n == 0 : return 1
    total = 0
    for i in {1,2}:
        if (n -i)>=0 :
            total += num_ways_x(n-i)
    return total

def num_ways_x_bottom_up(n):

    if n == 0 : return 1
    nums = [0]*(n+1)
    nums[0]= 1

    for i in range (1,n+1):
        total = 0
        for j in [1,2,4]:
            if i-j >=0:
                #print("i-j",i-j)
                print (nums[i-j])
                total += nums[i-j]
                print(total)
        nums[i] = total#nums[1]=1,nums[2]=1,nums[3]=
    return nums[n]


print(num_ways_x(4))

print (num_ways_x_bottom_up(4))
