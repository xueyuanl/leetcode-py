class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        to_sort = []
        for i, v in enumerate(nums):
            to_sort.append([v, i])

        to_sort.sort(reverse=True)
        res = [None for i in range(len(nums))]
        if len(nums) >= 1:
            res[to_sort[0][1]] = 'Gold Medal'
        if len(nums) >= 2:
            res[to_sort[1][1]] = 'Silver Medal'
        if len(nums) >= 3:
            res[to_sort[2][1]] = 'Bronze Medal'

        for i in range(3, len(to_sort)):
            res[to_sort[i][1]] = str(i + 1)
        return res
