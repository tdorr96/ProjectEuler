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

    triangle = []
    with open('0067_triangle.txt', 'r') as open_f:
        for row in open_f:
            triangle.append([int(col) for col in row.strip('\n').split(' ')])

    print(maximum_path_sum(triangle))
