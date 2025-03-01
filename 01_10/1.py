def natural_numbers_multiples_of(multiples, limit):
    # Returns sum of natural numbers below `limit` that are multiples of any of the numbers in `multiples
    # "If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9.
    # The sum of these multiples is 23."
    # How to use this function for that example would be `natural_numbers_multiples_of([3, 5], 10)`

    total = 0
    for i in range(1, limit):
        if any(i % x == 0 for x in multiples):
            total += i
    return total


if __name__ == '__main__':

    assert(natural_numbers_multiples_of([3, 5], 10) == 23)

    # Find the sum of all the multiples of 3 or 5 below 1000.
    print(natural_numbers_multiples_of([3, 5], 1000))
