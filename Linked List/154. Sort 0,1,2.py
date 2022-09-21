# User function Template for python3
'''
    Your task is to segregate the list of
    0s,1s and 2s.

    Function Arguments: head of the original list.
    Return Type: head of the new list formed.

    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }

'''


class Solution:
    # Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        # code here
        h0, t0 = None, None
        h1, t1 = None, None
        h2, t2 = None, None
        while head:
            if head.data == 0:
                if h0 is None:
                    h0, t0 = head, head
                else:
                    t0.next = head
                    t0 = t0.next
            elif head.data == 1:
                if h1 is None:
                    h1, t1 = head, head
                else:
                    t1.next = head
                    t1 = t1.next
            else:
                if h2 is None:
                    h2, t2 = head, head
                else:
                    t2.next = head
                    t2 = t2.next
            head = head.next
        if h0 is None and h1 is None:
            return h2
        elif h1 is None and h2 is None:
            return h0
        elif h0 is None and h2 is None:
            return h1

        elif h0 is None:
            t1.next = h2
            t2.next = None
            return h1
        elif h1 is None:
            t0.next = h2
            t2.next = None
            return h0
        elif h2 is None:
            t0.next = h1
            t1.next = None
            return h0
        else:
            t0.next = h1
            t1.next = h2
            t2.next = None
            return h0


# {
#  Driver Code Starts
# Initial Template for Python 3
# Contributed by : Nagendra Jha

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


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
        a = LinkedList()  # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list
        printList(Solution().segregate(a.head))
# } Driver Code Ends