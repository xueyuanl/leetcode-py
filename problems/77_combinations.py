class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.n = n
        self.k = k
        self.dfs([], 0)
        return self.res

    def dfs(self, case, index):
        if len(case) == self.k:
            self.res.append(case[:])
            return

        for i in range(index, self.n):
            case.append(i + 1)
            self.dfs(case, i + 1)
            case.pop()





