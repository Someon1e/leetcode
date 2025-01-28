# https://leetcode.com/problems/find-if-array-can-be-sorted/description/


class Solution:
    def canSortArray(self, nums) -> bool:
        minimum_maximum = [nums[0], nums[0]]
        segments = [minimum_maximum]
        tracking_bit_count = nums[0].bit_count()
        for num in nums[1:]:
            bit_count = num.bit_count()
            if bit_count == tracking_bit_count:
                if num > minimum_maximum[1]:
                    minimum_maximum[1] = num
                elif num < minimum_maximum[0]:
                    minimum_maximum[0] = num
            else:
                minimum_maximum = [num, num]
                segments.append(minimum_maximum)
                tracking_bit_count = bit_count

        for i in range(len(segments)):
            if i + 1 == len(segments):
                break
            if segments[i][1] >= segments[i + 1][0]:
                return False
        return True


from leetcode import test

test(Solution().canSortArray([8, 4, 2, 30, 15]), True)
test(Solution().canSortArray([1, 2, 3, 4, 5]), True)
test(Solution().canSortArray([3, 16, 8, 4, 2]), False)
