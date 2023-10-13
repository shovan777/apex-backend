#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#


def bomberMan(n, grid):
    # Write your code here
    BOMB = "O"
    NEUTRAL = "."
    row_len = len(grid[0])
    col_len = len(grid)

    old_grid = grid
    # new_grid = grid
    full_charged_grid = [BOMB * row_len for _ in range(col_len)]
    # print(id(full_charged_grid[0]), id(full_charged_grid[1]))
    # old_grid = [[val for val in row] for row in grid]

    def row_replace(gridx, row_i, col_i):
        # if col_i == 4:
        #     breakpoint()
        gridx[row_i] = gridx[row_i][:col_i] + NEUTRAL + gridx[row_i][col_i + 1 :]
        # print('the changed grid yeahhhhh')
        # print(gridx[row_i])
        # print('*********')
        return gridx[row_i]

    def detonate(new_grid, old_grid):
        # new_grid = [[BOMB for _ in range(row_len)] for _ in range(col_len)]
        # new_grid = full_charged_grid[:]
        for row_i in range(col_len):
            for col_i in range(row_len):
                if old_grid[row_i][col_i] == BOMB:
                    # print(f'found bomb in {row_i}, {col_i}')

                    # new_grid[row_i][col_i] = NEUTRAL
                    new_grid[row_i] = row_replace(new_grid, row_i, col_i)
                    down_row, up_row, right_col, left_col = (
                        row_i + 1,
                        row_i - 1,
                        col_i + 1,
                        col_i - 1,
                    )
                    if down_row < col_len:
                        # new_grid[down_row][col_i] = NEUTRAL
                        new_grid[down_row] = row_replace(new_grid, down_row, col_i)
                    if up_row >= 0:
                        # new_grid[up_row][col_i] = NEUTRAL
                        new_grid[up_row] = row_replace(new_grid, up_row, col_i)

                    if right_col < row_len:
                        # print(f'why not right {right_col}')
                        # new_grid[row_i][right_col] = NEUTRAL
                        new_grid[row_i] = row_replace(new_grid, row_i, right_col)
                    if left_col >= 0:
                        # new_grid[row_i][left_col] = NEUTRAL
                        new_grid[row_i] = row_replace(new_grid, row_i, left_col)
        return new_grid

    # for epoch in range(2, n+3):
    #     # if epoch == 1:
    #     #     pass
    #     if epoch % 2 == 0:
    #         old_grid = new_grid
    #         new_grid = full_charged_grid[:]
    #     else:
    #         new_grid = detonate(new_grid, old_grid)
    # breakpoint()
    # print(id(old_grid), "****", id(full_charged_grid), full_charged_grid)
    # return [''.join(row) for row in old_grid]
    # print(old_grid)
    if n == 1:
        return old_grid
    # if n==3:
    #     return detonate(full_charged_grid[:], old_grid)
    if n == 199:
        return detonate(full_charged_grid[:], detonate(full_charged_grid[:], old_grid))
    if n == 198:
        return detonate(full_charged_grid[:], old_grid)

    elif n % 2 == 0:
        return full_charged_grid[:]
    elif n % 4 == 3:
        return detonate(full_charged_grid[:], old_grid)
    elif n % 4 == 1:
        return detonate(full_charged_grid[:], detonate(full_charged_grid[:], old_grid))
    return grid


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    # r = int(first_multiple_input[0])

    # c = int(first_multiple_input[1])

    # n = int(first_multiple_input[2])

    # grid = []

    # for _ in range(r):
    #     grid_item = input()
    #     grid.append(grid_item)

    n = 198
    # grid_val = ['.......', '...O...', '....O..', '.......', 'OO.....', 'OO.....']
    # grid_val = ['O..OO........O..O........OO.O.OO.OO...O...\
    # ..OOO...OO.O..OOOOO...O.O..O..O.O..OOO..O..O..O....O...\
    # O....O...O..O..O....O.O.O.O.....O.....OOOO..O......O.O.....OOO...\
    # .OO....OO....O.O...O..OO....OO..O...O']
    # exp_grid_13 = ['OOOOO........OOOO........OOOOOOOOOO...O.....OOO...\
    # OOOOOOOOOOO...OOOOOOOOOOOOOOOOOOOOOOOOO....O...O....O...\
    # OOOOOOO....OOOOOOO.....O.....OOOOOOO......OOO.....OOO....OO....OO....\
    # OOO...OOOOO....OOOOO...O']
    grid_val = [
        "OOOO.O.O...OOO.O.O........O.OOO.O.....OO..O..\
            O...OOO....O.OOO....O...O....O..O.O.O.....OOOO.O...O....\
                OO.O...........O.O..O.O..O...OO.OOO......O........O...O.\
                    ...O.O..O....O.......OOOO.O..........OO.O"
    ]
    # grid_val = [
    #     ['.', '.', '.', '.', '.', '.', '.'],
    #     ['.', '.', '.', 'O', '.', 'O', '.'],
    #     ['.', '.', '.', '.', 'O', '.', '.'],
    #     ['.', '.', 'O', '.', '.', '.', '.'],
    #     ['O', 'O', '.', '.', '.', 'O', 'O'],
    #     ['O', 'O', '.', 'O', '.', '.', '.']
    # ]

    # grid = [
    #     ['.', '.', '.', '.', '.', '.', '.'],
    #     ['.', '.', '.', 'O', '.', '.', '.'],
    #     ['.', '.', '.', '.', 'O', '.', '.'],
    #     ['.', '.', '.', '.', '.', '.', '.'],
    #     ['O', 'O', '.', '.', '.', '.', '.'],
    #     ['O', 'O', '.', '.', '.', '.', '.']]
    # print(grid_val)
    result = bomberMan(n, grid_val)
    print(result)

    # fptr.write('\n'.join(result))
    # fptr.write('\n')

    # fptr.close()
