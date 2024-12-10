# https://leetcode.com/problems/ransom-note/description/


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for letter in set(ransomNote):
            if magazine.count(letter) < ransomNote.count(letter):
                return False
        return True


# TODO: tests
