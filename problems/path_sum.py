# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False

        def recursive(node, value):
            if node is None:
                return False
            values = value + node.val
            if values == sum and (node.left is None and node.right is None):
                return True
            return recursive(node.left, values) or recursive(node.right, values)

        return recursive(root, 0)
