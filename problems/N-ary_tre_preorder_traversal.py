"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []

        def recursive(node):
            if not node:
                return
            res.append(node.val)
            for i in node.children:
                recursive(i)

        recursive(root)
        return res

    # iteratively method
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        from collections import deque
        res = []
        if not root: return res
        d = deque()

        d.append(root)
        while d:
            pop = d.pop()
            res.append(pop.val)
            d.extend(pop.children[::-1])

        return res

