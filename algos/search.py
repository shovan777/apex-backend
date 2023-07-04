def binary_search(arr, low, high, to_find):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == to_find:
        return mid
    if arr[mid] > to_find:
        return binary_search(arr, low, mid - 1, to_find)
    return binary_search(arr, mid + 1, high, to_find)


if __name__ == "__main__":
    # arr = [1, 2, 3, 4, 5]
    # generate a difficult array for search
    arr = [i for i in range(1000)]
    to_find = 234
    index_pos = binary_search(arr, 0, len(arr) - 1, to_find)
    print(f"Element {arr[index_pos]} == {to_find} is at index {index_pos}")
