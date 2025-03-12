import math


def is_pentagonal(n):

    p = (1 + math.sqrt(24*n + 1)) / 6
    return p.is_integer()


def pentagonal(n):

    return int(n * (3*n - 1) / 2)


if __name__ == '__main__':

    limit = 5000
    for j in range(1, limit):
        p_j = pentagonal(j)
        for k in range(j+1, limit):
            p_k = pentagonal(k)
            if is_pentagonal(p_j + p_k) and is_pentagonal(p_k - p_j):
                print(p_j, p_k, p_k - p_j)

