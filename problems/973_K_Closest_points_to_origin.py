class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        length = len(points)
        if K == length:
            return points

        square_list = []
        for point in points:
            sum_square = point[0] ** 2 + point[1] ** 2
            square_list.append((sum_square, point))

        sorted_square_list = sorted(square_list)
        res = []

        for i in range(K):
            res.append(sorted_square_list[i][1])

        return res