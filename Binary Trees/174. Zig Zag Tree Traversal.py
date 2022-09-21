# User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
import queue


class Solution:
    # Function to store the zig zag order traversal of tree in a list.
    def zigZagTraversal(self, root):
        if root is None:
            return
        ans = []
        level = []
        q1 = queue.Queue()
        q2 = queue.Queue()
        flag = True
        q1.put(root)
        while not q1.empty():
            while not q1.empty():
                curr = q1.get()
                level.append(curr.data)
                if curr.left:
                    q2.put(curr.left)
                if curr.right:
                    q2.put(curr.right)
            if flag:
                ans.extend(level.copy())
                flag = False
            else:
                ans.extend(level.copy()[::-1])
                flag = True
            level.clear()
            q1, q2 = q2, q1
        return ans


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB

from collections import defaultdict
from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


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


if __name__ == '__main__':
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        ob = Solution()
        res = ob.zigZagTraversal(root)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
# } Driver Code Ends