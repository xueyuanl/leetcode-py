class Solution(object):
    def isArmstrong(self, N):
        """
        :type N: int
        :rtype: bool
        """
        n = N
        sum = 0
        power = len(str(N))
        while n > 0:
            tail = n % 10
            n /= 10
            sum += pow(tail, power)
            if sum > N:
                return False

        if sum < N:
            return False
        return True