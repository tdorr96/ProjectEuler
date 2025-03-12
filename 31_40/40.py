import functools

if __name__ == '__main__':

    d_powers = [10**power for power in range(0, 7)]
    d_ns = []

    # Work out a mapping from integer number to it's corresponding indices in champernowe's constant
    start = 1
    for power in range(0, 6):
        for i in range(10**power, 10**(power+1)):
            index = start + (i-10**power) * (power+1)
            for digit in range(0, power+1):
                idx = index+digit
                if idx in d_powers:
                    d_ns.append(int(str(i)[digit]))
        start = index + (power+1)

    print(functools.reduce(lambda x, y: x * y, d_ns, 1))
