import heapq
from typing import List

import numpy as np


def kWeakestRows_old(mat: List[List[int]], k: int) -> List[int]:
    max_sum_ind = 0
    max_sum = 0
    mat_sum = []
    # def sum_max(row, i, max_sum, max_sum_ind):
    #     sum_val = sum(row)
    #     if sum_val > max_sum:
    #         max_sum = sum_val
    #         max_sum_ind = i
    #         print(max_sum, max_sum_ind)
    #     return sum_val
    # sum_row = map(sum_max, mat)
    # sum_row = [sum_max(row, i, max_sum, max_sum_ind) for i, row in enumerate(mat)]
    for i, row in enumerate(mat):
        sum_val = sum(row)
        mat_sum.append(sum_val)
        if sum_val > max_sum:
            max_sum = sum_val
            max_sum_ind = i
            print(max_sum, max_sum_ind)
    found_k = 1
    result_set = set([max_sum_ind])
    mat_sum.pop(max_sum_ind)
    for i, val in enumerate(mat_sum):
        if found_k >= k:
            break
        if val == max_sum:
            result_set.add(val)
    return list(result_set)


def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
    mat_sum = {i: sum(row) for i, row in enumerate(mat)}
    sorted_mat_dict = dict(sorted(mat_sum.items(), key=lambda item: item[1]))

    return list(sorted_mat_dict.keys())[:k]


def kWeakestRows2(mat: List[List[int]], k: int) -> List[int]:
    k_weakest = dict(heapq.nsmallest(2, enumerate(mat), key=lambda item: sum(item[1])))
    return list(k_weakest.keys())


matrix_list = np.identity(5, dtype=int).tolist()
matrix_list[1][0] = 1

print(kWeakestRows2(matrix_list, 2))
