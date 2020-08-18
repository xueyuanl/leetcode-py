class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        red, white, blue = 0, 0, 0

        for i in range(len(nums)):
            if nums[i] == 0:
                red += 1
            elif nums[i] == 1:
                white += 1
            else:
                blue += 1

        nums[:red] = [0] * red
        nums[red:red + white] = [1] * white
        nums[red + white: red + white + blue] = [2] * blue

