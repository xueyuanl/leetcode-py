class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        if len(arr) == 2:
            return [arr]

        min_abs = 10000000

        res = []
        for i in range(1, len(arr)):
            m = arr[i] - arr[i - 1]
            if m < min_abs:
                min_abs = m
                res = [[arr[i - 1], arr[i]]]
            elif m == min_abs:
                res.append([arr[i - 1], arr[i]])

        return res
