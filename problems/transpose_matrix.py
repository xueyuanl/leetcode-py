class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        trans = []

        for c in range(len(A[0])):
            trans.append([A[r][c] for r in range(len(A))])
        return trans

        # trans = [[0 for i in range(len(A))] for j in range(len(A[0]))]
        #
        # for r in range(len(A)):
        #     for c in range(len(A[0])):
        #         trans[c][r] = A[r][c]
        # return trans
