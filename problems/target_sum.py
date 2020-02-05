class Solution(object):
    """
    TODO:
    """
    def findTargetSumWays(self, nums, S):
        """
        time exceeded solution
        :type nums: List[int]
        :type S: int
        :rtype: int
        """

        length = len(nums)
        self.res = 0
        self.nums = nums

        def recursive(sum, i):
            if i == length:
                if sum == S:
                    self.res += 1
                return
            recursive(sum + self.nums[i], i + 1)
            recursive(sum - self.nums[i], i + 1)

        recursive(0, 0)
        return self.res
