class Solution(object):
    """
    easy understand explanation: https://cloud.tencent.com/developer/article/1470589
    """
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = [[]]

        for n in nums:
            dup_res = res[:]
            for r in dup_res:
                duplicate = r[:]
                duplicate.append(n)
                res.append(duplicate)

        return res
