def evenly_divisible_by_all(factors):
    # Returns the smallest number that is evenly divisible by all the numbers in `factors`
    # "2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder."
    # Example given in problem, would be returned with `evenly_divisible_by_all(range(1, 11))`

    i = 0
    while True:
        # If we assume the list `factors` is sorted, we can increment by the largest number in it
        i += factors[-1]
        if all(i % x == 0 for x in factors):
            return i


if __name__ == '__main__':

    assert(evenly_divisible_by_all(range(1, 11)) == 2520)

    print(evenly_divisible_by_all(range(1, 21)))
