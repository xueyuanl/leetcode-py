import copy


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        self.count = len(nums)

        self.res = []
        self.backtracking([])
        return self.res

    def backtracking(self, sub_set , index ):
        self.res.append(sub_set[:])

        for i in range(index, self.count)


