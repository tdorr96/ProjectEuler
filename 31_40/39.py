from collections import defaultdict


def factors(n):

    assert n > 0

    if n == 1:
        return [1]

    # Only need to test for factors up to square root of n
    limit = int(n ** 0.5) + 1

    all_factors = []
    for i in range(1, limit):
        if n % i == 0:
            all_factors.append(i)
            if int(n/i) != i:
                all_factors.append(int(n/i))

    return all_factors


def coprime(n, m):

    factors_n = factors(n)
    factors_m = factors(m)
    intersection = list(set(factors_n) & set(factors_m))
    return intersection == [1]


def odd(n):

    return n % 2 != 0


if __name__ == '__main__':

    # Use Euclid's formula for generating pythagorean triples, then work out p from the triple,
    # rather than the other way around
    # We populate a mapping from values of perimeter p to all the solutions (a, b, c)
    # Need to look for values m,n up to 21. m & n generate the primitive primes, the k only increases the magnitudes
    # So for the smallest n of 1, the largest m can be without exceeding 1000 is 21
    ps = defaultdict(list)
    for n in range(1, 22):
        for m in range(n+1, 22):
            if coprime(n, m) and not(odd(n) and odd(m)):
                # To be unique, m and n have to be coprime, and not both odd
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                if a+b+c > 1000:
                    # For a given n, if m is increasing, p will only keep increasing, so can move on to next n from here
                    break
                # By this point we have the unique primitive triples, with a perimeter <= 1000,
                # but we need to introduce another parameter k to generate all the non-primitive ones
                k = 1
                while k * (a+b+c) <= 1000:
                    p = k * (a+b+c)
                    ps[p].append((a*k, b*k, c*k))
                    k += 1

    print(max(ps, key=lambda k: len(ps[k])))
