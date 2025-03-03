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


def factors(n):

    assert n > 0

    if n == 1:
        return [1]

    # Only need to test for factors up to square root of n
    limit = int(n ** 0.5) + 1

    factors = []
    for i in range(1, limit):
        if n % i == 0:
            factors.append(i)
            if int(n/i) != i:
                factors.append(int(n/i))

    return factors


if __name__ == '__main__':

    assert([i for i in range(100) if is_prime(i)] == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

    n = 600851475143
    prime_factors = filter(lambda f: is_prime(f), factors(n))
    largest_prime_factor = sorted(prime_factors, reverse=True)[0]
    print(largest_prime_factor)

