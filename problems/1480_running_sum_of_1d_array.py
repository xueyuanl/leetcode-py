class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        res = [0] * length

        sum = 0
        for i in range(length):
            sum += nums[i]
            res[i] = sum

        return res
