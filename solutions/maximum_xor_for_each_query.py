# https://leetcode.com/problems/maximum-xor-for-each-query/description/


class Solution:
    def getMaximumXor(self, nums, maximumBit: int):
        xor = 0
        for num in nums:
            xor ^= num

        answers = []
        bit_mask = (1 << maximumBit) - 1
        for num in reversed(nums):
            answers.append(xor ^ bit_mask)
            xor ^= num
        return answers


from leetcode import test

test(Solution().getMaximumXor([0, 1, 1, 3], 2), [0, 3, 2, 3])
test(Solution().getMaximumXor([2, 3, 4, 7], 3), [5, 2, 6, 5])
test(Solution().getMaximumXor([0, 1, 2, 2, 5, 7], 3), [4, 3, 6, 4, 6, 7])
