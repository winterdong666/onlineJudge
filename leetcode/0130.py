class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return
        l = len(board)
        w = len(board[0])
        searched = []
        stack = []
        find = []
        for i in range(l):
            if board[i][0] == 'O':
                searched.append((i, 0))
                stack.append((i, 0))
                find.append((i, 0))
            if board[i][w - 1] == 'O':
                searched.append((i, w - 1))
                stack.append((i, w - 1))
                find.append((i, w - 1))
        for i in range(1, w - 1):
            if board[0][i] == 'O':
                searched.append((0, i))
                stack.append((0, i))
                find.append((0, i))
            if board[l - 1][i] == 'O':
                searched.append((l - 1, i))
                stack.append((l - 1, i))
                find.append((l - 1, i))
        while len(stack) > 0:
            tmp = stack.pop()
            tl, tw = tmp[0], tmp[1]
            if tl > 0 and board[tl - 1][tw] == 'O' and (not ((tl - 1, tw) in searched)):
                searched.append((tl - 1, tw))
                stack.append((tl - 1, tw))
                find.append((tl - 1, tw))
            if tl < l - 1 and board[tl + 1][tw] == 'O' and (not ((tl + 1, tw) in searched)):
                searched.append((tl + 1, tw))
                stack.append((tl + 1, tw))
                find.append((tl + 1, tw))
            if tw > 0 and board[tl][tw - 1] == 'O' and (not ((tl, tw - 1) in searched)):
                searched.append((tl, tw - 1))
                stack.append((tl, tw - 1))
                find.append((tl, tw - 1))
            if tw < w - 1 and board[tl][tw + 1] == 'O' and (not ((tl, tw + 1) in searched)):
                searched.append((tl, tw + 1))
                stack.append((tl, tw + 1))
                find.append((tl, tw + 1))
        for i in range(l):
            for j in range(w):
                board[i][j] = 'X'
        for i in find:
            board[i[0]][i[1]] = 'O'
