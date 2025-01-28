# https://leetcode.com/problems/missing-number/description/


class Solution:
    def missingNumber(self, nums) -> int:
        result = 0
        for x in range(len(nums)):
            result ^= x + 1
            result ^= nums[x]
        return result


from leetcode import test

test(Solution().missingNumber([3, 0, 1]), 2)
test(Solution().missingNumber([0, 1]), 2)
test(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)
