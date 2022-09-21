class node:
    def __init__(self, data):
        self.data = data
        self.next = None


# recursive
def reverseLL(head):
    if head is None or head.next is None:
        return head, head
    sh, st = reverseLL(head.next)
    st.next = head
    st = st.next
    st.next = None
    return sh, st


# iterative
def reverseLLIterative(head):
    curr = head
    prev = None
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


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
h1 = reverseLL(head)
# h2 = reverseLLIterative(head)
printLL(h1[0])
print()
# printLL(h2)
