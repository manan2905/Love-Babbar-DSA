# User function Template for python3

'''
# Node class

class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''


class Solution:
    def buildtree(self, inorder, preorder, n):
        # code here
        # build tree and return root node
        if len(inorder) == 0:
            return
        root = Node(preorder[0])
        # finding index of the root in inorder
        ind = -1
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                ind = i
                break
        li, ri = inorder[:i], inorder[i + 1:]
        l = len(li)
        lp, rp = preorder[1:len(li) + 1], preorder[len(li) + 1:]

        root.left, root.right = self.buildtree(li, lp, n), self.buildtree(ri, rp, n)
        return root


# {
#  Driver Code Starts
# Initial Template for Python 3

class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


def printPostorder(n):
    if n is None:
        return
    printPostorder(n.left)
    printPostorder(n.right)
    print(n.data, end=' ')


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        inorder = [int(x) for x in input().split()]
        preorder = [int(x) for x in input().split()]

        root = Solution().buildtree(inorder, preorder, n)
        printPostorder(root)
        print()

# } Driver Code Ends