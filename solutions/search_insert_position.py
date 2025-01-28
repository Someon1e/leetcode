# https://leetcode.com/problems/search-insert-position/description/


class Solution:
    def searchInsert(self, nums, target: int) -> int:
        upper = len(nums) - 1
        lower = 0
        while lower <= upper:
            mid = (upper + lower) // 2
            num = nums[mid]
            if num > target:
                upper = mid - 1
            elif num < target:
                lower = mid + 1
            else:
                return mid
        return lower


from leetcode import test

test(Solution().searchInsert([1, 3, 5, 6], 5), 2)
test(Solution().searchInsert([1, 3, 5, 6], 2), 1)
test(Solution().searchInsert([1, 3, 5, 6], 7), 4)
