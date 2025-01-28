# https://leetcode.com/problems/two-sum/description/


class Solution:
    def twoSum(self, nums, target):
        for first_index, num in enumerate(nums):
            try:
                return [first_index, nums.index(target - num, first_index + 1)]
            except ValueError:
                pass


from leetcode import test

test(Solution().twoSum([2, 7, 11, 15], 9), [0, 1])
test(Solution().twoSum([3, 2, 4], 6), [1, 2])
test(Solution().twoSum([3, 3], 6), [0, 1])
