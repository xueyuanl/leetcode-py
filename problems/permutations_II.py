import copy
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.count = len(nums)
        maps = {}
        for n in nums:
            c = str(n)
            if c in maps:
                maps[c] += 1
            else:
                maps[c] = 1

        self.res = []
        self.backtracking([], maps)
        return self.res

    def backtracking(self, permu, maps):
        if len(permu) == self.count:
            self.res.append(copy.copy(permu))
            return

        for m in maps:
            if maps[m] == 0:
                continue
            maps[m] -= 1
            permu.append(int(m))
            self.backtracking(permu, maps)
            permu.pop()
            maps[m] += 1


if __name__ == '__main__':
    s = Solution()
    s.permuteUnique([1, 1, 2])
