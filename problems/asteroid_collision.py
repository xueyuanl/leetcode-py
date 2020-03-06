class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        res = []

        def can_append(tail, new):
            if new > 0 and tail > 0:
                return True
            if new < 0 and tail < 0:
                return True
            if tail < 0 < new:
                return True
            return False

        def can_replace(tail, new):
            if new < 0 < tail < abs(new):
                return True
            return False

        def can_destroy(tail, new):
            if new < 0 < tail and abs(new) == tail:
                return True
            return False

        for a in asteroids:
            if not res:
                res.append(a)
            else:
                flag = 0
                while res:
                    if can_append(res[-1], a):
                        res.append(a)
                        flag = 0
                        break
                    elif can_replace(res[-1], a):
                        res.pop()
                        flag = 1
                    elif can_destroy(res[-1], a):
                        res.pop()
                        flag = 0
                        break
                    else:
                        flag = 0
                        break
                if flag:
                    res.append(a)
        return res
