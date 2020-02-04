class Solution(object):
    """
    a quite confused problem
    """
    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """

        even, odd = 0, 0
        for i in chips:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1

        return min(even, odd)