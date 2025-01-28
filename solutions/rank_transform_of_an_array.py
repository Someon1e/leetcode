# https://leetcode.com/problems/rank-transform-of-an-array/description/


class Solution:
    def arrayRankTransform(self, arr):
        ranks = list(set(arr))
        ranks.sort()
        lookup = {value: rank + 1 for rank, value in enumerate(ranks)}
        return [lookup[value] for value in arr]


from leetcode import test

test(Solution().arrayRankTransform([40, 10, 20, 30]), [4, 1, 2, 3])
test(Solution().arrayRankTransform([100, 100, 100]), [1, 1, 1])
test(
    Solution().arrayRankTransform([37, 12, 28, 9, 100, 56, 80, 5, 12]),
    [5, 3, 4, 2, 8, 6, 7, 1, 3],
)
