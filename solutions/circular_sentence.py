# https://leetcode.com/problems/circular-sentence/description/


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        last = None
        for word in sentence.split(" "):
            if last is not None and last != word[0]:
                return False
            last = word[-1]
        return sentence[0] == sentence[-1]


from leetcode import test

test(Solution().isCircularSentence("leetcode exercises sound delightful"), True)
test(Solution().isCircularSentence("eetcode"), True)
test(Solution().isCircularSentence("Leetcode is cool"), False)
