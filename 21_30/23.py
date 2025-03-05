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


def is_perfect_number(n):

    return n == sum_of_proper_divisors(n)


def is_deficient_number(n):

    return sum_of_proper_divisors(n) < n


def is_abundant_number(n):

    return sum_of_proper_divisors(n) > n


if __name__ == '__main__':

    assert(is_perfect_number(28))
    assert(is_abundant_number(12))

    # Faster to find all the numbers which can be written as sum of two abundant numbers
    # and then flip set to find those that cannot, in the given range of 1-28123

    abundant_numbers = [n for n in range(12, 28124-12) if is_abundant_number(n)]

    # Find all positive integers up to 28123 which can be written as sum of two abundant numbers
    limit = 28123
    sum_abundant_numbers = set()
    for a in range(len(abundant_numbers)):
        for b in range(a, len(abundant_numbers)):
            abundant_sum = abundant_numbers[a]+abundant_numbers[b]
            if abundant_sum <= limit:
                sum_abundant_numbers.add(abundant_sum)
            else:
                # For given a, if a+b is > 28123, as list is sorted all following b will still result in a+b > 28123
                break

    # Now find all the numbers not in this set (i.e. cannot be written as the sum of two abundant numbers)
    total = sum(i for i in range(1, 28124) if i not in sum_abundant_numbers)
    print(total)