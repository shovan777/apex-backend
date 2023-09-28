sum_ones = 0
max_sum = 0
bin_list = ""
n = 5
while n > 0:
    rem = n % 2
    print(f"n: {n}, rem: {rem}")

    if rem == 1:
        sum_ones += 1
        if sum_ones > max_sum:
            max_sum = sum_ones
            print(f"max_ones = {max_sum}")
    else:
        sum_ones = 0
    print(sum_ones)

    n = n // 2
