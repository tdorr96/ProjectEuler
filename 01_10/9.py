if __name__ == '__main__':

    # Use Euclid's formula for generating Pythagorean triples.
    # m > n > 0
    # Did not need to multiply through a, b, and c with a k positive integer as triple was primitive
    for n in range(1, 50):
        for m in range(n + 1, 50):
            a = m ** 2 - n ** 2
            b = 2 * m * n
            c = m ** 2 + n ** 2
            if a + b + c == 1000:
                print(a * b * c)
