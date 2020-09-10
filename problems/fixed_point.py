class Solution(object):
    def fixedPoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # ugly solution
        for i, v in enumerate(A):
            if i == v:
                return i
        return -1
