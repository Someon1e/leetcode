# https://leetcode.com/problems/valid-anagram/


class Solution:
    def isAnagram(self, s: str, t: str):
        # return Counter(s) == Counter(t)
        # but that defeats the purpose

        if len(s) != len(t):
            return False
        for character in set(s):
            if t.count(character) != s.count(character):
                return False
        return True


from leetcode import test

test(Solution().isAnagram("anagram", "nagaram"), True)
test(Solution().isAnagram("rat", "car"), False)
