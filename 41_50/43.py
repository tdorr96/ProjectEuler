import itertools

if __name__ == '__main__':

    # To get all the 0-to-9 pandigital numbers, use permutations
    perms = itertools.permutations(range(10))

    # (index range, divisible by). Indexes are off by 1 compared to example for Python
    sub_string_divisibility = [
        ((1, 3), 2), ((2, 4), 3), ((3, 5), 5), ((4, 6), 7), ((5, 7), 11), ((6, 8), 13), ((7, 9), 17)
    ]

    total = 0
    for pandigital in perms:
        s = ''.join(str(digit) for digit in pandigital)
        if all(int(s[indices[0]:indices[1]+1]) % divisble_by == 0
               for (indices, divisble_by) in sub_string_divisibility):
            total += int(s)

    print(total)