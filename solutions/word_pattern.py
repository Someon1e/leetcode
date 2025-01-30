# https://leetcode.com/problems/word-pattern/description/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False

        character_map = {}
        for character, word in zip(pattern, words):
            if character in character_map:
                if word != character_map[character]:
                    return False
            else:
                if word in character_map.values():
                    return False
                character_map[character] = word
        return True

from leetcode import test
test(Solution().wordPattern("abba", "dog cat cat dog"), True)
test(Solution().wordPattern("abba","dog cat cat fish"), False)
test(Solution().wordPattern("aaaa", s = "dog cat cat dog"), False)
