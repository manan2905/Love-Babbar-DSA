def isSafe(board, r, c, n):
    if r < 0 or c < 0 or r >= n or c >= n or board[r][c] != -1:
        return False
    return True


def backtrack(board, r, c, rm, cm, n, move_number):
    if move_number == n * n:
        return True
    for i in range(8):
        nr = r + rm[i]
        nc = c + cm[i]
        if isSafe(board, nr, nc, n):
            board[nr][nc] = move_number
            if backtrack(board, nr, nc, rm, cm, n, move_number + 1):
                return True
            board[nr][nc] = -1
    return False


def takeInput():
    n = int(input())
    board = [[-1 for _ in range(n)] for _ in range(n)]
    row_moves = [1, -1, 1, -1, 2, 2, -2, -2]
    col_moves = [-2, -2, 2, 2, 1, -1, 1, -1]
    backtrack(board, 0, 0, row_moves, col_moves, n, 1)
    board[0][0] = 0
    for li in board:
        print(*li)


takeInput()
