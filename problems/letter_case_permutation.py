class Solution(object):

    def __init__(self):
        self.s = None
        self.length = None
        self.res = []

    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        self.s = S
        self.length = len(S)
        self.backtrack('', 0)
        return self.res

    def backtrack(self, sub, i):
        if i == self.length - 1:
            self.res.append(sub)
            return
        if self.s[i].isalpha():
            self.backtrack(sub + self.s[i].swapcase(), i + 1)

        self.backtrack(sub + self.s[i], i + 1)
