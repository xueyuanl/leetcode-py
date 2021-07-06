class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """

        matrix = [[0 for i in range(m)] for j in range(n)]
        res = 0
        for x, y in indices:
            for i in range(m):
                matrix[x][i] += 1
                if matrix[x][i] & 1 == 1:
                    res += 1
                else:
                    res -= 1
            for j in range(n):
                matrix[j][y] += 1
                if matrix[j][y] & 1 == 1:
                    res += 1
                else:
                    res -= 1
        return res
