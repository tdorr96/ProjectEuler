import time
import functools


def factorial(n):

    return functools.reduce(lambda x, y: x * y, range(1, n+1), 1)


def sum_factorial_of_digits(n, cache):

    return sum(cache[int(digit)] for digit in str(n))


if __name__ == '__main__':

    assert(factorial(0) == 1)
    assert(factorial(1) == 1)
    assert(factorial(4) == 24)
    assert(factorial(5) == 120)

    # We only need to know the factorials of integers from 0 through 9
    factorial_cache = {i: factorial(i) for i in range(10)}

    assert(sum_factorial_of_digits(145, factorial_cache) == 145)

    # To figure out upper limit of numbers to check for, consider that for a given number of digits n in a number
    # The largest the sum of the factorial of the digits can be is n * 9!
    # Once the number of digits exceeds 7, the largest number of any number with that amount of digits, 999..99,
    # the sum of the factorial of the digits will never be large enough to equal the original number

    start_time = time.time()
    ns = []
    for n in range(10, 10000000):
        if sum_factorial_of_digits(n, factorial_cache) == n:
            ns.append(n)
    end_time = time.time()
    print(end_time - start_time)
    print(ns, sum(ns))
