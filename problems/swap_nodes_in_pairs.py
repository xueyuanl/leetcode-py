# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def swap(pre, a, b):
            pre.next = b
            a.next = b.next
            b.next = a
            return a

        pre_head = ListNode(0, head)
        leading = pre_head

        current = head
        while current is not None and current.next is not None:
            pre_head = swap(pre_head, current, current.next)
            current = pre_head.next

        return leading.next
