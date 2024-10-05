# https://leetcode.com/problems/power-of-two/description/

powers_of_two = set([2**i for i in range(32)])


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n in powers_of_two


from leetcode import *

test(Solution().isPowerOfTwo(1), True)
test(Solution().isPowerOfTwo(16), True)
test(Solution().isPowerOfTwo(3), False)
