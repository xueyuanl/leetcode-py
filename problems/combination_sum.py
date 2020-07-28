class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def recursive(nums, tmp):
            if sum(tmp) > target:
                return
            if sum(tmp) == target:
                res.append(tmp)
                return
            for i in range(len(nums)):
                recursive(nums[i:], tmp + [nums[i]])

        recursive(candidates, [])

        return res
