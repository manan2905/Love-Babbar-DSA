# User function Template for python3

# Function that constructs BST from its preorder traversal.
def post_order(pre, size):
    if size == 0:
        return
    root = Node(pre[0])
    ind = -1
    for i in range(1, size):
        if pre[0] < pre[i]:
            ind = i
            break
    if ind > 0:
        lpre, rpre = pre[1:ind], pre[ind:]
    else:
        lpre, rpre = pre[1:], []

    root.left = post_order(lpre, len(lpre))
    root.right = post_order(rpre, len(rpre))
    return root


# code here


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None


def postOrd(root):
    if not root:
        return
    postOrd(root.left)
    postOrd(root.right)
    print(root.data, end=' ')


if __name__ == '__main__':
    t = int(input())

    for _tcs in range(t):
        size = int(input())
        pre = [int(x) for x in input().split()]

        root = post_order(pre, size)

        postOrd(root)
        print()
# } Driver Code Ends
