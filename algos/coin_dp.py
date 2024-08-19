def getWays(n: int, c: list[int]) -> int:
    # record = {}
    i = 0
    c = [i for i in c if i <= n]
    # for num in c:

    return i


getWays(3, [8, 3, 1, 2])
# for [5,1,2] sum to 11
# first sort the array to [5,2,1]
# get abs(11/5)=2=q  and 11%5=1 then, if we have 1 it is solved
# if we didn't have 1 then, we would decrease q-1=1
# if 11 - 5q then, that becomes the sum to solve
