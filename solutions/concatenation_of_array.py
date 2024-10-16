# https://leetcode.com/problems/concatenation-of-array/description/


class Solution:
    def getConcatenation(self, nums):
        return nums + nums


from leetcode import *


test(Solution().getConcatenation([1, 2, 1]), [1, 2, 1, 1, 2, 1])
test(Solution().getConcatenation([1, 3, 2, 1]), [1, 3, 2, 1, 1, 3, 2, 1])
