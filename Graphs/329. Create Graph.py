def takeinput():
    s = [int(i) for i in input().split()]
    n, m = s[0], s[1]
    # considering a 0-based Undirected graph
    adjMatrix = [[0 for _ in range(n)] for _ in range(n)]
    # making adjacency list
    adjList = [[] for _ in range(n)]
    for _ in range(m):
        s = [int(i) for i in input().split()]
        u, v = s[0], s[1]
        # Adjacency matrix
        adjMatrix[u][v] = 1
        adjMatrix[v][u] = 1
        # Adjacency List
        adjList[u].append(v)
        adjList[v].append(u)

    print(adjList)
    print(adjMatrix)


takeinput()
