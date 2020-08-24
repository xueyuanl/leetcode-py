class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

        A, B = 0, 0
        d = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                if secret[i] not in d:
                    d[secret[i]] = 1
                else:
                    if d[secret[i]] < 0:
                        B += 1
                        d[secret[i]] += 1
                    else:
                        d[secret[i]] += 1
                if guess[i] not in d:
                    d[guess[i]] = -1
                else:
                    if d[guess[i]] > 0:
                        B += 1
                        d[guess[i]] -= 1
                    else:
                        d[guess[i]] -= 1
        return ''.join([str(A), 'A', str(B), 'B'])