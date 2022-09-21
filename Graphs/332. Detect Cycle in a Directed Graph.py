import queue


def cycleBFS(adjList, visited, i):
    q = queue.Queue()
    s = set()
    q.put(i)
    visited[i] = True
    while not q.empty():
        curr = q.get()
        visited[curr] = False
        if curr not in s:
            s.add(curr)
        else:
            return True
        for ele in adjList[curr]:
            if not visited[ele]:
                visited[ele] = True
                q.put(ele)
    return False


def detectCycleInDirectedGraph(n, edges):
    adjList = [[] for _ in range(n + 1)]
    for li in edges:
        u, v = li[0], li[1]
        adjList[u].append(v)    
    visited = [False] * (n + 1)
    #     temp = visited.copy()
    for i in range(1, len(visited)):
        if not visited[i]:
            if cycleBFS(adjList, visited, i):
                return True
    return False


def cycleDFS(adjList, visited, temp, i):
    visited[i] = True
    temp[i] = True
    for ele in adjList[i]:
        if not temp[ele]:
            if cycleDFS(adjList, visited, temp, ele):
                return True
        else:
            return True
    temp[i] = False
    return False


def detectCycleInDirectedGraph(n, edges):
    adjList = [[] for _ in range(n + 1)]
    for li in edges:
        u, v = li[0], li[1]
        adjList[u].append(v)
    visited = [False] * (n + 1)
    temp = visited.copy()
    for i in range(1, len(visited)):
        if not visited[i]:
            if cycleDFS(adjList, visited, temp, i):
                return True
    return False
