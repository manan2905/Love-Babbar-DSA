# User function Template for python3

class Solution:
    # Heapify function to maintain heap property.
    def heapify(self, arr, n, i):
        # code here
        pi = i
        c1, c2 = 2 * pi + 1, 2 * pi + 2
        while c1 < n:
            min = pi
            if arr[min] < arr[c1]:
                min = c1
            if c2 < n and arr[min] < arr[c2]:
                min = c2
            if min == pi:
                break
            arr[min], arr[pi] = arr[pi], arr[min]
            pi = min
            c1, c2 = 2 * pi + 1, 2 * pi + 2

    # Function to build a Heap from array.
    def buildHeap(self, arr, n):
        # code here
        for i in range(len(arr) - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)

    # Function to sort an array using Heap Sort.
    def HeapSort(self, arr, n):
        # optimizing heap sort
        for i in range(len(arr) // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        self.buildHeap(arr, n)


# {
#  Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr, n)
        print(*arr)

# } Driver Code Ends
