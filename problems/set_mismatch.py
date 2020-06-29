class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        hash = [0] * 10001

        for n in nums:
            hash[n] += 1

        res = []
        dup = 0
        miss = 0
        for i in range(1, len(nums) + 1):
            if hash[i] == 2:
                dup = i
            if hash[i] == 0:
                miss = i

        res.extend([dup, miss])
        return res

