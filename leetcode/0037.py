def isValidSudoku(board):
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

class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def DFS(board, left, flag):
            if left < 0:
                return True
            x = left // 9
            y = left % 9
            if board[x][y] != ".":
                return DFS(board, left - 1, flag)
            else:
                for i in range(1, 10):
                    board[x][y] = str(i)
                    if isValidSudoku(board):
                        if DFS(board, left - 1, flag):
                            return True
                    else:
                        board[x][y] = "."
            board[x][y] = "."
            return False
        DFS(board, 80, False)
        
        
