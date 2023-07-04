# implementing merge sort algorithm using recursion

# merge two sorted lists into one sorted list
import timeit


def merge(arr: list, p: int, q: int, r: int) -> list:
    # create two temporary lists
    left = arr[p : q + 1]
    right = arr[q + 1 : r + 1]

    len_left = q + 1 - p  # len(left)
    len_right = r - q  # len(right)

    # maintain current index of temp lists and main list
    i = 0  # index of left sub-list
    j = 0  # index of right sub-list
    k = p  # index of merged list

    # Until we reach either end of either left or right, pick larger among
    # elements left and right and place them in the correct position at A[p..r]
    while i < len_left and j < len_right:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1  # move to next element in left
        else:
            arr[k] = right[j]
            j += 1  # move to next element in right
        k += 1  # move to next position in merged list

    # When we run out of elements in either left or right,
    # pick up the remaining elements and put in A[p..r]
    if i < len_left:
        arr[k : r + 1] = left[i:len_left]
    elif j < len_right:
        arr[k : r + 1] = right[j:len_right]

    # no need to return anything since we are modifying the array in-place


# recursive function to sort an array of integers


def merge_sort(arr: list, p: int, r: int) -> list:
    # base case
    if p >= r:
        return

    # find the middle index
    q = (p + r) // 2

    # recursively sort the first and the second halves
    merge_sort(arr, p, q)
    merge_sort(arr, q + 1, r)

    # merge the sorted halves
    merge(arr, p, q, r)


def merge_timer():
    SETUP_CODE = """
from __main__ import merge_sort
from random import randint"""

    TEST_CODE = """
# arr = [randint(0, 100) for i in range(100)]
arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1] # worst case
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] # best case
# print("Original array:", arr)
merge_sort(arr, 0, len(arr) - 1)
# print("Sorted array:", arr)"""

    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=1, number=10000)
    print("Average time: {}".format(sum(times) / len(times)))


# main with timeit
if __name__ == "__main__":
    merge_timer()

# main
# if __name__ == "__main__":
#     n_times = 100
#     # orig_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#     orig_arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#     print("Original array:", orig_arr)
#     total_time = 0
#     for i in range(n_times):
#         arr = orig_arr.copy()
#         start = timeit.timeit()
#         merge_sort(arr, 0, len(arr) - 1)
#         total_time += timeit.timeit() - start

#     print("Sorted array:", arr, "for", n_times, "times")
#     print("Total time:", total_time, "seconds")
