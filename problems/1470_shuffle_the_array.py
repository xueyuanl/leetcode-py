class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """

        res = [0] * len(nums)
        res_i = 0
        for i in range(n):
            res[res_i] = nums[i]
            res[res_i + 1] = nums[i + n]
            res_i += 2
        return res
