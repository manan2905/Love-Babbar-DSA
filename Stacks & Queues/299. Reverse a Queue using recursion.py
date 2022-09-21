# User function Template for python
from sys import setrecursionlimit

setrecursionlimit(10 ** 6)


# Function to reverse the queue.
def rev(q):
    # add code here
    if q.qsize() == 0:
        return q
    d = q.get()
    nq = rev(q)
    nq.put(d)
    return nq


# {
#  Driver Code Starts
# Initial Template for Python 3

from queue import Queue

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        q = Queue(maxsize=n + 1)
        for j in a:
            q.put(j)
        q = rev(q)
        for i in range(0, n):
            print(q.get(), end=" ")
        print()
# } Driver Code Ends