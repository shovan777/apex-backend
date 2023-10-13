def sumXor(n):
    # Write your code here
    # count = 0
    # for num in range(n+1):
    #     if n + num == n ^ num:
    #         count += 1
    return pow(2, bin(n).count("0") - 1) if n else 1
