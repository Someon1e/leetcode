# https://leetcode.com/problems/valid-perfect-square/description/

lookup = set(n * n for n in range(46341))


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return num in lookup


from leetcode import test

test(Solution().isPerfectSquare(16), True)
test(Solution().isPerfectSquare(14), False)
