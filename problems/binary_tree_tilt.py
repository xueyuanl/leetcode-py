# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum = 0

        def recursive(node):
            if node is None:
                return
            recursive(node.left)
            recursive(node.right)
            tilt = node.left.val if node.left else 0 + node.right.val if node.right else 0
            node.val += tilt
            sum += abs(node.left.val if node.left else 0, node.right.val if node.right else 0)

        return sum