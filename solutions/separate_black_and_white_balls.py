# https://leetcode.com/problems/separate-black-and-white-balls/description/


class Solution:
    def minimumSteps(self, s: str) -> int:
        steps = 0
        counter = 0
        for character in s:
            if character == "1":
                counter += 1
            elif character == "0":
                steps += counter
        return steps


from leetcode import test

test(Solution().minimumSteps("101"), 1)
test(Solution().minimumSteps("100"), 2)
test(Solution().minimumSteps("0111"), 0)
