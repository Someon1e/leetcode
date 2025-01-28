# https://leetcode.com/problems/check-if-n-and-its-double-exist/description/


class Solution:
    def checkIfExist(self, arr) -> bool:
        if arr.count(0) > 1:
            return True
        for x in arr:
            if x != 0 and x * 2 in arr:
                return True
        return False


from leetcode import test

test(Solution().checkIfExist([10, 2, 5, 3]), True)
test(Solution().checkIfExist([3, 1, 7, 11]), False)
