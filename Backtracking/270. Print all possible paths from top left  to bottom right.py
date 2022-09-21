def backtrack(mat, vis, r, c, n, m, currPath, paths):
    if r < 0 or c < 0 or c == m or r == n or vis[r][c] == 1:
        return

    if r == n - 1 and c == m - 1:
        currPath.append(mat[r][c])
        paths.append(currPath.copy())
        currPath.pop()
        return
    vis[r][c] = 1
    currPath.append(mat[r][c])
    backtrack(mat, vis, r + 1, c, n, m, currPath, paths)
    backtrack(mat, vis, r, c + 1, n, m, currPath, paths)
    vis[r][c] = 0
    currPath.pop()


def printPaths(mat):
    paths = []
    n, m = len(mat), len(mat[0])
    vis = [[0 for _ in range(m)] for _ in range(n)]
    backtrack(mat, vis, 0, 0, n, m, [], paths)
    for ele in paths:
        print(*ele)


def takeInput():
    n = int(input("Enter Number of Rows>> "))
    mat = [[int(i) for i in input().split()] for _ in range(n)]
    printPaths(mat)


takeInput()
