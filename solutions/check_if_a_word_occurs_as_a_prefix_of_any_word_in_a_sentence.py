# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/description/


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for index, word in enumerate(sentence.split(" ")):
            if word.startswith(searchWord):
                return index + 1
        return -1


from leetcode import test

test(Solution().isPrefixOfWord("i love eating burger", "burg"), 4)
test(Solution().isPrefixOfWord("this problem is an easy problem", "pro"), 2)
test(Solution().isPrefixOfWord("i am tired", "you"), -1)
