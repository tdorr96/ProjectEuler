import math


def to_binary(n):

    if n == 0:
        return '0'

    bits = [0 for i in range(int(math.log2(n)) + 1)]
    for exponent in range(len(bits)-1, -1, -1):
        power = 2 ** exponent
        if power <= n:
            n -= power
            bits[exponent] = 1
    return ''.join(str(b) for b in reversed(bits))


def is_palindrome(s):
    # Find the middle point, and check if the two halves either side of it are the same, with right side being reversed
    # Works for both even & odd length strings. In odd case the middle number is essentially discarded

    if len(s) == 1:
        return True

    middle_split = int(len(s)/2)
    left, right = s[:middle_split], s[-middle_split:]
    return left == right[::-1]


if __name__ == '__main__':

    total = 0
    for n in range(1, 1000000):
        if is_palindrome(str(n)) and is_palindrome(to_binary(n)):
            print(n, to_binary(n))
            total += n
    print(total)
