# https://leetcode.com/problems/score-of-a-string/description/


class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) - 1))


from leetcode import *

test(Solution().scoreOfString("hello"), 13)
test(Solution().scoreOfString("zaz"), 50)
