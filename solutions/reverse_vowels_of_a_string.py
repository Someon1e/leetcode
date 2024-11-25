# https://leetcode.com/problems/reverse-vowels-of-a-string/description/


class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = []
        for character in s:
            if character in "aeiouAEIOU":
                stack.append(character)

        result = []
        for character in s:
            if character in "aeiouAEIOU":
                result.append(stack.pop())
            else:
                result.append(character)
        return "".join(result)


# TODO: tests
