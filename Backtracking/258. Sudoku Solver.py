class Solution:
    def isSafe(self, board, row, col, k):
        for i in range(len(board)):
            if board[row][i] == k:
                return False
            if board[i][col] == k:
                return False
        for i in range(3):
            for j in range(3):
                if board[3 * (row // 3) + i][3 * (col // 3) + j] == k:
                    return False
        return True

    def backtrack(self, board):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    for k in range(1, 10):
                        if self.isSafe(board, i, j, str(k)):
                            board[i][j] = str(k)
                            if self.backtrack(board):
                                return True
                            else:
                                board[i][j] = "."
                    # not able to place anyone in the location
                    return False
        # means rest sudoku is already filled
        return True

    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtrack(board)
