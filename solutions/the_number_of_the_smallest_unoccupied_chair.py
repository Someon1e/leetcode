# https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/

from heapq import heappush, heappop


class Solution:
    def smallestChair(self, times, targetFriend: int) -> int:
        friends = len(times)

        empty, occupied = list(range(friends)), []

        for i in sorted(range(friends), key=lambda x: times[x][0]):
            arrive, leave = times[i]

            while occupied and occupied[0][0] <= arrive:
                heappush(empty, heappop(occupied)[1])
            seat = heappop(empty)

            if i == targetFriend:
                return seat

            heappush(occupied, (leave, seat))


from leetcode import test

test(Solution().smallestChair([[1, 4], [2, 3], [4, 6]], 1), 1)
test(Solution().smallestChair([[3, 10], [1, 5], [2, 6]], 0), 2)
