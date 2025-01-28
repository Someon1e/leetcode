# https://leetcode.com/problems/maximum-width-ramp/description/


class Solution:
    def maxWidthRamp(self, nums) -> int:
        indices = []
        smallest = None
        for index, num in enumerate(nums):
            if smallest is None or smallest > num:
                indices.append(index)
                smallest = num

        max_width = 0
        index2 = len(nums)
        for num in reversed(nums):
            index2 -= 1
            while indices and nums[indices[-1]] <= nums[index2]:
                index = indices.pop()

                max_width = max(max_width, index2 - index)
        return max_width


from leetcode import test

test(Solution().maxWidthRamp([6, 0, 8, 2, 1, 5]), 4)
test(Solution().maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]), 7)
