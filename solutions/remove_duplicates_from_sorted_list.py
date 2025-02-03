# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

class Solution:
    def deleteDuplicates(self, head):
        res = head

        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return res

# TODO: tests
