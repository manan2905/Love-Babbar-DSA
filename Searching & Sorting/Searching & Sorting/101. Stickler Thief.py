# User function Template for python3

class Solution:

    # Function to find the maximum money the thief can get.
    def FindMaxSum(self, a, n):
        def func(ind):
            # base case
            if ind == 0:
                return a[0]
            if ind < 0:
                return 0
            if dp[ind] != -1:
                return dp[ind]
            l = func(ind - 2) + a[ind]
            r = func(ind - 1)
            dp[ind] = max(l, r)
            return dp[ind]

        dp = [-1 for i in range(n)]
        return func(n - 1)


# {
#  Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

sys.setrecursionlimit(10 ** 6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.FindMaxSum(a, n))
# } Driver Code Ends
