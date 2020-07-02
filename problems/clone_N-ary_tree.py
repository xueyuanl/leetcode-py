# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution(object):
    def cloneTree(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        new_root = Node(root.val, [self.cloneTree(c) for c in root.children])
        return new_root
