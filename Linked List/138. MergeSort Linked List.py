# User function Template for python3

'''
    :param head: head of unsorted linked list
    :return: head of sorted linkd list

    # Node Class
    class Node:
        def __init__(self, data):  # data -> value stored in node
            self.data = data
            self.next = None
'''


class Solution:
    # Function to sort the given linked list using Merge Sort.
    def mergeLL(self, head1, head2):
        fh, ft = None, None
        while head1 is not None and head2 is not None:
            if head1.data < head2.data:
                newnode = Node(head1.data)
                if fh is None:
                    fh, ft = newnode, newnode
                else:
                    ft.next = newnode
                    ft = ft.next
                head1 = head1.next
            else:
                newnode = Node(head2.data)
                if fh is None:
                    fh, ft = newnode, newnode
                else:
                    ft.next = newnode
                    ft = ft.next
                head2 = head2.next

        if head1 is not None:
            ft.next = head1
        else:
            ft.next = head2
        return fh

    def length(self, head):
        c = 0
        while head is not None:
            c += 1
            head = head.next
        return c

    def mergeSort(self, head):
        if head is None or head.next is None:
            return head
        l = self.length(head)
        mid = l // 2
        i = 0
        prev = None
        curr = head
        while i < mid:
            prev = curr
            curr = curr.next
            i += 1
        prev.next = None
        sl1, sl2 = self.mergeSort(head), self.mergeSort(curr)
        ans = self.mergeLL(sl1, sl2)
        return ans


# {
#  Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys


# Contributed by : Nagendra Jha

# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node


# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end=" ")
        curr_node = curr_node.next
    print(' ')


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n = int(input())
        p = LinkedList()  # create a new linked list 'a'.
        nodes_p = list(map(int, input().strip().split()))
        for x in nodes_p:
            p.append(x)  # add to the end of the list

        printList(Solution().mergeSort(p.head))

# } Driver Code Ends
