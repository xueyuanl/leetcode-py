class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """

        nums = high - low + 1

        if low & 1 == 1:  # low is odd number
            if nums & 1 == 1:
                return nums // 2 + 1
            else:
                return nums // 2
        else:
            return nums // 2
