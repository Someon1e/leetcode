# https://leetcode.com/problems/take-gifts-from-the-richest-pile/description/


from math import sqrt, floor


class Solution:
    def pickGifts(self, gifts, k: int) -> int:
        for _ in range(k):
            most = max(gifts)
            index = gifts.index(most)
            gifts[index] = floor(sqrt(most))
        return sum(gifts)


from leetcode import test

test(Solution().pickGifts([25, 64, 9, 4, 100], 4), 29)
test(Solution().pickGifts([1, 1, 1, 1], 4), 4)
