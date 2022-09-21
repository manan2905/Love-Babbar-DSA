# User function Template for python3


def maxSum(arr, n):
    # code here
    arr.sort()
    i = 0
    j = len(arr) - 1
    flag = True



# {
#  Driver Code Starts
# Initial Template for Python 3


t = int(input())
for _ in range(0, t):
    n = int(input())
    # x=list(map(int,input().split()))
    # n=x[0]
    # k=x[1]
    arr = list(map(int, input().split()))
    ans = maxSum(arr, n)
    print(ans)

# } Driver Code Ends