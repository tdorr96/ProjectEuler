is_prime = __import__('3').is_prime


def prime_generator(limit):
    # Generator function to return the prime numbers up to `limit`

    assert limit > 2

    # We know prime numbers have to be odd, except the first prime number (2)
    # So yield 2 as the first, then start at 3 and increment in values of 2 to keep it odd
    yield 2

    i = 3
    while True:
        if i >= limit:
            break
        if is_prime(i):
            yield i
        i += 2


if __name__ == '__main__':

    assert(sum(prime_generator(10)) == 17)

    print(sum(prime_generator(2000000)))
