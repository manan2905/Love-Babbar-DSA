import queue


class Solution:

    # def cycleBFS(self, adjList, visited, node):
    #     q = queue.Queue()
    #     visited[node] = True
    #     q.put((node, -1))
    #     while not q.empty():
    #         curr,par = q.get()
    #         for ele in adjList[curr]:
    #             if not visited[ele]:
    #                 visited[ele] = True
    #                 q.put((ele,curr))
    #             elif par != ele:
    #                 return True
    #     return False

    def cycleDFS(self, adjList, visited, node, par):
        visited[node] = True
        for ele in adjList[node]:
            if not visited[ele]:
                if self.cycleDFS(adjList,visited, ele, node):
                    return True
            elif par != ele:
                return True
        return False

    def isCycle(self, n, adjList):
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                if self.cycleDFS(adjList, visited, i, -1):
                    return True
        return False


# Code here

# {
#  Driver Code Starts
if __name__ == '__main__':

    T = int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.isCycle(V, adj)
        if (ans):
            print("1")
        else:
            print("0")

# } Driver Code Ends
