def flip_matrix(mat):
    two_n = len(mat)
    n = two_n // 2
    max_sum = 0
    # go over the left topmost quadrant sub matrix
    for row in range(n):
        for col in range(n):
            cur = mat[row][col]
            # find alternatives to elements
            coupled_row = two_n - 1 - row
            coupled_col = two_n - 1 - col
            right = mat[row][coupled_col]
            left = mat[coupled_row][col]
            diag = mat[coupled_row][coupled_col]
            max_sum += max([right, left, diag, cur])

    print(max_sum)


to_filp = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 49], [62, 98, 114, 108]]

flip_matrix(to_filp)
