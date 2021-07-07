class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """

        alphabet = [0] * 26

        for i in range(len(keyboard)):
            alphabet[ord(keyboard[i]) - 97] = i

        base = 0
        res = 0
        for w in word:
            index = alphabet[ord(w) - 97]
            res += abs(index - base)
            base = index
        return res
