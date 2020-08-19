class Solution(object):
    def __init__(self):
        self.nums = None

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        cover = 0
        for i in range(len(nums)):
            if cover < i:
                return False  # [1, 0, 0]
            cover = max(cover, nums[i] + i)
            if cover >= len(nums) - 1:
                return True
        return False
