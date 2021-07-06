# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    a better solution: https://www.polarxiong.com/archives/LeetCode-543-diameter-of-binary-tree.html
    """
    def __init__(self):
        self.maximum = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count_node(root)
        return self.maximum

    def count_node(self, node):
        if not node:
            return 0, 0
        if not node.left and not node.right:
            return 0, 0
        left_node = self.count_node(node.left)
        right_node = self.count_node(node.right)

        one_side = max(left_node[0], right_node[0]) + 1
        if node.left and node.right:
            internal = left_node[0] + right_node[0] + 2
        elif not node.right:
            internal = left_node[0] + 1
        else:
            internal = right_node[0] + 1

        self.maximum = max(self.maximum, internal)
        return one_side, internal
