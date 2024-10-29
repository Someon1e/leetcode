# https://leetcode.com/problems/third-maximum-number/description/


class Solution:
    def thirdMax(self, nums) -> int:
        nums_set = set(nums)
        if len(nums_set) >= 3:
            return sorted(nums_set)[-3]
        return max(nums_set)


from leetcode import *

test(Solution().thirdMax([3, 2, 1]), 1)
test(Solution().thirdMax([1, 2]), 2)
test(Solution().thirdMax([2, 2, 3, 1]), 1)
