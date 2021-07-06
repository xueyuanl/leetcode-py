# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        l = []
        p = head
        while p:
            l.append((p.val, p))
            p = p.next

        ll = sorted(l)

        for i in range(len(ll) - 1):
            ll[i][1].next = ll[i + 1][1]

        ll[len(ll) - 1][1].next = None

        return ll[0][1]
