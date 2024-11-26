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

# TODO: tests