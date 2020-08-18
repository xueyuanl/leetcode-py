class Solution(object):
    def __init__(self):
        self.nums = None

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.nums = nums
        if len(nums) == 1:
            return True

        return self.jump(0)

    def jump(self, index):
        res = False
        for j in range(1, self.nums[index] + 1):
            tmp_index = index
            tmp_index += j
            if tmp_index == len(self.nums) - 1:
                res = True
                break
            elif tmp_index > len(self.nums) - 1:
                break
            else:
                if self.jump(tmp_index):
                    res = True

        return res
