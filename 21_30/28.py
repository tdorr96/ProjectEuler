def corners_add(n):
    # Worked out on paper, to add the corners of an nxn grid, for n odd, its the following equation

    return 4 * (n**2) - 6 * (n-1)


def sum_corners_add(n):

    assert n >= 3 and n % 2 != 0

    total = 1  # Start at 1 to include the middle number 1 as edge case
    for i in range(3, n+1, 2):
        total += corners_add(i)
    return total


if __name__ == '__main__':

    assert(corners_add(5) == 25 + 21 + 17 + 13)
    assert(corners_add(3) == 9 + 7 + 5 + 3)
    assert(sum_corners_add(5) == 101)

    print(sum_corners_add(1001))
