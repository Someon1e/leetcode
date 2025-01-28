# https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/


class Solution:
    def makeFancyString(self, s: str) -> str:
        last = None
        count = 0
        output = []
        for character in s:
            if character == last:
                if count == 2:
                    continue
                count += 1
                output.append(character)
            else:
                last = character
                count = 1
                output.append(character)
        return "".join(output)


from leetcode import test

test(Solution().makeFancyString("leeetcode"), "leetcode")
test(Solution().makeFancyString("aaabaaaa"), "aabaa")
test(Solution().makeFancyString("aab"), "aab")
