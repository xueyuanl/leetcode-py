class Solution(object):
    def __init__(self):
        self.res = []

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def recurse(left, right, string):
            if left == 0 and right == 0:
                res.append(string)
                return

            if left > 0:
                recurse(left - 1, right, string + '(')
            if right > 0 and left < right:
                recurse(left, right - 1, string + ')')

        recurse(n, n, '')

        return res


