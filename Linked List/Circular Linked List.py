class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def takeInput():
    li = [int(i) for i in input().split()]
    fh, ft = None, None
    for i in range(len(li)):
        newnode = Node(li[i])
        if fh is None:
            fh, ft = newnode, newnode
        else:
            ft.next = newnode
            ft = ft.next
        if i == len(li) - 1:
            # last node
            ft.next = fh
    return fh


def delete(head, data):
    # setting the tail node first
    # so that we are able to delete the first node if required
    tail = head
    while True:
        tail = tail.next
        if tail.next == head:
            break
    curr = head
    while True:
        if curr == tail:
            if curr.next == tail and curr.data == data:
                return None
        if curr.data == data:
            tail.next = curr.next
            curr = curr.next
            head = curr
        else:
            curr = curr.next
    return head


def count(head):
    c = 0
    curr = head
    while True:
        c += 1
        curr = curr.next
        if head == curr:
            break
    return c


def printLL(head):
    curr = head
    if head is None:
        return
    while True:
        print(curr.data, end=" ")
        curr = curr.next
        if curr == head:
            break


head = takeInput()
printLL(head)
print()
printLL(delete(head, 5))
