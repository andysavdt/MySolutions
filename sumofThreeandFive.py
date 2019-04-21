sum = 0
for i in range(1,1000):
    if i%3 == 0 or i%5 == 0 :
        sum = sum +i
print("Sum of numbers divisible by 3 and 5 in range of 1 to 1000 is %d",sum)
