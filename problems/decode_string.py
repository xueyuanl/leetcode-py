class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.size = len(s)
        return self.recursive(s)

    def recursive(self, s):
        res = ''
        i = 0
        number = 0
        while i < self.size:
            if s[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                number, j = self.get_number(i, s)
                i = j
            elif s[i] == '[':
                j = self.get_braket(i, s)
                s_tmp = self.recursive(s[i + 1:j])
                res += s_tmp * number
                i = j + 1
            else:
                res += s[i]
                i += 1
        return res

    def get_braket(self, index, s):
        brackets = 0

        for i in range(index, len(s)):
            if s[i] == '[':
                brackets += 1
            if s[i] == ']':
                brackets -= 1
            if brackets == 0:
                return i

    def get_number(self, index, s):
        res = '' + s[index]
        for i in range(index + 1, self.size):
            if s[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                res = res + s[i]
            else:
                return int(res), i
