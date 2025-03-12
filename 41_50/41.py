import itertools


def is_prime(n):

    # Quick checks
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Only need to test for factors up to square root of n. This approach avoids floating-point square root
    k = 3
    while k * k <= n:
        if n % k == 0:
            return False
        k += 2  # Increment by 2. We've already checked to see if it's divisible by even numbers
    return True


if __name__ == '__main__':

    # All n-pandigital numbers can be worked out using permutations
    # Much more efficient to get all the n-pandigital numbers, varying n, and test if they're prime
    # Rather than generating all primes and seeing if they're pandigital
    max_pandigital = 0
    for pandigital in range(1, 10):
        perms = itertools.permutations(range(1, pandigital+1))
        for p in perms:
            n = int(''.join(str(digit) for digit in p))
            if is_prime(n):
                max_pandigital = max_pandigital if n <= max_pandigital else n

    print(max_pandigital)

