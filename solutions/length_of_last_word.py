# https://leetcode.com/problems/length-of-last-word/description/


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])


from leetcode import test

test(Solution().lengthOfLastWord("Hello World"), 5)
test(Solution().lengthOfLastWord("   fly me   to   the moon  "), 4)
test(Solution().lengthOfLastWord("luffy is still joyboy"), 6)
