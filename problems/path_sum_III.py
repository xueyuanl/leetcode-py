# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.res = 0

        def recursive_path(node, value):
            if node is None:
                return
            values = value + node.val
            if values == sum:
                self.res += 1

            recursive_path(node.left, values)
            recursive_path(node.right, values)

        def recursive_node(node):
            if node is None:
                return

            recursive_path(node, 0)
            recursive_node(node.left)
            recursive_node(node.right)

        recursive_node(root)

        return self.res
