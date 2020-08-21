from common.search import binary_search


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # find pivot point
        pivot = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                pivot = i
                break
        a = binary_search(nums, target, 0, pivot)
        b = binary_search(nums, target, pivot + 1, len(nums) - 1)
        if a:
            return a
        elif b:
            return b
        else:
            return -1
