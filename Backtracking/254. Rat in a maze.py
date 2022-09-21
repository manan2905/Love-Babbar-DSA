class Solution:
    def isValid(self, r, c, grid, mat, n):
        if r < 0 or r == n or c == n or c < 0 or mat[r][c] == 0 or grid[r][c] == 1:
            return False
        return True

    def backtrack(self, grid, mat, r, c, s, ans, n):

        if not self.isValid(r, c, grid, mat, n):
            return
        if r == n - 1 and c == n - 1:
            ans.append(s)
            return
        grid[r][c] = 1
        self.backtrack(grid, mat, r + 1, c, s + "D", ans, n)
        self.backtrack(grid, mat, r, c + 1, s + "R", ans, n)
        self.backtrack(grid, mat, r - 1, c, s + "U", ans, n)
        self.backtrack(grid, mat, r, c - 1, s + "L", ans, n)
        grid[r][c] = 0

    def findPath(self, m, n):
        # code here
        grid = [[0 for _ in range(n)] for _ in range(n)]
        ans = []
        self.backtrack(grid, m, 0, 0, "", ans, n)
        # print(ans)
        return ans


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))

        matrix = [[0 for i in range(n[0])] for j in range(n[0])]
        k = 0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k += 1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0:
            print(-1)
        else:
            for x in result:
                print(x, end=" ")
            print()
# } Driver Code Ends
