class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n == 0:
            return len(tasks)
        d = {}
        max_task_value = 0
        max_task_number = 0
        for t in tasks:
            if t in d:
                d[t] += 1
            else:
                d[t] = 1
            if d[t] == max_task_value:
                max_task_number += 1
            if d[t] > max_task_value:
                max_task_value = d[t]
                max_task_number = 1

        return max( (max_task_value - 1) * (n + 1) + max_task_number, len(tasks))