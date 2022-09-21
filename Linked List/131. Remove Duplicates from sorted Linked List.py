from sys import setrecursionlimit

setrecursionlimit(10 ** 6)

# you do not need to return anything but make changes withing the list
# Function to remove duplicates from sorted linked list.
def removeDuplicates(head):
    # code here
    if head is None:
        return
    prev = head
    curr = head.next
    while curr is not None:
        if prev.data == curr.data:
            curr = curr.next
        else:
            prev.next = curr
            prev = curr
            curr = curr.next
    if prev.next is not None:
        prev.next = None