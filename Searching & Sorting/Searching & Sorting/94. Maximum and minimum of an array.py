class Solution:
    def middle(self, A, B, C):
        # code here
        if A > B > C or A < B < C:
            return B
        elif B > A > C or B < A < C:
            return A
        else:
            return C


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A, B, C = map(int, input().strip().split())
        ob = Solution()
        print(ob.middle(A, B, C))
# } Driver Code Ends