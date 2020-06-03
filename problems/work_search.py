class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.word = word
        self.board = board
        self.length = len(board[0])
        self.high = len(board)
        self.len_word = len(word)

        for h in range(self.high):
            for l in range(self.length):
                if self.backtrack(0, h, l):
                    return True
        return False

    def backtrack(self, count, h, l):
        if count == self.len_word:
            return True

        if h == -1 or l == -1 or h == self.high or l == self.length or self.board[h][l] != self.word[count]:
            return False
        # mark as visited
        tmp = self.board[h][l]
        self.board[h][l] = ' '

        res = self.backtrack(count + 1, h, l - 1) or \
              self.backtrack(count + 1, h, l + 1) or \
              self.backtrack(count + 1, h - 1, l) or \
              self.backtrack(count + 1, h + 1, l)
        self.board[h][l] = tmp
        return res
