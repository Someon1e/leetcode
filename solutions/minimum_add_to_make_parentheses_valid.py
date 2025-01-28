# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        needed = 0
        for character in s:
            match character:
                case "(":
                    stack.append(character)
                case ")":
                    if stack:
                        assert stack.pop() == "("
                    else:
                        needed += 1
                case _:
                    raise Exception()
        return len(stack) + needed


from leetcode import test

test(Solution().minAddToMakeValid("())"), 1)
test(Solution().minAddToMakeValid("((("), 3)
