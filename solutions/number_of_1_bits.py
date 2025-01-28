# https://leetcode.com/problems/number-of-1-bits/description/


class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()


from leetcode import test

test(Solution().hammingWeight(11), 3)
test(Solution().hammingWeight(128), 1)
test(Solution().hammingWeight(2147483645), 30)
