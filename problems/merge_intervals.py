class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) < 1:
            return []
        res = []
        sorted_intervals = sorted(intervals)

        new_pair = sorted_intervals[0]
        res.append(new_pair)
        for pair in sorted_intervals:
            if pair[0] <= new_pair[1]:
                new_pair[1] = max(pair[1], new_pair[1])
            else:
                new_pair = pair
                res.append(new_pair)

        return res
