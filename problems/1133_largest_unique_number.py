class Solution(object):
    def largestUniqueNumber(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        arr = [0] * 1001
        for a in range(A):
            arr[a] += 1
        for i in range(1001, 0, -1):
            if arr[i] == 1:
                return i
        return -1