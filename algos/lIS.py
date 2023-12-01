def find_longest_sub(c):
    c_len = len(c)
    sub_lengths = [1] * c_len
    for i in range(1, c_len):
        can_lens = [sub_lengths[k] for k in range(i) if c[k] < c[i]]
        sub_lengths[i] = 1 + max(can_lens, default=0)
    return max(sub_lengths, default=0)


first_arr = [3, 1, 8, 2, 5]
second_arr = [5, 2, 8, 6, 3, 6, 9, 5]

print(find_longest_sub(second_arr))
