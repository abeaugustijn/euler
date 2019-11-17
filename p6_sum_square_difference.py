n1 = 0
for x in range (0, 101):
    n1 += x

n1 = n1 * n1

n2 = 0
for x in range (0, 101):
    print (x)
    n2 = n2 + x * x

print (n1 - n2)
