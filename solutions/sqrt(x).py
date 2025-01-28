# https://leetcode.com/problems/sqrtx/description/


class Solution:
    def mySqrt(self, x: int) -> int:
        lower = 1
        upper = x
        while lower <= upper:
            middle = (lower + upper) // 2
            squared = middle * middle
            if squared == x:
                return middle
            elif squared > x:
                # decrease upperbound
                upper = middle - 1
            else:
                # increase lowerbound
                lower = middle + 1
        return upper


from leetcode import test

test(Solution().mySqrt(4), 2)
test(Solution().mySqrt(8), 2)
