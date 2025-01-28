# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/description/


class Solution:
    def minGroups(self, intervals) -> int:
        sorted_starts = sorted(i[0] for i in intervals)
        sorted_ends = sorted(i[1] for i in intervals)

        end_index, overlaps = 0, 0

        for start in sorted_starts:
            if start > sorted_ends[end_index]:
                end_index += 1
            else:
                overlaps += 1

        return overlaps


from leetcode import test

test(Solution().minGroups([[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]), 3)
test(Solution().minGroups([[1, 3], [5, 6], [8, 10], [11, 13]]), 1)
