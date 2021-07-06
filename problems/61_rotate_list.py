# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        length = 0
        pointer = head

        while pointer:
            length += 1
            pointer = pointer.next

        if length == 0:  # case: [] 0
            return head

        true_k = k % length  # take remainder and do the actual rotate
        if true_k == 0:
            return head

        fast_p = head
        slow_p = head
        for i in range(true_k):
            fast_p = fast_p.next

        while fast_p.next:
            fast_p = fast_p.next
            slow_p = slow_p.next

        fast_p.next = head
        new_head = slow_p.next
        slow_p.next = None
        return new_head
