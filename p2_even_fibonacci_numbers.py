n0 = 0
n1 = 1
tmp = 0

sum = 0

while tmp <= 4000000:
    tmp = n0
    n0 = n1
    n1 = n1 + tmp
    if tmp % 2 == 0:
        sum = sum + tmp

print (sum)
