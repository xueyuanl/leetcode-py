class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        sorted_list = sorted(nums)

        res = [0] * length

        for n in range(length):
            i = sorted_list.index(nums[n])
            while i - 1 >= 0 and sorted_list[i - 1] == sorted_list[i]:
                i -= 1
            res[n] = i

        return res
