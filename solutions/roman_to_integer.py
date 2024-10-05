# https://leetcode.com/problems/roman-to-integer/description/

SYMBOL_MAP = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        counting = 0
        typeof = 0
        for character in s:
            value = SYMBOL_MAP[character]
            if value > typeof:
                # Found a character that is more valuable
                typeof = value
                # Subtract characters before
                total -= counting
                counting = 0
            elif value < typeof:
                # Found a character that is less valuable
                typeof = value
                # Add characters before
                total += counting
                counting = 0
            counting += value
        return total + counting


from leetcode import *

test(Solution().romanToInt("III"), 3)
test(Solution().romanToInt("LVIII"), 58)
test(Solution().romanToInt("MCMXCIV"), 1994)
