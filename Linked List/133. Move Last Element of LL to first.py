class node:
    def __init__(self, data):
        self.data = data
        self.next = None


def moveLasttoFirst(head):
    if head is None or head.next is None:
        return head
    prev = None
    curr = head
    while curr.next is not None:
        prev = curr
        curr = curr.next
    prev.next = None
    curr.next = head
    return curr


def takeInput():
    s = [int(ele) for ele in input().split()]
    head, tail = None, None
    for ele in s:
        newnode = node(ele)
        if head is None:
            head = newnode
            tail = newnode
        else:
            tail.next = newnode
            tail = tail.next
    return head


def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next


head = takeInput()
h1 = moveLasttoFirst(head)
printLL(h1)
