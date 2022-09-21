# User function Template for python3

class Solution:
    def find_permutation(self, S):
        # Code here
        def func(ind, curr, d):
            if len(curr) == len(S):
                ans.append(curr)
                return
            for i in range(len(S)):
                if d[i] == False:
                    d[i] = True
                    func(i + 1, curr + S[i], d)
                    d[i] = False

        d = {}
        for i in range(len(S)):
            d[i] = False
        ans = []
        func(0, "", d)
        s = set(ans)
        res = sorted([char for char in s])
        return res


# {
# Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        S = input()
        ob = Solution()
        ans = ob.find_permutation(S)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends
