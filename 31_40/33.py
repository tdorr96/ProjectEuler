if __name__ == '__main__':

    fractions = []
    for numerator in range(10, 100):
        if numerator % 10 == 0:
            continue
        for denominator in range(numerator+1, 100):
            if denominator % 10 == 0:
                continue
            frac = numerator/denominator
            for digit in range(1, 10):
                if str(numerator).count(str(digit)) == 1 and str(denominator).count(str(digit)) == 1:
                    reduced_numerator = int(str(numerator).replace(str(digit), ''))
                    reduced_denominator = int(str(denominator).replace(str(digit), ''))
                    reduced_frac = reduced_numerator/reduced_denominator
                    if frac == reduced_frac:
                        fractions.append(frac)

    assert(len(fractions) == 4)
    print(fractions)