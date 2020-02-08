class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        if n % 2 != 0:
            return list(range(int(-n / 2), int(n / 2) + 1))
        else:
            return list(range(int(-n / 2), 0)) + list(range(1, int(n / 2) + 1))

