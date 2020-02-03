"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        self.max_depth = 0

        def recursive(node, depth):
            if not node:
                return

            if depth > self.max_depth:
                self.max_depth = depth

            for c in node.children:
                recursive(c, depth + 1)

        recursive(root, 1)
        return self.max_depth

