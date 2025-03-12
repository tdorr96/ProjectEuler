import time


if __name__ == '__main__':

    start_time = time.time()
    # Use a dictionary as has O(1) lookup, much faster than storing in a list
    pentagonal_numbers = {int(n * (3*n -1) / 2): True for n in range(1, 10000)}

    for p_j in pentagonal_numbers:
        for p_k in pentagonal_numbers:
            if (p_j + p_k) in pentagonal_numbers and (p_j - p_k) in pentagonal_numbers:
                print(p_j, p_k, p_j - p_k)
    end_time = time.time()

    print(end_time-start_time)
