class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        self.count = len(nums)
        self.sorted_nums = sorted(nums)  # sorted first,
        self.res = []
        self.backtracking([], 0)
        return self.res

    def backtracking(self, sub_set, index):
        self.res.append(sub_set[:])

        for i in range(index, self.count):
            if i > index and self.sorted_nums[i] == self.sorted_nums[i - 1]:
                continue
            sub_set.append(self.sorted_nums[i])
            self.backtracking(sub_set, i + 1)
            sub_set.pop()
