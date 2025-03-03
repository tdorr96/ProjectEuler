def difference(i):
    # Returns "difference between the sum of the squares of the first `i`` natural numbers and the square of the sum"

    square_of_sum = sum(range(1, i+1)) ** 2
    sum_of_squares = sum(x ** 2 for x in range(1, i+1))
    return square_of_sum - sum_of_squares


if __name__ == '__main__':

    assert(difference(10) == 2640)

    print(difference(100))
