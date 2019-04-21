sum = 0
fib1 = 1
fib2 = 2
temp =1
while fib2 < 4000000:
    if fib2 %2 == 0:
        sum = sum + fib2
    temp = fib1
    fib1 = fib2
    fib2 = fib2 + temp
print sum

