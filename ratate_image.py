class Solution(object):
    """
    https://www.cnblogs.com/grandyang/p/4389572.html
    """
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        size = len(matrix[0])

        for i in range(size):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(size):
            matrix[i].reverse()
