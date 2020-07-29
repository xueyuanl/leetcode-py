# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        pointer = head
        prev = ListNode(0, head)
        begin = prev
        broken_point1 = None
        broken_point2 = None
        if m == 1:
            broken_point1 = prev
            broken_point2 = prev.next
        for i in range(m - 1):
            if i == m - 2:
                prev = pointer
                broken_point1 = pointer
                broken_point2 = pointer.next
            pointer = pointer.next

        for i in range(n - m + 1):
            nexts = pointer.next
            pointer.next = prev
            prev = pointer
            pointer = nexts

        broken_point1.next = prev
        broken_point2.next = pointer

        return begin.next
