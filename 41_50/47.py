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


def prime_factors(n, cache):

    # Only need to test for factors up to square root of n. Add 1 for range() being exclusive of end limit
    limit = int(n ** 0.5) + 1

    all_factors = []
    for i in range(1, limit):
        if n % i == 0:
            if is_prime(i, cache):
                all_factors.append(i)
            if int(n/i) != i:
                if is_prime(int(n/i), cache):
                    all_factors.append(int(n/i))

    return all_factors


if __name__ == '__main__':

    primes_cache = {2: True}

    # Looking for the first `n` consecutive integers to have `m` distinct prime factors
    consecutive = 4
    distinct_primes = 4

    n = 1
    while True:
        ns = [n+i for i in range(consecutive)]
        ps = [prime_factors(k, primes_cache) for k in ns]
        if all(len(factors) == distinct_primes for factors in ps):
            print(ns, ps)
            break
        n += 1
