class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        le = len(height)
        i = 0
        j = le - 1
        maximum = 0
        while i < j:
            maximum = max(maximum, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return maximum
