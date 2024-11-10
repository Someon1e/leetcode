# https://leetcode.com/problems/contains-duplicate/description/


class Solution:
    def containsDuplicate(self, nums) -> bool:
        return len(nums) != len(set(nums))


from leetcode import *

test(Solution().containsDuplicate([1, 2, 3, 1]), True)
test(Solution().containsDuplicate([1, 2, 3, 4]), False)
test(Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)
