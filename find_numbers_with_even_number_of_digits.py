class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = 0

        for n in nums:
            if len(str(n)) % 2 == 0:
                res += 1
        return res
