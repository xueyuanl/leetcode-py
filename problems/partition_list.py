# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None
        value_list = []
        while head:
            value_list.append([head.val, head])
            head = head.next

        p_less = None
        p_more = None
        less_head = None
        more_head = None
        for i in range(len(value_list)):
            if value_list[i][0] < x:
                if less_head is None:
                    p_less = value_list[i][1]
                    less_head = p_less
                else:
                    p_less.next = value_list[i][1]
                    p_less = p_less.next
            else:
                if more_head is None:
                    p_more = value_list[i][1]
                    more_head = p_more
                else:
                    p_more.next = value_list[i][1]
                    p_more = p_more.next
        if p_less:
            p_less.next = more_head
        if p_more:
            p_more.next = None
        return less_head if less_head else more_head

    # a better solution
    #
    # def partition(self, head, x):
    #     h1 = l1 = ListNode(0)
    #     h2 = l2 = ListNode(0)
    #     while head:
    #         if head.val < x:
    #             l1.next = head
    #             l1 = l1.next
    #         else:
    #             l2.next = head
    #             l2 = l2.next
    #         head = head.next
    #     l2.next = None
    #     l1.next = h2.next
    #     return h1.next
