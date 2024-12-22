# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/


class Solution:
    def removeDuplicates(self, nums) -> int:
        index = 0
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
                nums[index] = num
                index += 1
        return index


# TODO: tests
