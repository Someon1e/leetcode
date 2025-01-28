# https://leetcode.com/problems/rotate-string/description/


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for shift in range(len(s)):
            if s[shift:] + s[:shift] == goal:
                return True
        return False


from leetcode import test

test(Solution().rotateString("abcde", "cdeab"), True)
test(Solution().rotateString("abcde", "abced"), False)
