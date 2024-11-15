# https://leetcode.com/problems/happy-number/description/


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set([n])
        while True:
            sum_of_squares = 0
            for x in str(n):
                sum_of_squares += int(x) ** 2
            n = sum_of_squares
            if n == 1:
                return True
            elif n in seen:
                return False
            seen.add(n)


# TODO: tests
