class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        frequency = [0] * 501
        for i in arr:
            frequency[i] += 1
        max_value = -1
        for i in range(500, 0, -1):
            if frequency[i] == i and i > max_value:  # frequency equal to value
                max_value = i
        return max_value
