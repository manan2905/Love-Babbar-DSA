import queue


class Solution:
    def BFScheck(self, adj, node, colors, visited):
        colors[node] = 0
        visited[node] = True
        q = queue.Queue()
        q.put((node, 0))
        while not q.empty():
            curr, color = q.get()
            for ele in adj[curr]:
                if colors[ele] == -1:
                    colors[ele] = 1 - color
                    visited[ele] = True
                    q.put((ele, 1 - color))
                elif colors[ele] == color:
                    return False
        return True

    def DFScheck(self, adj, node, colors, visited, color):
        visited[node] = True
        colors[node] = color
        for ele in adj[node]:
            if colors[ele] == -1:
                if not self.DFScheck(adj, ele, colors, visited, 1 - color):
                    return False
            elif colors[ele] == color:
                return False
        return True

    def isBipartite(self, V, adj):
        colors = [-1] * V
        visited = [False] * V
        for i in range(V):
            if not visited[i]:
                if not self.DFScheck(adj, i, colors, visited, 0):
                    return False
        return True


# code here


# {
#  Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.isBipartite(V, adj)
        if (ans):
            print("1")
        else:
            print("0")

# } Driver Code Ends
