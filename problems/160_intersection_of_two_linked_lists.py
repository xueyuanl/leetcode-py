# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        if headA is None or headB is None:
            return None

        a = headA
        b = headB
        while a is not b:
            a = headB if a is None else a.next
            b = headA if b is None else b.next
        return a

        # s = set()
        # while headA:
        #     s.add(headA)
        #     headA = headA.next
        #
        # while headB:
        #     if headB in s:
        #         return headB
        #     headB = headB.next
        # return None
