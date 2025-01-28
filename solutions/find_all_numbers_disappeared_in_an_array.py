# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/


class Solution:
    def findDisappearedNumbers(self, nums):
        result = []
        nums_set = set(nums)
        for n in range(1, len(nums) + 1):
            if n not in nums_set:
                result.append(n)
        return result


from leetcode import test


test(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]), [5, 6])

test(Solution().findDisappearedNumbers([1, 1]), [2])
