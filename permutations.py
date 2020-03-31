import copy

class Solution(object):
    """
    reference: https://blog.csdn.net/xiazdong/article/details/7986015
    """

    def __init__(self):
        self.res = []

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self._perm_recursion(nums, 0, len(nums))
        return self.res

    def _perm_recursion(self, nums, begin, end):
        if begin == end:
            self.res.append(copy.copy(nums))
        else:

            for i in range(begin, end):
                nums[i], nums[begin] = nums[begin], nums[i]
                self._perm_recursion(nums, begin + 1, end)
                nums[i], nums[begin] = nums[begin], nums[i]


if __name__ == '__main__':
    s = Solution()
    s.permute([1, 2, 3])
