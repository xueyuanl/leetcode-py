# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getLonelyNodes(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []

        def recursive(node):
            if node.left and not node.right:
                res.append(node.left.val)
                recursive(node.left)
            elif not node.left and node.right:
                res.append(node.right.val)
                recursive(node.right)
            elif node.left and node.right:
                recursive(node.left)
                recursive(node.right)

        recursive(root)
        return res
