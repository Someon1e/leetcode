class Solution:
    def reverseBits(self, n: int) -> int:
        return int(format(n, "032b")[::-1], 2)


from leetcode import *

test(
    Solution().reverseBits(0b00000010100101000001111010011100),
    0b00111001011110000010100101000000,
)
test(
    Solution().reverseBits(0b11111111111111111111111111111101),
    0b10111111111111111111111111111111,
)
