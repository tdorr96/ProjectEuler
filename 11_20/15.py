import math

def lattice_paths(grid, cache):
    # Even though we worked out a single equation for answer, let's say we want to define it programatically
    # We use recursion, by defining the paths as made up of paths from smaller rects
    # Need to use memoization though

    # 1. Memoization
    if grid in cache:
        return cache[grid]

    # 2. If not memoized so far, recursively work it out
    if grid[0] == 1:
        # column
        paths = 1 + lattice_paths((1, grid[1]-1), cache)
    elif grid[1] == 1:
        # row
        paths = 1 + lattice_paths((grid[0]-1, 1), cache)
    else:
        # rect
        paths = lattice_paths((grid[0]-1, grid[1]), cache) + lattice_paths((grid[0], grid[1]-1), cache)

    # 3. Store worked out path in cache and return
    cache[grid] = paths
    return paths


if __name__ == '__main__':
    # Was easiest to work out on paper first by defining number of paths in terms of number of paths of smaller rects

    # Can actually be defined by a single equation, without the programmatic approach above using binomial coefficient
    # n!/(k!(n-k)!). N is total number of moves, K is number of moves in one direction
    # So would be 40!/(20!20!)

    cache = {(1, 1): 2}  # base case
    assert(lattice_paths((2, 2), cache) == 6)

    cache = {(1, 1): 2}  # base case
    paths = lattice_paths((20, 20), cache)
    print(paths)

    binomial = (math.factorial(40))/(math.factorial(20) * math.factorial(20))
    assert(paths == binomial)
