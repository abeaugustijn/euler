import math

def is_palindrome(num):
    num = str(num)
    num_len = len(num)
    for x in range (0, math.ceil(num_len // 2)):
        if num[x] != num[num_len - x - 1]:
            return (False)
    return (True)

def largest_palindrome():
    largest = 0
    for i in range(0, 1000):
        for j in range (0, 1000):
            sum = i * j
            if is_palindrome(sum):
                if (sum > largest):
                    largest = sum
    return (largest)

if __name__ == '__main__':
    print(largest_palindrome())
