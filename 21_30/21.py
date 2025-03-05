def sum_of_proper_divisors(n):
    # Numbers less than `n` which divide evenly into `n`

    if n == 1:
        return 0

    # Only need to test for divisors up to square root of n
    limit = int(n ** 0.5) + 1

    divisors = []
    for i in range(1, limit):
        if n % i == 0:
            divisors.append(i)
            if i != 1 and int(n/i) != i:
                divisors.append(int(n/i))

    return sum(divisors)


if __name__ == '__main__':

    amiable_numbers = set()

    for a in range(2, 10000):
        b = sum_of_proper_divisors(a)
        if a != b and sum_of_proper_divisors(b) == a:
            amiable_numbers.add(a)
            amiable_numbers.add(b)

    print(sum(amiable_numbers))
