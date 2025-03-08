
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

    products = set()
    for a in range(1, 10000):
        for b in range(a+1, 10000):
            product = a * b
            s = str(a) + str(b) + str(product)
            if len(s) > 9:
                break
            if pandigital(s):
                products.add(product)
    print(sum(products))
