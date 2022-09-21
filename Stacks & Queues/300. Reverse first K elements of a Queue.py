# User function Template for python3
'''
Function Arguments :
        @param  : q ( given queue to be used), k(Integer )
        @return : list, just reverse the first k elements of queue and return new queue
'''


# Function to reverse first k elements of a queue.

def modifyQueue(q, k):
    s = []
    i = 0
    z = len(q)
    while k != 0:
        s.append(q[i])
        i += 1
        k -= 1
    while len(s) != 0:
        q.append(s.pop())

    while i < (z - k):
        q.append(q[i])
        i += 1
    return q[i:]


# {
#  Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

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
        n, k = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))

        queue = []  # our queue to be used
        for i in range(n):
            queue.append(a[i])  # enqueue elements of array in our queue

        print(*modifyQueue(queue, k))
# } Driver Code Ends