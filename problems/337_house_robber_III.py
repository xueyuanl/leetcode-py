# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    https://blog.csdn.net/camellhf/article/details/52891319
    """
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.decide_if_rob_node(root))

    def decide_if_rob_node(self, node):
        if not node:
            return 0, 0

        left_value = self.decide_if_rob_node(node.left)
        right_value = self.decide_if_rob_node(node.right)

        # rob this node
        rob_value = node.val + left_value[1] + right_value[1]
        # do not rob this node
        no_rob_value = max(left_value[0], left_value[1]) + max(right_value[0], right_value[1])

        return rob_value, no_rob_value
