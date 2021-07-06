# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        if fast is not None:  # odd nodes
            slow = slow.next

        # reverse the right half list
        prev = None
        node = slow
        while node is not None:
            next = node.next
            node.next = prev
            prev = node
            node = next

        while prev is not None:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True