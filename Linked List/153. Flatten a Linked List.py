# User function Template for python3


'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None

'''


def mergeLL(h1, h2):
    nh, nt = None, None
    while h1 and h2:
        if h1.data < h2.data:
            if nh is None:
                nh, nt = h1, h1
            else:
                nt.bottom = h1
                nt = nt.bottom
            h1 = h1.bottom
        else:
            if nh is None:
                nh, nt = h2, h2
            else:
                nt.bottom = h2
                nt = nt.bottom
            h2 = h2.bottom
    if h1:
        nt.bottom = h1
    if h2:
        nt.bottom = h2
    return nh


def flatten(root):
    # Your code here
    if root is None or root.next is None:
        return root
    nh = mergeLL(root, root.next)
    root = root.next.next
    while root:
        nh = mergeLL(root, nh)
        root = root.next
    return nh


# {
#  Driver Code Starts
# Initial Template for Python 3

class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None


def printList(node):
    while (node is not None):
        print(node.data, end=" ")
        node = node.bottom

    print()


if __name__ == "__main__":
    t = int(input())
    while (t > 0):
        head = None
        N = int(input())
        arr = []

        arr = [int(x) for x in input().strip().split()]
        temp = None
        tempB = None
        pre = None
        preB = None

        flag = 1
        flag1 = 1
        listo = [int(x) for x in input().strip().split()]
        it = 0
        for i in range(N):
            m = arr[i]
            m -= 1
            a1 = listo[it]
            it += 1
            temp = Node(a1)
            if flag is 1:
                head = temp
                pre = temp
                flag = 0
                flag1 = 1
            else:
                pre.next = temp
                pre = temp
                flag1 = 1

            for j in range(m):
                a = listo[it]
                it += 1
                tempB = Node(a)
                if flag1 is 1:
                    temp.bottom = tempB
                    preB = tempB
                    flag1 = 0
                else:
                    preB.bottom = tempB
                    preB = tempB
        root = flatten(head)
        printList(root)

        t -= 1

# } Driver Code Ends
