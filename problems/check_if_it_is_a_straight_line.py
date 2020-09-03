class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """

        x1 = coordinates[1][0] - coordinates[0][0]
        y1 = coordinates[1][1] - coordinates[0][1]
        for i in range(2, len(coordinates)):
            x2 = coordinates[i][0] - coordinates[0][0]
            y2 = coordinates[i][1] - coordinates[0][1]
            if x1 * y2 != x2 * y1:  # y2 / x2 == y1 / x1 =>> x1 * y2 == x2 * y1
                return False
        return True

        # def get_slope(a, b):
        #     if b[0] - a[0] == 0:
        #         return float(9001)
        #     return float(b[1] - a[1]) / float(b[0] - a[0])
        #
        # slope = get_slope(coordinates[1], coordinates[0])
        #
        # for i in range(2, len(coordinates)):
        #     if get_slope(coordinates[i], coordinates[0]) != slope:
        #         return False
        # return True
