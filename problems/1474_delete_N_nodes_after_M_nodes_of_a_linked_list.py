# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteNodes(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        cur = head
        pre = None
        while cur:
            i, j = m, n
            while cur and i > 0:
                i -= 1
                pre = cur
                cur = cur.next

            while cur and j > 0:
                j -= 1
                cur = cur.next

            pre.next = cur

        return head
