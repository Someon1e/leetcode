# https://leetcode.com/problems/power-of-three/description/

powers_of_three = set([3**i for i in range(32)])


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n in powers_of_three


from leetcode import test

test(Solution().isPowerOfThree(27), True)
test(Solution().isPowerOfThree(0), False)
test(Solution().isPowerOfThree(-1), False)
