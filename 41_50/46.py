import math


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


def odd_composite_generator():

    n = 3
    while True:
        if not is_prime(n):
            yield n
        n += 2


def prime_generator():

    yield 2
    n = 3
    while True:
        if is_prime(n):
            yield n
        n += 2


def goldbach_conjecture(n, p):
    # Takes a number `n` and prime `p`, and figures out if we can write as `n = p + 2 * k**2` for some `k` to figure out

    k = math.sqrt((n-p)/2)
    return int(k) if k.is_integer() else None


if __name__ == '__main__':

    # For every odd-composite number we're considering, generate list of primes up to that number
    # Save list across numbers
    prime_gen = prime_generator()
    useful_primes = [prime_gen.__next__()]

    odd_comp_gen = odd_composite_generator()
    for n in odd_comp_gen:

        # Keep generating primes until we have all the ones in primes list that could be part of sum
        while n > useful_primes[-1]:
            useful_primes.append(prime_gen.__next__())

        if not any([goldbach_conjecture(n, p) for p in useful_primes if n > p]):
            print(n)
            break



