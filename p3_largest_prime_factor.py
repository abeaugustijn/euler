def is_prime(num):
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

def prime_factors(num):
    res = []
    d = 3
    while num > 1:
        if num % d == 0:
            res.append(d)
            num = num / d
            d = 3
        d = next_prime(d)
    return (res)

if __name__ == '__main__':
    for res in prime_factors(600851475143):
        print(res)

