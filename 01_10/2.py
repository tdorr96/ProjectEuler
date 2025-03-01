def fibonacci_generator(limiter):
    # Returns Fibonacci numbers, starting at 1 and 2, in a generator function, up to a max value
    # E.g. `list(fibonacci_generator(100))` will return [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    a, b = 1, 2
    while a < limiter:
        yield a
        a, b = b, a + b


if __name__ == '__main__':

    total = 0
    for i in fibonacci_generator(4000000):
        # Go through terms in the Fibonacci sequence whose values do not exceed 4 million
        if i % 2 == 0:
            total += i
    print(total)
