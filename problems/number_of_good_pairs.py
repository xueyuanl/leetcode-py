class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        sorted_nums = sorted(nums)

        base = 0
        res = 0
        for i in range(1, length + 1):
            if i < length and sorted_nums[i] == sorted_nums[base]:
                continue

            diff = i - base
            if diff > 1:
                res += diff * (diff - 1) / 2
            base = i
        return res