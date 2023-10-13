def maxMin(k, arr):
    # Write your code here
    arr.sort()
    print(arr)
    while k < len(arr):
        left_diff = arr[1] - arr[0]
        right_diff = arr[-1] - arr[-2]
        if left_diff <= right_diff:
            arr.pop()
        else:
            arr.pop(0)
        print(arr)
    return arr[-1] - arr[0]
    # max_min_arr = []
    # # print(len(arr) - k)
    # for i in range(len(arr) - k + 1):
    #     # print(f'i:{i}')
    #     sub_arr = arr[i:i + k]
    #     print(sub_arr)
    #     # diff = max(sub_arr) - min(sub_arr)
    #     diff = sub_arr[-1] - sub_arr[0]
    #     max_min_arr.append(diff)
    # return min(max_min_arr)


arr = [1, 5, 50, 51, 53]
arr2 = [
    4504,
    1520,
    5857,
    4094,
    4157,
    3902,
    822,
    6643,
    2422,
    7288,
    8245,
    9948,
    2822,
    1784,
    7802,
    3142,
    9739,
    5629,
    5413,
    7232,
]
# print(maxMin(3, arr))
print(maxMin(5, arr2))
