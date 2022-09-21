# User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


# Function to delete a given node from the list
def deleteNode(head, key):
    # your code goes here
    prev = None
    curr = head
    while curr.next != head:
        if curr.data == key:
            prev.next = curr.next
            break
        prev = curr
        curr = curr.next
    return head


# Function to reverse the list
def reverse(head_ref):
    # your code goes here
    if (head_ref == None):
        return None

    # reverse procedure same as
    # reversing a singly linked list
    prev = None
    current = head_ref

    next = current.next
    current.next = prev
    prev = current
    current = next
    while (current != head_ref):
        next = current.next
        current.next = prev
        prev = current
        current = next

    # adjutsing the links so as to make the
    # last node po to the first node
    head_ref.next = prev
    head_ref = prev
    return head_ref


# {
#  Driver Code Starts
# Initial Template for Python 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def push(data, prev):
    if prev == None:
        prev = Node(data)
        return prev
    tmp = Node(data)
    prev.next = tmp
    return tmp


def printList(head):
    flg = False
    tmp = head
    while flg == False or tmp != head:
        flg = True
        print(tmp.data, end=" ")
        tmp = tmp.next
    print()


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(i) for i in input().split()]
        delNode = int(input())

        head = Node(None)
        prev = head
        for i in arr:
            prev = push(i, prev)
        head = head.next
        prev.next = head
        deleteNode(head, delNode)
        reverse(head)
        printList(head)

# } Driver Code Ends
