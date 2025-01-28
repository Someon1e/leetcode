# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/description/


class Solution:
    def largestCombination(self, candidates) -> int:
        counter = [0 for _ in range(24)]
        for candidate in candidates:
            for bit in range(24):
                if candidate & (1 << bit):
                    counter[bit] += 1
        return max(counter)


from leetcode import test


test(Solution().largestCombination([16, 17, 71, 62, 12, 24, 14]), 4)
test(Solution().largestCombination([8, 8]), 2)
