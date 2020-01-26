import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        heap = []
        d = {}

        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        for key, v in d.items():
            heapq.heappush(heap, (v, key))
            if len(heap) > k:
                heapq.heappop(heap)

        return [ t[1] for t in heap]
