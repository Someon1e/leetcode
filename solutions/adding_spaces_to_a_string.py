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
