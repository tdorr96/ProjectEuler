def collatz_sequence(n, cache):
    # We use memoization to speed up computation
    # I.e. if as part of our chain we've reached an n we already calculated the sequence for,
    # just append that pre-computed chain to ours and return (and store the resulting chain too)

    k = n
    sequence = 1
    while k != 1:

        k = int(k/2) if k % 2 == 0 else 3*k + 1

        if k in cache:
            sequence += cache[k]
            break

        sequence += 1

    cache[n] = sequence
    return sequence


if __name__ == '__main__':

    assert(collatz_sequence(13, {}) == 10)

    cache = {}
    starting_number, longest_chain = None, 0
    for i in range(1, 1000000):
        chain = collatz_sequence(i, cache)
        if chain > longest_chain:
            longest_chain = chain
            starting_number = i

    print(starting_number)
