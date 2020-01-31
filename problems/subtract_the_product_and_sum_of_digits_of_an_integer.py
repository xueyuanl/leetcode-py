class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """

        product = 1
        sums = 0

        while n > 0:
            digit = n % 10
            product *= digit
            sums += digit
            n /= 10

        return product - sums