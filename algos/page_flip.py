# def pageCount(n, p):
#     # Write your code here
#     mid_page = n/2
#     if p%2 != 0:
#         p = p -1
#     if p > mid_page:
#         return n - p -1
#     return p -1


def pageCount(n, p):
    # Write your code here
    mid_page = n // 2
    if p % 2 != 0:
        p = p - 1
    if n % 2 != 0:
        n = n - 1
    if p > mid_page:
        return (n - p - 1) if (n - p - 1) > 0 else 0
    return (p - 1) if (p - 1) > 0 else 0


print(pageCount(6, 6))
