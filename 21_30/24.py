def permutations(l):
    # Use recursion

    # Base case
    if len(l) == 1:
        return [l]

    # Normal case, for each element in list, work out the permutations of the list with that one removed, and then
    # stick the element we removed on front of all the lists returned.
    perms = []
    for idx, i in enumerate(l):
        sub_perms = permutations(l[:idx] + l[idx+1:])
        perms.extend(map(lambda sub_l: [i] + sub_l, sub_perms))
    return perms


if __name__ == '__main__':

    perms = permutations(list(range(10)))
    print(''.join(str(char) for char in perms[1000000-1]))

