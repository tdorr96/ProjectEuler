import time
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

    start_time = time.time()
    ns_searched = []
    for n in range(1000, 10000):
        if n in ns_searched:
            continue
        perms = [int(''.join(p)) for p in itertools.permutations(str(n))]
        ns_searched.extend(perms)
        for n1, n2, n3 in itertools.combinations(perms, 3):
            if n3 - n2 == 3330 and n2 - n1 == 3330 and is_prime(n1) and is_prime(n2) and is_prime(n3):
                print(n, str(n1) + str(n2) + str(n3))
    end_time = time.time()
    print(end_time - start_time)
