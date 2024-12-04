# https://leetcode.com/problems/adding-spaces-to-a-string/description/


class Solution:
    def addSpaces(self, s: str, spaces) -> str:
        output = []
        space_index = 0
        for index, character in enumerate(s):
            if len(spaces) != space_index and index == spaces[space_index]:
                output.append(" ")
                space_index += 1
            output.append(character)
        return "".join(output)


from leetcode import *

test(
    Solution().addSpaces("LeetcodeHelpsMeLearn", [8, 13, 15]), "Leetcode Helps Me Learn"
)
test(Solution().addSpaces("icodeinpython", [1, 5, 7, 9]), "i code in py thon")
test(Solution().addSpaces("spacing", [0, 1, 2, 3, 4, 5, 6]), " s p a c i n g")
