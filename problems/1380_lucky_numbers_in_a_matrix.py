class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        col = len(matrix[0])
        row = len(matrix)
        res = []
        for c in range(col):
            max = 0
            rr = 0
            for r in range(row):
                if matrix[r][c] > max:
                    max = matrix[r][c]
                    rr = r
            flag = True
            for cc in range(col):
                if matrix[rr][cc] < max:
                    flag = False
            if flag:
                res.append(max)

        return res