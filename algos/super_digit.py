# def superDigit(n, k):
#     def find_super(n):
#         # print(n)
#         if len(n) == 1:
#             return int(n)
#         # Write your code here
#         return find_super(str(sum(map(lambda x: int(x), n))))
#     return find_super(n * k)
def superDigit(n, k):
    def find_super(n):
        # print(n)
        if len(n) == 1:
            return int(n)
        # Write your code here
        return find_super(str(sum(map(lambda x: int(x), n))))

    super_n = str(find_super(n) * k)
    if len(super_n) == 1:
        return int(super_n)
    return find_super(super_n)


print(superDigit("148", 3))
