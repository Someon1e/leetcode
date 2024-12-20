# https://leetcode.com/problems/contains-duplicate-ii/description/


class Solution(object):
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        seen = {}
        for i, num in enumerate(nums):
            if num in seen and abs(i - seen[num]) <= k:
                return True
            seen[num] = i
        return False


from leetcode import *

test(Solution().containsNearbyDuplicate([1, 2, 3, 1], 3), True)
test(Solution().containsNearbyDuplicate([1, 0, 1, 1], 1), True)
test(Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2), False)
