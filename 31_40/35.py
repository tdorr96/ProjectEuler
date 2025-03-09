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


def is_circular_prime(n, cache):

    s = str(n)
    circular = [s[i:] + s[:i] for i in range(len(s))]
    # Python uses eager evaluation, so as soon as one is False, it won't evaluate the rest in the list
    return all(is_prime(int(c), cache) for c in circular)


if __name__ == '__main__':

    primes_cache = {2: True}

    primes = []
    for n in range(2, 1000000):
        if is_circular_prime(n, primes_cache):
            primes.append(n)
    print(len(primes))
