def is_prime(n):

    # Quick checks
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Only need to test for factors up to square root of n
    limit = int(n ** 0.5) + 1

    for i in range(2, limit):
        if n % i == 0:
            return False

    return True


def prime_generator(n):
    # Generator function to return the first `n` prime numbers

    assert n > 0

    # We know prime numbers have to be odd, except the first prime number (2)
    # So yield 2 as the first, then start at 3 and increment in values of 2 to keep it odd
    yield 2

    i = 3
    primes_found = 1
    while True:
        if primes_found == n:
            break
        if is_prime(i):
            yield i
            primes_found += 1
        i += 2


if __name__ == '__main__':

    assert(list(prime_generator(6)) == [2, 3, 5, 7, 11, 13])

    *_, last = prime_generator(6)  # Get the last value of an iterator
    assert(last == 13)

    *_, last = prime_generator(10001)
    print(last)
