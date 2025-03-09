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


def truncate(n, direction):

    s = str(n)

    if direction == 'left':
        return [int(s[i:]) for i in range(len(s))]

    elif direction == 'right':
        return [int(s if i == 0 else s[:-i]) for i in range(len(s))]


if __name__ == '__main__':

    primes_cache = {2: True}

    n = 11
    primes = []
    while len(primes) != 11:
        if (all(is_prime(i, primes_cache) for i in truncate(n, 'left')) and
                all(is_prime(i, primes_cache) for i in truncate(n, 'right'))):
            primes.append(n)
        n += 2
    print(primes)
    print(sum(primes))
