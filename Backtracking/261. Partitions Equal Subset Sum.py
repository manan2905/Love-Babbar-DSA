# User function Template for Python3

class Solution:
    def backtrack(self, arr, ind, s):
        if s == 0:
            return True
        if s < 0 or ind == len(arr):
            return False
        return self.backtrack(arr, ind + 1, s - arr[ind]) or self.backtrack(arr, ind + 1, s)

    def equalPartition(self, N, arr):
        # code here
        if sum(arr) % 2 != 0:
            return 0
        s = sum(arr) // 2
        return self.backtrack(arr, 0, s)


# {
# Driver Code Starts
# Initial Template for Python3

import sys

input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])

        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends