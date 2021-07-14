class Solution(object):
    """
    refer: https://leetcode.com/problems/valid-number/discuss/360781/Python-with-state-machine-36ms
    """
    # 状态机，当前状态， 输入值，下一状态
    # 遍历终结时，判断当前状态是否在所有合法状态集合里
    def isNumber(self, s):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # states
        start = 0
        int_sign = 1
        integer = 2
        point = 3
        frac = 4
        exp = 5
        exp_sign = 6
        exp_int = 7

        # inputs
        digit = 1
        sign = 2
        dot = 3
        e = 4

        def classify(c):
            if c in '0123456789': return digit
            if c == '.': return dot
            if c in '+-': return sign
            if c in 'eE': return e
            return -1

        state_machine = {
            start: {sign: int_sign, digit: integer, dot: point},
            int_sign: {digit: integer, dot: point},
            integer: {digit: integer, dot: frac, e: exp},
            point: {digit: frac},
            frac: {digit: frac, e: exp},
            exp: {digit: exp_int, sign: exp_sign},
            exp_sign: {digit: exp_int},
            exp_int: {digit: exp_int},
        }

        state = start
        for c in s.strip():
            char_type = classify(c)

            if char_type in state_machine[state]:
                state = state_machine[state][char_type]
            else:
                return False  # input is 'e'
            if state == -1:
                return False  # input like 'abc'
        # string finished, judge if the state is end state
        return state in [integer, frac, exp_int]
