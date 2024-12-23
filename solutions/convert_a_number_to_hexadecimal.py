class Solution:
    def toHex(self, num: int) -> str:
        if num < 0:
            num += 4294967296
        elif num == 0:
            return "0"

        def character(hex):
            match hex:
                case 10:
                    return "a"
                case 11:
                    return "b"
                case 12:
                    return "c"
                case 13:
                    return "d"
                case 14:
                    return "e"
                case 15:
                    return "f"
                case _:
                    return str(hex)

        result = []
        while num >= 16:
            result.append(character(num % 16))
            num //= 16
        if num != 0:
            result.append(character(num))
        return "".join(reversed(result))


from leetcode import *

test(Solution().toHex(26), "1a")
test(Solution().toHex(-1), "ffffffff")
