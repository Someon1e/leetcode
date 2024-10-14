# https://leetcode.com/problems/maximal-score-after-applying-k-operations/description/

from math import ceil
from heapq import heappush, heappop, heapify


class Solution:
    def maxKelements(self, nums, k: int) -> int:
        total = 0

        # why is there no max heap
        for i in range(len(nums)):
            nums[i] *= -1
        heapify(nums)

        for _ in range(k):
            num = -heappop(nums)
            total += num
            heappush(nums, -ceil(num / 3))
        return total


from leetcode import *


test(Solution().maxKelements([10, 10, 10, 10, 10], 5), 50)
test(Solution().maxKelements([1, 10, 3, 3, 3], k=3), 17)
