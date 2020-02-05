class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """

        length = len(mat)

        l = []
        for i in range(length):
            soldier = mat[i].count(1)
            l.append([soldier, i])

        sorted_l = sorted(l)

        res = []

        for i in range(k):
            res.append(sorted_l[i][1])
        return res