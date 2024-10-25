# https://leetcode.com/problems/plus-one/description/


class Solution:
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        digits.insert(0, 1)
        return digits


from leetcode import *

test(Solution().plusOne([1, 2, 3]), [1, 2, 4])
test(Solution().plusOne([4, 3, 2, 1]), [4, 3, 2, 2])
test(Solution().plusOne([9]), [1, 0])
