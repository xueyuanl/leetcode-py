# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    refer: https://www.cnblogs.com/hiddenfox/p/3408931.html
    """
    def detectCycle(self, head):
        walker = head
        runner = head
        meet_node = None
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                meet_node = runner
                break
        if meet_node is None:  # there is no cycle in the list
            return None

        while head != meet_node:
            head = head.next
            meet_node = meet_node.next
        return head

    # use extra space
    # def detectCycle(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     s = set()
    #     while head:
    #         if head not in s:
    #             s.add(head)
    #         else:
    #             return head
    #         head = head.next
    #     return None
