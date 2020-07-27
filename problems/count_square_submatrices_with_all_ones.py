class Solution(object):
    """
    refer: https://leetcode.com/problems/count-square-submatrices-with-all-ones/discuss/643429/Python-DP-Solution-%2B-Thinking-Process-Diagrams-(O(mn)-runtime-O(1)-space)
    """
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        row = len(matrix)
        column = len(matrix[0])
        res = 0

        for r in range(row):
            for c in range(column):
                if matrix[r][c] == 1:
                    if r == 0 or c == 0:
                        res += 1
                    else:
                        cell_value = min(matrix[r - 1][c - 1], matrix[r - 1][c], matrix[r][c - 1]) + 1
                        res += cell_value
                        matrix[r][c] = cell_value

        return res
