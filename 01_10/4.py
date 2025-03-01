def is_palindrome(n):
    # Find the middle point, and check if the two halves either side of it are the same, with right side being reversed
    # Works for both even & odd length strings. In odd case the middle number is essentially discarded

    s = str(n)
    middle_split = int(len(s)/2)
    left, right = s[:middle_split], s[-middle_split:]
    return left == right[::-1]


if __name__ == '__main__':

    # "Find the largest palindrome made from product of two 3-digit numbers"
    largest_palindrome = 0
    for x in range(100, 1000):
        for y in range(100, 1000):
            n = x * y
            if is_palindrome(n):
                largest_palindrome = largest_palindrome if n < largest_palindrome else n
    print(largest_palindrome)
