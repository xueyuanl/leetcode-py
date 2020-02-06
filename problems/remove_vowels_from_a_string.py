class Solution(object):
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = 'aeiou'
        res = []
        for i in S:
            if i not in vowels:
                res.append(i)

        return ''.join(res)
