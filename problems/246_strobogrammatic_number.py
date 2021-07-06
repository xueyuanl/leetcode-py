class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """

        false_set = ['2', '3', '4', '5', '7']

        for n in num:
            if n in false_set:
                return False

        length = len(num)

        for i in range(int(length / 2) + 1):
            symmetry = length - 1 - i
            if i == symmetry and num[i] in ['6', '9']:
                return False
            if num[i] == '6':
                if num[symmetry] == '9':
                    continue
                else:
                    return False
            if num[i] == '9':
                if num[symmetry] == '6':
                    continue
                else:
                    return False
            if num[i] != num[symmetry]:
                return False

        return True

