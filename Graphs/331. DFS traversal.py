# User function Template for python3

class Solution:
    def trav(self, adjList, ans, i, visited):
        ans.append(i)
        visited[i] = 1
        for ele in adjList[i]:
            if not visited[ele]:
                self.trav(adjList, ans, ele, visited)

    def dfsOfGraph(self, V, adj):
        # code here
        ans = []
        visited = [False] * V
        self.trav(adj, ans, 0, visited)
        return ans


# {
#  Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    while T > 0:
        V, E = map(int, input().split())
        adj = [[] for i in range(V + 1)]
        for i in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob = Solution()
        ans = ob.dfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()
        T -= 1
# } Driver Code Ends