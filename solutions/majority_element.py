# https://leetcode.com/problems/majority-element/description/

from collections import Counter

class Solution:
    def majorityElement(self, nums) -> int:
        counter = Counter(nums)
        for n in counter:
            if counter[n] > len(nums) / 2:
                return n

from leetcode import *

test(Solution().majorityElement([3, 2, 3]), 3)
test(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)
