# https://leetcode.com/problems/uncommon-words-from-two-sentences/description/

from collections import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str):
        return [a for a, b in Counter(s1.split(" ") + s2.split(" ")).items() if b == 1]


from leetcode import test

test(
    Solution().uncommonFromSentences("this apple is sweet", "this apple is sour"),
    ["sweet", "sour"],
)
test(
    Solution().uncommonFromSentences("apple apple", "banana"),
    ["banana"],
)
