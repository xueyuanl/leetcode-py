class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """

        def maximum69Number(self, num: int) -> int:
            ss = str(num)
            res = ''
            flag = 0
            for k, v in enumerate(ss):
                if v == '6' and flag == 0:
                    res += '9'
                    flag = 1
                else:
                    res += v
            return int(res)
