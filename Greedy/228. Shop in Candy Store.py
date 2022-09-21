# User function Template for python3

class Solution:

    def candyStore(self, candies, N, K):
        # code here
        candies.sort()

        def func(candies):
            i = 0
            j = N
            cost = 0
            c = K
            while i < j:
                cost += candies[i]
                i += 1
                while i < j and c != 0:
                    j -= 1
                    c -= 1
                c = K
            return cost

        return [func(candies), func(candies[::-1])]


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N, K = [int(x) for x in input().split()]
        candies = [int(x) for x in input().split()]

        solObj = Solution()

        print(*solObj.candyStore(candies, N, K))
# } Driver Code Ends