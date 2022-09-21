# User function Template for python3

class Solution:
    def isValid(self, arr, maxLength, total_painter):
        s = 0
        painter = 1
        for ele in arr:
            s += ele
            if s > maxLength:
                s = ele
                painter += 1
        if total_painter < painter:
            return False
        return True

    def minTime(self, A, n, k):
        s = max(A)
        e = sum(A)
        res = -1
        while s <= e:
            # max length each painter will paint
            maxLength = (s + e) // 2
            if self.isValid(A, maxLength, k):
                res = maxLength
                e = maxLength - 1
            else:
                s = maxLength + 1
        return res


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        str = input().split()
        k = int(str[0])
        n = int(str[1])
        arr = input().split()
        for itr in range(n):
            arr[itr] = int(arr[itr])

        ob = Solution()
        print(ob.minTime(arr, n, k))
# } Driver Code Ends