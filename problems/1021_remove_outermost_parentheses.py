class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = []
        flag_in_parentheses = 0
        par = 0
        for s in S:
            if s == '(':
                if not flag_in_parentheses:
                    flag_in_parentheses = 1
                else:
                    par += 1
                    res.append(s)
            elif s == ')':
                if flag_in_parentheses:
                    if par > 0:
                        par -= 1
                        res.append(s)
                    else:
                        flag_in_parentheses = 0
        return ''.join(res)
