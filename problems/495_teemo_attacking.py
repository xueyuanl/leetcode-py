class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if len(timeSeries) == 0:
            return 0
        res = 0
        poisoned_time = timeSeries[0]
        for t in timeSeries:
            if t >= poisoned_time:
                res += duration
            else:
                res += t + duration - poisoned_time
            poisoned_time = t + duration

        return res
