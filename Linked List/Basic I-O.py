# to input a linked list we will enter a string and then convert that into linked list
class node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert(head, pos, data):
    i = 0
    prev = None
    curr = head
    newnode = node(data)
    while i < pos:
        prev = curr
        curr = curr.next
        i += 1
    if prev is None:
        newnode.next = head
        return newnode
    prev.next = newnode
    newnode.next = curr
    return head


def insertRecursive(head, pos, data):
    if pos == 0:
        newnode = node(data)
        newnode.next = head
        return newnode
    if head is None:
        return
    nh = insertRecursive(head.next, pos - 1, data)
    head.next = nh
    return head





def delete(head, val):
    prev = None
    curr = head
    while curr is not None:
        if curr.data == val:
            if prev is not None:
                prev.next = curr.next
                curr = curr.next
            else:
                head = curr.next
                curr = curr.next
        else:
            prev = curr
            curr = curr.next
    return head


def deleteRecursive(head, val):
    if head is None:
        return
    sh = deleteRecursive(head.next, val)
    if head.data == val:
        return sh
    head.next = sh
    return head


def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next


head = takeInput()
head = deleteRecursive(head, 1)
printLL(head)
