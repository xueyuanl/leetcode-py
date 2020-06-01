class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_a = sorted(nums)
        return (sorted_a[-1] - 1) * (sorted_a[-2] - 1)