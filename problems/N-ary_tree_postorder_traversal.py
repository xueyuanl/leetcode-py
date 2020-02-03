"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        res = []

        def recursive(node):
            if not node:
                return
            for i in node.children:
                recursive(i)
            res.append(node.val)

        recursive(root)
        return res