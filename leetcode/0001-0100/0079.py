class Solution:
    def exist(self, board: 'List[List[str]]', word: 'str') -> 'bool':
        def existHelper(board, word, i, j):
            if board[i][j] == word[0]:
                if word[1:] == "":
                    return True
                board[i][j] = " "
                if i > 0 and existHelper(board, word[1:], i - 1, j):
                    return True
                if i < len(board) - 1 and existHelper(board, word[1:], i + 1, j):
                    return True
                if j > 0 and existHelper(board, word[1:], i, j - 1):
                    return True
                if j < len(board[0]) - 1 and existHelper(board, word[1:], i, j + 1):
                    return True
                board[i][j] = word[0]
                return False
            else:
                return False
        if word == "":
            return True
        if len(board) == 0:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if existHelper(board, word, i, j):
                    return True
        return False
