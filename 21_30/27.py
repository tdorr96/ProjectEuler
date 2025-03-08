import time


def is_prime(n, cache):

    # Quick checks
    if n < 2:
        return False
    if n in cache:
        return cache[n]
    if n % 2 == 0:
        cache[n] = False
        return False

    # Only need to test for factors up to square root of n. This approach avoids floating-point square root
    k = 3
    while k * k <= n:
        if n % k == 0:
            cache[n] = False
            return False
        k += 2  # Increment by 2. We've already checked to see if it's divisible by even numbers

    cache[n] = True
    return True


def quadratic_formula(a, b, n):

    return n**2 + a*n + b


def consecutive_primes(a, b, primes_cache):

    n = 0
    while is_prime(quadratic_formula(a, b, n), primes_cache):
        n += 1
    return n


if __name__ == '__main__':

    assert(consecutive_primes(a=1, b=41, primes_cache={}) == 40)
    assert (consecutive_primes(a=-79, b=1601, primes_cache={}) == 80)

    start_time = time.time()
    primes_cache = {2: True}
    max_primes, max_a, max_b = 0, None, None
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            primes = consecutive_primes(a, b, primes_cache)
            if primes > max_primes:
                max_primes = primes
                max_a, max_b = a, b
    end_time = time.time()

    print(end_time - start_time)
    print(max_a, max_b, max_primes, max_a * max_b)
