def sum_of_power_of_digits(n, power):

    return n == sum(int(digit) ** power for digit in str(n))


if __name__ == '__main__':

    assert(sum_of_power_of_digits(1634, 4))
    assert(sum_of_power_of_digits(8208, 4))
    assert(sum_of_power_of_digits(9474, 4))

    # For powers of 5, only need to consider 6 digit numbers because
    # Consider a 7 digit number, the maximum it can be is 9,999,999. The sum of it's digits to the power of 5 is
    # 7(9 ** 5) = 413343, which is only 6 digits long, so it could never reach a total of 7 digits.
    total = 0
    for i in range(10, 1000000):
        if sum_of_power_of_digits(i, 5):
            total += i
    print(total)
