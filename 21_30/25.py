def fibonacci_generator():
    # Returns Fibonacci numbers, starting at 1 and 2, in a generator function, as well as the index of fibonacci term

    index = 1
    a, b = 1, 1
    while True:
        yield a, index
        a, b = b, a + b
        index += 1


if __name__ == '__main__':

    for (fib, index) in fibonacci_generator():
        if len(str(fib)) == 1000:
            print(index)
            break
