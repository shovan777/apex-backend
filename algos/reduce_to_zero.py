# best soln
from math import floor


class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0

        while num != 0:
            steps += 1
            # if rightmost bit is 1, then odd
            if num & 1:
                num -= 1
            else:
                # apparently this is div by 2
                num >>= 1

        return steps


# my soln


def numberOfSteps(num: int) -> int:
    count = 0
    while num != 0:
        div = num / 2
    if div - floor(div) == 0:
        num = div
    else:
        num = num - 1
    count += 1
    return count
