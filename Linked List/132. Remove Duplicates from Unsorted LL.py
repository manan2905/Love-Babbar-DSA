from collections import OrderedDict


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    # Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        d = OrderedDict()
        curr = head
        fh, ft = None, None
        while curr is not None:
            if curr.data not in d:
                d[curr.data] = 1
            curr = curr.next

        for k in d:
            newnode = Node(k)
            if fh is None:
                fh, ft = newnode, newnode
            else:
                ft.next = newnode
                ft = ft.next
        return fh
