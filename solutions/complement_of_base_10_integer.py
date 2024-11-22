# https://leetcode.com/problems/complement-of-base-10-integer/description/


class Solution:
    def bitwiseComplement(self, num: int) -> int:
        if num == 0:
            return 1
        mask = (1 << num.bit_length()) - 1
        return ~num & mask


from leetcode import *

test(Solution().bitwiseComplement(5), 2)
test(Solution().bitwiseComplement(7), 0)
test(Solution().bitwiseComplement(10), 5)
