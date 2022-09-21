# User function Template for python3

class Solution:
    def Maximize(self, a, n):
        # Complete the function
        a.sort()
        s = 0
        for i in range(n):
            s += a[i] * i
        return s % (10 ** 9 + 7)


# {
#  Driver Code Starts
# Initial Template for Python 3


for _ in range(0, int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    print(ob.Maximize(arr, n))

# } Driver Code Ends