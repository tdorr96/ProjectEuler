def distinct_terms(limit):

    terms = set()
    for a in range(2, limit+1):
        for b in range(2, limit+1):
            terms.add(a ** b)
    return len(terms)


if __name__ == '__main__':

    assert(distinct_terms(5) == 15)
    print(distinct_terms(100))
