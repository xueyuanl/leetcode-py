class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        length = len(flowerbed)
        zero_max = 0

        can_planted = 0
        for i in range(length):
            if flowerbed[i] == 0:
                zero_max += 1
                if i == 0:
                    zero_max += 1
            if flowerbed[i] == 1:
                if zero_max > 0:
                    can_planted += int((zero_max - 1) / 2)
                    zero_max = 0

        if zero_max > 0:
            zero_max += 1
            can_planted += int((zero_max - 1) / 2)

        if can_planted < n:
            return False
        return True
