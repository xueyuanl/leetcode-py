# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """

        res = 0

        iter = head

        while iter:
            res = res * 2 + iter.val
            iter = iter.next

        return res
