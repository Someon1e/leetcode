# https://leetcode.com/problems/string-compression-iii/description/


class Solution:
    def compressedString(self, word: str) -> str:
        comp = []
        count = 0
        previous = None
        for character in word:
            if character == previous:
                count += 1
                if count == 9:
                    comp.append("9")
                    comp.append(previous)
                    count = 0
            else:
                if previous is not None:
                    if count != 0:
                        comp.append(str(count))
                        comp.append(previous)
                previous = character
                count = 1
        if previous is not None:
            if count != 0:
                comp.append(str(count))
                comp.append(previous)
        return "".join(comp)


from leetcode import *

test(Solution().compressedString("abcde"), "1a1b1c1d1e")
test(Solution().compressedString("aaaaaaaaaaaaaabb"), "9a5a2b")
