# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.sum = 0

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.recursive(root)
        return self.sum

    def recursive(self, node):
        if node is None:
            return
        self.recursive(node.left)
        self.recursive(node.right)
        a = node.left.val if node.left else 0
        b = node.right.val if node.right else 0
        node.val += a + b
        self.sum += abs(a - b)

