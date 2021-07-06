class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """

        frequency_chars = [0] * 27

        for c in chars:
            frequency_chars[ord(c) - 96] += 1

        res = 0
        for word in words:
            if self.check(word, frequency_chars[:]):
                res += len(word)
        return res

    def check(self, word, chars):
        for w in word:
            if chars[ord(w) - 96] == 0:
                return False
            chars[ord(w) - 96] -= 1
        return True
