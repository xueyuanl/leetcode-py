class Solution(object):
    """
    refer to: https://leetcode-cn.com/problems/3sum/solution/pai-xu-shuang-zhi-zhen-zhu-xing-jie-shi-python3-by/
    """

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        length = len(nums)
        if length < 3:
            return []

        res = []
        sn = sorted(nums)
        for i in range(length):
            if sn[i] > 0:
                return res
            if i > 0 and sn[i] == sn[i - 1]:
                continue
            l = i + 1
            r = length - 1
            while l < r:
                if sn[i] + sn[l] + sn[r] == 0:
                    res.append([sn[i], sn[l], sn[r]])
                    while l < r and sn[l] == sn[l + 1]:
                        l += 1
                    while l < r and sn[r] == sn[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif sn[i] + sn[l] + sn[r] > 0:
                    r -= 1
                else:
                    l += 1
        return res
