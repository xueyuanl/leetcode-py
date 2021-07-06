class Solution(object):
    def maxNumberOfApples(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        s = sorted(arr)

        sum = 0
        res = 0
        for item in arr:
            sum += item
            if sum > 5000:
                break
            else:
                res += 1
        return res