triangle1 = [
    [3],
    [7, 4],
    [2, 4, 6],
    [8, 5, 9, 3]
]


s2 = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

triangle2 = []
for row in s2.split('\n'):
    triangle2.append([int(col) for col in row.split(' ')])


def maximum_path_sum(triangle):
    # "By starting at the top of the `triangle` and moving to adjacent numbers on the row below,
    # find the maximum total from top to bottom"
    # Brute force is too inefficient, use a smarter approach
    # Starting at bottom, work up row by row, assigning each node the maximum value of all paths from it to the bottom
    # This can be worked out just from the two nodes below it, picking the maximum at each step, as we work from bottom
    # to top, so we don't have to consider all the paths and pick the maximum at the end in a brute force way

    # Set up another triangle data structure, with the same shape as the triangle argument
    # with 0s in all nodes, except the bottom row
    maximum_paths = [
        [col if row_idx == len(triangle) - 1 else 0 for col in row]
        for row_idx, row in enumerate(triangle)
    ]

    # Working from bottom to top, assign each node in new triangle data structure the maximum value of any
    # paths from it to the bottom row, worked out by just looking at the maximum of two below it by nature of working
    # from bottom to top
    for row_idx in reversed(range(len(triangle)-1)):
        for col_idx in range(len(maximum_paths[row_idx])):
            maximum_paths[row_idx][col_idx] = triangle[row_idx][col_idx] + max(
                maximum_paths[row_idx+1][col_idx], maximum_paths[row_idx+1][col_idx+1]
            )

    return maximum_paths[0][0]


if __name__ == '__main__':

    assert(maximum_path_sum(triangle1) == 23)

    print(maximum_path_sum(triangle2))


