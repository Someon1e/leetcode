# https://leetcode.com/problems/integer-to-roman/description/

number_conversion = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"),
    (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
]

class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        for sub, character in number_conversion:
            while num >= sub:
                num -= sub
                result += character
        return result

from leetcode import test

test(Solution().intToRoman(3749), "MMMDCCXLIX")
test(Solution().intToRoman(58), "LVIII")
test(Solution().intToRoman(1994), "MCMXCIV")
