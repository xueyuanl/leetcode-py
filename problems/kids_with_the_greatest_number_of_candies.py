class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max = -1
        for c in candies:
            if c > max:
                max = c

        res = []
        for c in candies:
            if c + extraCandies >= max:
                res.append(True)
            else:
                res.append(False)

        return res
