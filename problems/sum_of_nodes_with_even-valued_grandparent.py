# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.res = 0
        def add_value(node):
            sum = 0
            if node.left:
                if node.left.left:
                    sum += node.left.left.val
                if node.left.right:
                    sum += node.left.right.val
            if node.right:
                if node.right.left:
                    sum += node.right.left.val
                if node.right.right:
                    sum += node.right.right.val
            return sum


        def recursive_node(node):
            if node is None:
                return
            if node.val % 2 == 0:
                self.res += add_value(node)
            recursive_node(node.left)
            recursive_node(node.right)

        recursive_node(root)
        return self.res