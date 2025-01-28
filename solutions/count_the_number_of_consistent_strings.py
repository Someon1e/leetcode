# https://leetcode.com/problems/count-the-number-of-consistent-strings/description/


class Solution:
    def countConsistentStrings(self, allowed: str, words) -> int:
        count = 0
        for word in words:
            consistent = 1
            for character in word:
                if character not in allowed:
                    consistent = 0
                    break
            count += consistent
        return count


from leetcode import test

test(Solution().countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]), 2)
test(
    Solution().countConsistentStrings("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"]),
    7,
)
test(
    Solution().countConsistentStrings(
        "cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]
    ),
    4,
)
