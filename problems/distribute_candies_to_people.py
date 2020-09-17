class Solution(object):
    """
    refer: https://leetcode.com/problems/distribute-candies-to-people/discuss/323364/JavaC%2B%2BPython-O(sqrt(candies))-with-explanation
    """
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        res = [0] * num_people
        i = 0
        while candies > 0:
            res[i % num_people] += min(candies, i + 1)
            candies -= i + 1
            i += 1
        return res
