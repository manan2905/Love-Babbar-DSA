# User function Template for python3

class Solution:

    # Function to find the maximum number of meetings that can
    # be performed in a meeting room.
    def maximumMeetings(self, n, start, end):
        # code here
        arr = []
        for i in range(n):
            arr.append([start[i], end[i]])
        arr.sort(key=lambda x: x[1])
        c = 1
        cur = -1
        for i in range(len(arr)):
            if cur == -1:
                cur = arr[i]
            else:
                if arr[i][0] > cur[-1]:
                    cur = arr[i]
                    c += 1
        return c


# {
# Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        start = list(map(int, input().strip().split()))
        end = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maximumMeetings(n, start, end))
# } Driver Code Ends