# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        minimum = 1
        maximum = n

        while minimum < maximum:
            midpoint = (minimum + maximum) // 2
            if isBadVersion(midpoint):
                maximum = midpoint
            else:
                minimum = midpoint + 1

        return minimum
