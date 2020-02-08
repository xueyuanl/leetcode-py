# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        def get_rright(node):
            if node.right is None:
                return node
            return get_rright(node.right)



        def recursive(node):
            if node is None:
                return
            if node.left is None:
                return
            tmp_right = node.right
            node.right = node.left
            node.left = None

            recursive(node.right)
            rright = get_rright(node)
            rright.right = tmp_right
            recursive(rright.right)

        recursive(root)