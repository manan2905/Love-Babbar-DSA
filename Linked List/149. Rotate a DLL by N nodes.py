# User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
'''


def length(head):
    c = 0
    while head:
        c += 1
        head = head.next
    return c


def rotateByN(head, n):
    l = length(head)
    if head is None or n <= 0 or head.next is None or n == l:
        return head

    n = n % l
    curr = head
    while n != 0:
        curr = curr.next
        n -= 1
    # 1, 2, 3, 4, 5
    tail = curr.prev
    curr.prev = None
    nh = curr
    while curr.next:
        curr = curr.next
    curr.next = head
    head.prev = curr
    tail.next = None
    return nh


# {
#  Driver Code Starts
# Initial Template for Python 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data, tail):
        if not self.head:
            self.head = Node(new_data)
            return self.head
        Nnode = Node(new_data)
        Nnode.prev = tail
        tail.next = Nnode
        return Nnode

    def printList(self, node):
        while (node is not None):
            print(node.data, end=' ')
            node = node.next


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]

        dll = DoublyLinkedList()
        tail = None

        for e in arr:
            tail = dll.push(e, tail)

        reshead = rotateByN(dll.head, 5)
        dll.printList(reshead)
        print()

# } Driver Code Ends
