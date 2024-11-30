# https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/description/


class Solution:
    def minChanges(self, s: str) -> int:
        changes = 0
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                changes += 1
        return changes

from leetcode import *

test(Solution().minChanges("1001"), 2)
test(Solution().minChanges("10"), 1)
test(Solution().minChanges("0000"), 0)
