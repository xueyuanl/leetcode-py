class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        for i in range(len(A)):
            A[i] = A[i] ** 2

        a_sorted = sorted(A)
        return a_sorted
