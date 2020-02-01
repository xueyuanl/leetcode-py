class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """

        res = ''

        le = len(s)
        if le == 1:
            return str(chr(96 + int(s)))
        i = 0

        while i < le - 2:

            while i < le - 2 and s[i + 2] != '#':
                res += chr(96 + int(s[i]))
                i += 1

            if i != le - 2:
                res += chr(96 + int(s[i:i + 2]))
                i += 3

        if i == le - 2:
            res += chr(96 + int(s[i]))
            res += chr(96 + int(s[i + 1]))
        elif i == le - 1:
            res += chr(96 + int(s[i]))

        return res

