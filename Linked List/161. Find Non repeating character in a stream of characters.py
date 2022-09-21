# User function Template for python3
from collections import OrderedDict


class Solution:
    def FirstNonRepeating(self, A):
        # Code here
        d = OrderedDict()
        nr = A[0]
        ans = ""
        for char in A:
            d[char] = d.get(char, 0) + 1
            if d[nr] == 1:
                ans += nr
            else:
                flag = False
                for k in d:
                    if d[k] == 1:
                        nr = k
                        flag = True
                        break
                if not flag:
                    ans += "#"
                else:
                    ans += nr

        return ans


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        A = input()
        ob = Solution()
        ans = ob.FirstNonRepeating(A)
        print(ans)

# } Driver Code Ends
