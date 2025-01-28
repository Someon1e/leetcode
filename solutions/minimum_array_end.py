# https://leetcode.com/problems/minimum-array-end/description/


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        mask1 = 1
        mask2 = 1
        while mask2 <= n:
            while x & mask1:
                mask1 <<= 1
            if mask2 & n:
                x |= mask1
            mask1 <<= 1
            mask2 <<= 1
        return x


from leetcode import test

test(Solution().minEnd(3, 4), 6)
test(Solution().minEnd(2, 7), 15)
