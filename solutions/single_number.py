# https://leetcode.com/problems/single-number/description

class Solution:
    def singleNumber(self, nums) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

from leetcode import test


test(Solution().singleNumber([2, 2, 1]), 1)
test(Solution().singleNumber([4, 1, 2, 1, 2]), 4)
test(Solution().singleNumber([1]), 1)
