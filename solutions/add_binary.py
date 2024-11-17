class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = False
        result = []
        if len(a) < len(b):
            b, a = a, b
        b = b.rjust(len(a), "0")

        for v1, v2 in zip(reversed(a), reversed(b)):
            if v1 == "1" and v2 == "1":
                if carry:
                    result.append("1")
                else:
                    carry = True
                    result.append("0")
            elif v1 == "0" and v2 == "0":
                if carry:
                    result.append("1")
                    carry = False
                else:
                    result.append("0")
            else:
                if carry:
                    result.append("0")
                    carry = True
                else:
                    result.append("1")
        if carry:
            result.append("1")
        return "".join(reversed(result))


from leetcode import *

test(Solution().addBinary("11", "1"), "100")
test(Solution().addBinary("1010", "1011"), "10101")
