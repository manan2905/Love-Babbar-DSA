class Solution:
    def countSquares(self, N):
        # code here
        s = 1
        e = N
        ans = 0
        while s <= e:
            mid = (s + e) // 2
            a = mid ** 2
            if a == N:
                break
            elif a > N:
                e = mid - 1
            else:
                s = mid + 1
                ans = mid
        return ans


# {
#  Driver Code Starts
# Initial Template for Python 3
import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.countSquares(N))
# } Driver Code Ends