# User function Template for python3
from sys import setrecursionlimit

setrecursionlimit(10 ** 6)


class Solution:
    # Your task is to complete this function
    # function should return True/False or 1/0
    def check(self, root):
        # Code here
        def leftLevel(root):
            curr_lvl = 0
            a_lvl = -1
            while root:
                if root.left is None and root.right is None:
                    a_lvl = curr_lvl
                    break
                if root.left:
                    root = root.left
                else:
                    root = root.right
                curr_lvl += 1
            return a_lvl

        def func(root, lvl):
            if root is None:
                return True
            if root.left is None and root.right is None:
                if lvl == a_lvl:
                    return True
                return False
            lb, rb = func(root.left, lvl + 1), func(root.right, lvl + 1)
            if lb and rb:
                return True
            return False

        a_lvl = leftLevel(root)
        return func(root, 0)


# {
#  Driver Code Starts
# Initial Template for Python 3

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
        s = input()
        root = buildTree(s)
        if Solution().check(root):
            print(1)
        else:
            print(0)

# } Driver Code Ends