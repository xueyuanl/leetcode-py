# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]preorder = [3,9,20,15,7]
        :type inorder: List[int]inorder = [9,3,15,20,7]
        :rtype: TreeNode
        """
        l_pre = len(preorder)
        l_in = len(inorder)
        return self.recursive(preorder, 0, l_pre - 1, inorder, 0, l_in - 1)

    def recursive(self, preorder, p_l, p_r, inorder, i_l, i_r):
        if p_l > p_r:  # the tree list is empty
            return None

        root = TreeNode(preorder[p_l])

        root_index_in_inorder = None
        for i in range(i_l, i_r + 1):
            if preorder[p_l] == inorder[i]:
                root_index_in_inorder = i

        # construct left tree
        left_tree_preorder_l = p_l + 1
        left_tree_preorder_r = p_l + (root_index_in_inorder - i_l)

        left_tree_inorder_l = i_l
        left_tree_inorder_r = root_index_in_inorder - 1

        root.left = self.recursive(preorder, left_tree_preorder_l, left_tree_preorder_r,
                                   inorder, left_tree_inorder_l, left_tree_inorder_r)

        # construct right tree
        right_tree_preorder_l = left_tree_preorder_r + 1
        right_tree_preorder_r = p_r

        right_tree_inorder_l = root_index_in_inorder + 1
        right_tree_inorder_r = i_r

        root.right = self.recursive(preorder, right_tree_preorder_l, right_tree_preorder_r,
                                   inorder, right_tree_inorder_l, right_tree_inorder_r)

        return root
