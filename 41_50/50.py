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


def prime_generator(limit):

    yield 2
    n = 3
    while n < limit:
        if is_prime(n):
            yield n
        n += 2


if __name__ == '__main__':

    limit = 1000000

    # Use a dict for O(1) lookup
    primes_lookup = {p: True for p in prime_generator(limit=limit)}
    primes = list(primes_lookup.keys())

    max_p, max_chain = None, -1
    for i in range(len(primes)):
        current_sum = 0
        for j in range(i, len(primes)):
            current_sum += primes[j]
            if current_sum >= limit:
                break
            if current_sum in primes_lookup and j+1-i > max_chain:
                max_chain = j+1 - i
                max_p = current_sum

    print(max_p, max_chain)
