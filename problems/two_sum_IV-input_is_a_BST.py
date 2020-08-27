# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.s = set()
        self.k = None

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.k = k
        return self.recursive(root)

    def recursive(self, node):
        if node is None:
            return False
        if self.recursive(node.left):
            return True
        if self.k - node.val in self.s:
            return True
        else:
            self.s.add(node.val)
        if self.recursive(node.right):
            return True
