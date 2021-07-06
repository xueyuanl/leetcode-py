# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        l = len(preorder)
        return self.recursive(preorder, 0, l - 1)

    def recursive(self, tree, l, r):
        if l > r:
            return None
        root_node = TreeNode(tree[l])

        left_begin = l + 1
        left_end = r
        for i in range(l + 1, r + 1):
            if tree[i] > tree[l]:
                left_end = i - 1
                break
        root_node.left = self.recursive(tree, left_begin, left_end)

        right_begin = left_end + 1
        right_end = r
        root_node.right = self.recursive(tree, right_begin, right_end)

        return root_node
