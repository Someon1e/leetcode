# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/


class Solution:
    def minLength(self, s: str) -> int:
        while True:
            old = s
            s = s.replace("AB", "")
            s = s.replace("CD", "")
            if old == s:
                return len(s)


from leetcode import test

test(Solution().minLength("ABFCACDB"), 2)
test(Solution().minLength("ACBBD"), 5)
