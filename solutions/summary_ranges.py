class Solution:
    def summaryRanges(self, nums):
        start = None
        previous = None
        result = []
        for num in nums:
            if num - 1 != previous:
                if start is not None:
                    if previous != start:
                        result.append(f"{start}->{previous}")
                    else:
                        result.append(f"{start}")
                start = num

            previous = num
        if start is not None:
            if previous != start:
                result.append(f"{start}->{previous}")
            else:
                result.append(f"{start}")
        return result
