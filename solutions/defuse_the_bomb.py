# https://leetcode.com/problems/defuse-the-bomb/description/


class Solution:
    def decrypt(self, code, k: int):
        if k > 0:
            repeated = code * 2
            for i in range(len(code)):
                code[i] = sum(repeated[i + 1 : i + 1 + k])
        elif k < 0:
            repeated = code * 2
            for i in range(len(code)):
                code[i] = sum(repeated[i + len(code) + k : i + len(code)])
        else:
            return [0] * len(code)
        return code


from leetcode import test

test(Solution().decrypt([5, 7, 1, 4], 3), [12, 10, 16, 13])
test(Solution().decrypt([1, 2, 3, 4], 0), [0, 0, 0, 0])
test(Solution().decrypt([2, 4, 9, 3], -2), [12, 5, 6, 13])
