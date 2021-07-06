def mapadd(map, key):
    if key in map:
        map[key] += 1
    else:
        map[key] = 1


class Solution(object):
    """
    refer: https://github.com/labuladong/fucking-algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E6%8A%80%E5%B7%A7.md
    """
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        left, right = 0, 0
        length = len(s)
        res_start, min_len = 0, length + 1

        needs = {}
        for tt in t:
            mapadd(needs, tt)

        window = {}
        matched = 0  # mark how many characters is matched

        while right < length:
            c = s[right]
            if c in needs:
                mapadd(window, c)
                if window[c] == needs[c]:
                    matched += 1
            right += 1

            while matched == len(needs):
                # update res
                if right - left < min_len:
                    res_start, min_len = left, right - left
                c2 = s[left]
                if c2 in needs:
                    window[c2] -= 1
                    if window[c2] < needs[c2]:
                        matched -= 1
                left += 1

        if min_len == length + 1:
            return ''
        return s[res_start:res_start + min_len]
