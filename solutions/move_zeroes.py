# https://leetcode.com/problems/move-zeroes/description/


class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        index = 0
        for num in nums:
            if num != 0:
                nums[index] = num
                index += 1
        for zero in range(index, len(nums)):
            nums[zero] = 0


from leetcode import test, in_place

test(*in_place(Solution().moveZeroes, ([0, 1, 0, 3, 12])), [1, 3, 12, 0, 0])
test(*in_place(Solution().moveZeroes, ([0])), [0])
