class Solution(object):
    def sumOfDigits(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        _min = min(A)

        sum = 0

        while _min > 0:
            sum += _min % 10
            _min = _min / 10

        if sum & 1 == 1:
            return 0
        return 1
