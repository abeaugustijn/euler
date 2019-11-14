def is_prime(num):
    if num == 2:
        return (True)
    m = 2
    while (m * m <= num):
        if num % m == 0:
            return (False)
        m = m + 1
    return (True)

def next_prime(num):
    num = num + 1
    while not is_prime(num):
        num = num + 1
    return (num)

if __name__ == '__main__':
    p = 1
    for x in range (1, 10002):
        p = next_prime(p)
    print (p)
