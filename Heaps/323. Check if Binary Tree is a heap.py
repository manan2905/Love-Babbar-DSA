# User Template for python3

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
import queue


class Solution:
    # Your Function Should return True/False
    def traversal(self, root):
        if root is None:
            return []
        q = queue.Queue()
        q.put(root)
        ans = []
        while not q.empty():
            curr = q.get()

            if curr == None:
                ans.append(-1)
                continue
            else:
                ans.append(curr.data)
                if curr.left:
                    q.put(curr.left)
                else:
                    q.put(None)
                if curr.right:
                    q.put(curr.right)
                else:
                    q.put(None)
        return ans

    def checkHeap(self, arr, i, n):
        pi = i
        c1, c2 = 2 * pi + 1, 2 * pi + 2
        while c1 <= n:
            if arr[c1] > arr[pi] or (c2 <= n and arr[c2] > arr[pi]):
                return False
            pi += 1
            c1, c2 = 2 * pi + 1, 2 * pi + 2
        return True

    def isHeap(self, root):
        # CBT check
        a = self.traversal(root)
        j = len(a) - 1
        while a[j] == -1:
            j -= 1

        for i in range(j + 1):
            if a[i] == -1:
                return False

        return self.checkHeap(a, 0, j)


# {
#  Driver Code Starts
# Initial Template for Python 3

# Contributed by Susanta Mukherjee
import sys

sys.setrecursionlimit(10 ** 6)
from collections import deque


# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        root = buildTree(input())
        ob = Solution()
        if ob.isHeap(root):
            print(1)
        else:
            print(0)

# } Driver Code Ends