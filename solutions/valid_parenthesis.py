# https://leetcode.com/problems/valid-parentheses/description/

ending_to_opening = {")": "(", "}": "{", "]": "["}
opening = set(["(", "[", "{"])


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for character in s:
            if character in opening:
                stack.append(character)
            elif (stack and stack.pop()) != ending_to_opening[character]:
                return False
        return not stack


from leetcode import *


test(Solution().isValid("()"), True)
test(Solution().isValid("()[]{}"), True)
test(Solution().isValid("(]"), False)
test(Solution().isValid("([])"), True)
