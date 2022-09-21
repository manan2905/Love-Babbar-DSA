def backtrack(mat, vis, r, c, n, m, minPath, path):
    if r < 0 or c < 0 or r >= n or c >= m or vis[r][c] == 1 or mat[r][c] == 0:
        return
    if c == m - 1:
        print(path, end=" ")
        minPath[0] = min(minPath[0], len(path))
        return

    vis[r][c] = 1
    backtrack(mat, vis, r + 1, c, n, m, minPath, path + "D")
    backtrack(mat, vis, r - 1, c, n, m, minPath, path + "U")
    backtrack(mat, vis, r, c + 1, n, m, minPath, path + "R")
    backtrack(mat, vis, r, c - 1, n, m, minPath, path + "L")
    vis[r][c] = 0


def printShortest(mat):
    n, m = len(mat), len(mat[0])
    vis = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                if i > 0:
                    mat[i - 1][j] = -1
                if i < n - 1:
                    mat[i + 1][j] = -1
                if j < m - 1:
                    mat[i][j + 1] = -1
                if j > 0:
                    mat[i][j - 1] = -1
    for i in range(n):
        for j in range(m):
            if mat[i][j] == -1:
                mat[i][j] = 0
    minPath = [10000]
    # print(mat)
    for i in range(n):
        print(i, end=' ')
        backtrack(mat, vis, i, 0, n, m, minPath, ".")
        print()
    print(minPath[0])


def takeInput():
    n = int(input("Enter Number of Rows> "))
    mat = [[int(i) for i in input().split()] for _ in range(n)]
    printShortest(mat)


takeInput()
