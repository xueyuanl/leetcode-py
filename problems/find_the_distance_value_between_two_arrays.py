class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        res = 0
        for i in arr1:
            for j in arr2:
                if abs(i-j) <= d:
                    break
            else:
                res += 1
        return res
