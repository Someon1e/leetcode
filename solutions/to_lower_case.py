# https://leetcode.com/problems/to-lower-case/description/

upper_to_lower = {}
for upper in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    upper_to_lower[upper] = chr(ord(upper) | 32)


class Solution:
    def toLowerCase(self, s: str) -> str:
        # return s.lower()
        return "".join(upper_to_lower.get(character, character) for character in s)


from leetcode import *

test(Solution().toLowerCase("Hello"), "hello")
test(Solution().toLowerCase("here"), "here")
test(Solution().toLowerCase("LOVELY"), "lovely")
