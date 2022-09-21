# User function Template for python3

class Solution:
    def findMaxLen(self, string):
        # code here
        s = [-1]
        maxLen = 0
        for i in range(len(string)):
            char = string[i]
            if char == "(":
                s.append(i)
            elif char == ")":
                s.pop()
                if len(s) != 0:
                    maxLen = max(maxLen, i - s[-1])
                else:
                    s.append(i)
        return maxLen


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.findMaxLen(S))
# } Driver Code Ends