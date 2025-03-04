import time


def collatz_sequence(n, cache):
    # We use memoization to speed up computation
    # I.e. if as part of our chain we've reached an n we already calculated the sequence for,
    # just append that pre-computed chain to ours and return (and store the resulting chain too)
    # The cache just stores the length of the chains, not the actual chain, as much faster

    if n in cache:
        return cache[n]

    # Keep track of the k's along chain we have not found in the cache yet
    # These intermediate k's need to be added to cache for maximum memoization benefit
    # We assert that if we reach a number whose callatz length is cached, the rest of the numbers in that chain will
    # also be cached
    k = n
    ks = [k]
    sequence = 1
    while k != 1:

        k = int(k/2) if k % 2 == 0 else 3*k + 1

        if k in cache:
            sequence += cache[k]
            break

        sequence += 1
        ks.append(k)

    for idx, k in enumerate(ks):
        # We cache sub-chains we found as part of this chain we have not yet cached
        cache[k] = sequence - idx

    return sequence


if __name__ == '__main__':

    assert(collatz_sequence(13, {}) == 10)

    start_time = time.time()
    cache = {}
    starting_number, longest_chain = None, 0
    for i in range(1, 1000000):
        chain = collatz_sequence(i, cache)
        if chain > longest_chain:
            longest_chain = chain
            starting_number = i

    end_time = time.time()

    print(starting_number)
    print(end_time-start_time)
