# https://leetcode.com/problems/find-the-difference/description/


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0

        for character in t:
            result ^= ord(character)
        for character in s:
            result ^= ord(character)

        return chr(result)


from leetcode import test

test(Solution().findTheDifference("abcd", "abcde"), "e")
test(Solution().findTheDifference("", "y"), "y")
