class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # dirty solution
        l = [6,
             28,
             496,
             8128,
             33550336,
             8589869056,
             137438691328]

        if num in l:
            return True
        else:
            return False
        # TLE
        # sum = 1
        # for i in range(2, num // 2 + 1):
        #     if num % i == 0:
        #         sum += i
        #
        # if sum == num:
        #     return True
        # else:
        #     return False
