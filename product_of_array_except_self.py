class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        size = len(nums)
        res = [1] * size

        left = 1
        for i in range(size - 1):
            left = left * nums[i]
            res[i + 1] *= left

        right = 1
        for i in range(size - 1, 0, -1):
            right = right * nums[i]
            res[i - 1] *= right

        return res
