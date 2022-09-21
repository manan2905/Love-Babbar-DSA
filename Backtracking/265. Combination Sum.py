# {
# Driver Code Starts
# Initial Template for Python 3

import atexit
import io
import sys


# } Driver Code Ends
# User function Template for python3

class Solution:
    def combinationalSum(self, arr, k):
        def backtrack(ind, sub, target):
            if target == 0:
                ans.append(sub.copy())
                return
            if target < 0 or ind == len(arr):
                return
            for i in range(ind, len(arr)):
                if i > ind and arr[i] == arr[i - 1]:
                    continue
                if target < arr[i]:
                    break
                sub.append(arr[i])
                backtrack(i, sub, target - arr[i])
                sub.pop()

        ans = []
        arr.sort()
        backtrack(0, [], k)
        return ans

        # code here


# {
# Driver Code Starts.


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        s = int(input())
        ob = Solution()
        result = ob.combinationalSum(a, s)
        if (not len(result)):
            print("Empty")
            continue
        for i in range(len(result)):
            print("(", end="")
            size = len(result[i])
            for j in range(size - 1):
                print(result[i][j], end=" ")
            if (size):
                print(result[i][size - 1], end=")")
            else:
                print(")", end="")
        print()

# } Driver Code Ends
