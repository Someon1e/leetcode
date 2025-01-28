# https://leetcode.com/problems/longest-common-prefix/description/


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        index = 0
        while True:
            if len(strs[0]) <= index:
                return strs[0][:index]
            first = strs[0][index]
            for string in strs[1:]:
                if len(string) <= index or string[index] != first:
                    return string[:index]
            index += 1


from leetcode import test

test(Solution().longestCommonPrefix(["flower", "flow", "flight"]), "fl")
test(Solution().longestCommonPrefix(["dog", "racecar", "car"]), "")
