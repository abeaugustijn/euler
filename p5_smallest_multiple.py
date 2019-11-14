def is_divisible(num):
    for x in range (2, 21):
        if (num % x != 0):
            return (False)
    return (True)

def smallest_multiple():
    n = 1
    while (True):
        if is_divisible(n):
            return (n)
        if n % 1000000 == 0:
            print (n / 1000000)
        n = n + 1

if __name__ == '__main__':
    print (smallest_multiple())
