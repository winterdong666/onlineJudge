class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            check = [0] * 9
            for j in board[i]:
                if j != ".":
                    check[int(j) - 1] += 1
                    if check[int(j) - 1] > 1:
                        return False
        for i in range(9):
            check = [0] * 9
            for j in range(9):
                if board[j][i] != ".":
                    check[int(board[j][i]) - 1] += 1
                    if check[int(board[j][i]) - 1] > 1:
                        return False
        for i in range(3):
            for j in range(3):
                check = [0] * 9
                for k in range(3):
                    for l in range(3):
                        if board[i * 3 + k][j * 3 + l] != ".":
                            check[int(board[i * 3 + k][j * 3 + l]) - 1] += 1
                            if check[int(board[i * 3 + k][j * 3 + l]) - 1] > 1:
                                return False
        return True
