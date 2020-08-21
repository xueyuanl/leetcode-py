"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        l = [root]
        index = -1

        while index != len(l) - 1:
            index += 1
            if l[index].left:
                l.append(l[index].left)
            if l[index].right:
                l.append(l[index].right)

        for i in range(len(l) - 2):
            l[i].next = l[i + 1]

        i = -1
        p = 0
        while i + pow(2, p) <= len(l) - 1:
            l[i + pow(2, p)].next = None
            i = i + pow(2, p)
            p += 1

