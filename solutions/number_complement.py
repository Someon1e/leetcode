# https://leetcode.com/problems/number-complement/description/


class Solution:
    def findComplement(self, num: int) -> int:
        mask = (1 << num.bit_length()) - 1
        return ~num & mask


from leetcode import test

test(Solution().findComplement(5), 2)
test(Solution().findComplement(1), 0)
