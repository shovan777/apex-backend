from functools import reduce


def lonely_integer(a):
    # Write your code here
    # #########1
    # for i, num in enumerate(a):
    #     if a.count(num)==1:
    #         return num
    # #######2
    # a.sort()
    # while a and (len(a) > 2):
    #     first, second = a.pop(), a.pop()
    #     if first + second != 2*first:
    #         return first
    # if a:
    #     return a.pop()
    # #########3
    # result = 0
    # for i in a:
    #     result = result ^ i
    #     print(result)
    # return result
    # #########4
    return reduce(lambda x, y: x ^ y, a)


a = [1, 2, 3, 4, 1, 2, 3]
print(lonely_integer(a))
