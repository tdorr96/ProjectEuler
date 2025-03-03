def triangle_number():
    # Generator function for triangle numbers

    i, triangle = 1, 1
    while True:
        yield triangle
        i += 1
        triangle += i


def factors(n):

    assert n > 0

    if n == 1:
        return [1]

    k = 1
    all_factors = []
    while k * k <= n:
        if n % k == 0:
            all_factors.append(k)
            if k * k != n:
                all_factors.append(int(n/k))
        k += 1

    return all_factors


if __name__ == '__main__':

    for triangle in triangle_number():
        if len(factors(triangle)) > 500:
            print(triangle)
            break
