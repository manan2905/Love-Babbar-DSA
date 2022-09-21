# User function Template for python3
import queue


class Solution:

    def bfs(self, adjList, visited, i):
        q = queue.Queue()
        visited[i] = True
        q.put(i)
        ans = []
        while not q.empty():
            curr = q.get()
            ans.append(curr)
            for ele in adjList[curr]:
                if not visited[ele]:
                    visited[ele] = True
                    q.put(ele)
        return ans

    def bfsOfGraph(self, V, adj):
        # code here
        visited = [False] * V
        return self.bfs(adj, visited, 0)


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
        ob = Solution()
        ans = ob.bfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()

# } Driver Code Ends