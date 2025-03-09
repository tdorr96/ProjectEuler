def pandigital(s):
    # `s` is the concatenation of multiplicand, multiplier, and product,
    # and we're seeing if it's 1 through 9 pandigital

    if '0' in s or len(s) != 9:
        return False

    counts = {i: 0 for i in range(1, 10)}
    for digit in s:
        counts[int(digit)] += 1
    return all(value == 1 for value in counts.values())


if __name__ == '__main__':

    largest_pandigital = 0
    # Only need to go up to 10,000, as the smallest list of ints to multiply with is (1, 2)
    # So the largest number we can have is 9999, which is 4 digits, and * 2 = 19998, which is 5 digits, for a total of 9
    for n in range(1, 10000):
        for i in range(2, 10):
            concat = ''.join([str(n * j) for j in range(1, i + 1)])
            if pandigital(concat):
                if int(concat) > largest_pandigital:
                    largest_pandigital = int(concat)
    print(largest_pandigital)
