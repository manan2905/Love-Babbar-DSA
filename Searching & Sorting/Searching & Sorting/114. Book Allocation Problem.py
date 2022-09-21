class Solution:
    def isValid(self, arr, currMaxPages, s):
        student = 1
        sum = 0
        for ele in arr:
            sum += ele
            if sum > currMaxPages:
                sum = ele
                student += 1
        if student > s:
            return False
        return True

    def findPages(self, A, N, M):
        s = max(A)
        e = sum(A)
        res = -1
        if len(A) < M:
            return -1
        while s <= e:
            mid = (s + e) // 2
            if self.isValid(A, mid, M):
                res = mid
                e = mid - 1
            else:
                s = mid + 1
        return res


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        arr = [int(x) for x in input().strip().split()]
        m = int(input())

        ob = Solution()

        print(ob.findPages(arr, n, m))
# } Driver Code Ends