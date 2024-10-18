# https://leetcode.com/problems/palindrome-number/description/


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)


from leetcode import *

test(
    Solution().isPalindrome(121),
    True,
)
test(
    Solution().isPalindrome(-121),
    False,
)
test(
    Solution().isPalindrome(10),
    False,
)
