# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/


class Solution:
    def findDisappearedNumbers(self, nums):
        result = []
        nums_set = set(nums)
        for n in range(1, len(nums) + 1):
            if n not in nums_set:
                result.append(n)
        return result
