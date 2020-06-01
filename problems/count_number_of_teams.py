class Solution(object):
    """"
    refer: https://leetcode.com/problems/count-number-of-teams/discuss/554795/C%2B%2BJava-O(n-*-n)-and-O(n-log-n)
    """
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """

        res = 0

        l = len(rating)
        for i in range(l):
            left_less, left_more = 0, 0
            right_less, right_more = 0, 0
            for j in range(0, i):
                if rating[j] < rating[i]:
                    left_less += 1
                elif rating[j] > rating[i]:
                    left_more += 1
            for j in range(i + 1, l):
                if rating[j] > rating[i]:
                    right_more += 1
                elif rating[j] < rating[i]:
                    right_less += 1

            res += left_less * right_more + left_more * right_less
        return res
