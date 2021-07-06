class Solution(object):

    def validSubarrays(self, nums):
        """
        Time Limit Exceeded solution
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        length = len(nums)

        for i in range(length - 1, -1, -1):
            minimum = 100000
            for j in range(i, -1, -1):
                if nums[j] < minimum:
                    res += 1
        return res

    def validSubarrays(self, nums):
        res = 0

        stack = []

        for n in nums:
            while stack and stack[-1] > n:
                stack.pop()

            res += len(stack)
        return res
