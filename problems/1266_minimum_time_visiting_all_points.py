class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        size = len(points)

        if size == 1 or size == 0:
            return 0
        res = 0
        for i in range(size - 1):
            res += max(abs(points[i][0] - points[i + 1][0]), abs(points[i][1] - points[i + 1][1]))

        return res
