# https://leetcode.com/problems/keyboard-row/description/

qwertyuiop = set(character for character in "qwertyuiop")
asdfghjkl = set(character for character in "asdfghjkl")
zxcvbnm = set(character for character in "zxcvbnm")

class Solution:
    def findWords(self, words):
        filtered = []
        for word in words:
            characters = set(character for character in word.lower())

            count = 0
            count += characters.issubset(qwertyuiop) and 1 or 0
            count += characters.issubset(asdfghjkl) and 1 or 0
            count += characters.issubset(zxcvbnm) and 1 or 0
            if count == 1:
                filtered.append(word)

        return filtered

# TODO: tests
