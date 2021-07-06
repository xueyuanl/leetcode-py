# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_depth = 0

        self.res = 0

        def recursive(node, depth):
            if not node:
                return
            if depth > self.max_depth:
                self.res = node.val
                self.max_depth = depth
            elif depth == self.max_depth:
                self.res += node.val

            recursive(node.left, depth + 1)
            recursive(node.right, depth + 1)

        recursive(root, 1)

        return self.res

