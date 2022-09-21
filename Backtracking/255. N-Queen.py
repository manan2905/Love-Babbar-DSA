# User function Template for python3

class Solution:
    def isSafe(self, board, r, c):
        # check left row
        for i in range(c, -1, -1):
            if board[r][i] == 1:
                return False
        # check upper left
        i, j = r - 1, c - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1
        # check lower left
        i, j = r + 1, c - 1
        while i < len(board) and j >= 0:
            if board[i][j] == 1:
                return False
            i += 1
            j -= 1
        return True

    def backtrack(self, board, col, ans):
        if col == len(board):
            r = []
            for i in range(len(board)):
                for j in range(len(board)):
                    if board[i][j] == 1:
                        r.append(j + 1)
            ans.append(r.copy())
            return

        for i in range(len(board)):
            if self.isSafe(board, i, col):
                board[i][col] = 1
                self.backtrack(board, col + 1, ans)
                board[i][col] = 0

    def nQueen(self, n):
        # code here
        board = [[0 for _ in range(n)] for _ in range(n)]
        ans = []
        self.backtrack(board, 0, ans)
        return sorted(ans)


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        ans = ob.nQueen(n)
        if (len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[", end="")
                for j in range(len(ans[i])):
                    print(ans[i][j], end=" ")
                print("]", end=" ")
            print()

# } Driver Code Ends
