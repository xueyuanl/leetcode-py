class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        rows = len(grid)
        cols = len(grid[0])

        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] < 0:
                    res += 1

        return res