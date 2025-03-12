import math


def is_pentagonal(n):

    p = (1 + math.sqrt(24*n + 1)) / 6
    return p.is_integer()


def is_hexagonal(n):

    h = (1 + math.sqrt(8*n + 1)) / 4
    return h.is_integer()


if __name__ == '__main__':

    triangle = lambda n: int(n * (n+1)/2)

    n = 286
    found = False
    while not found:
        t_n = triangle(n)
        if is_pentagonal(t_n) and is_hexagonal(t_n):
            found = True
        else:
            n += 1

    print(n, triangle(n))
