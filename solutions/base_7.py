# https://leetcode.com/problems/base-7/description/

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        result = []
        negative = False
        if num < 0:
            negative = True
            num = -num
        while num != 0:
            result.append(str(num % 7))
            num //= 7
        if negative:
            result.append("-")
        return "".join(result[::-1])

from leetcode import test

test(Solution().convertToBase7(100), "202")
test(Solution().convertToBase7(-7), "-10")
