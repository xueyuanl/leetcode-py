class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l1 = len(s1)
        l2 = len(s2)
        sliding_window = [0] * 26

        for i in range(l1):
            sliding_window[ord(s1[i]) - 97] -= 1
            sliding_window[ord(s2[i]) - 97] += 1

        zero_num = 0
        for s in sliding_window:
            if s == 0:
                zero_num += 1

        if zero_num == 26:
            return True

        for i in range(l1, l2):
            new_slide = ord(s2[i]) - 97
            old_slide = ord(s2[i - l1]) - 97
            sliding_window[new_slide] += 1
            if sliding_window[new_slide] == 0:
                zero_num += 1
            if sliding_window[new_slide] == 1:
                zero_num -= 1
            sliding_window[old_slide] -= 1
            if sliding_window[old_slide] == 0:
                zero_num += 1
            if sliding_window[old_slide] == -1:
                zero_num -= 1

            if zero_num == 26:
                return True
        return False
