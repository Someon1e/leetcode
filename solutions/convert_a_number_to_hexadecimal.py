character_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

class Solution:
    def toHex(self, num: int) -> str:
        if num < 0:
            num += 4294967296
        elif num == 0:
            return "0"

        result = []
        while num >= 16:
            result.append(character_list[num % 16])
            num //= 16
        if num != 0:
            result.append(character_list[num])
        return "".join(reversed(result))


from leetcode import *

test(Solution().toHex(26), "1a")
test(Solution().toHex(-1), "ffffffff")
