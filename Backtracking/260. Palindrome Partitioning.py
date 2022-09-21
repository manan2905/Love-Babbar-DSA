# User function Template for python3

class Solution:
    def isPal(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def backtrack(self, ind, s, ans, path):
        if ind == len(s):
            ans.append(path.copy())
            return
        for i in range(ind, len(s)):
            if self.isPal(s[ind:i + 1]):
                path.append(s[ind:i + 1])
                self.backtrack(i + 1, s, ans, path)
                path.pop()

    def allPalindromicPerms(self, S):
        # code here
        ans = []
        self.backtrack(0, S, ans, [])
        return ans


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        allPart = ob.allPalindromicPerms(S)
        for i in range(len(allPart)):
            for j in range(len(allPart[i])):
                print(allPart[i][j], end=" ")
            print()
            # } Driver Code Ends