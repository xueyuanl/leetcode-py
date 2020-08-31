class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def get_happy_end(a):
            res = 0
            while a > 0:
                r = a % 10
                a = a // 10
                res += r * r
            return res

        happy = []
        while True:
            happy_end = get_happy_end(n)
            if happy_end == 1:
                return True
            if happy_end in happy:
                return False
            else:
                happy.append(happy_end)
            n = happy_end