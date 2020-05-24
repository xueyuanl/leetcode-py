class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''

        m = {}

        l = len(s)
        for i in range(l):
            ch = s[i]
            if ch in m:
                m[ch] += 1
            else:
                m[ch] = 1

        cf = []  # character_frequency
        for key in m:
            cf.append((m[key], key))

        sorted_cf = sorted(cf, reverse=True)

        res = []

        for i in sorted_cf:
            res.append(i[1] * i[0])

        return ''.join(res)
