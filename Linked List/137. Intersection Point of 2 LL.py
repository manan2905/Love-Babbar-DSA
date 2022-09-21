# User function Template for python3
'''
    Function to return the value at point of intersection
    in two linked list, connected in y shaped form.

    Function Arguments: head_a, head_b (heads of both the lists)

    Return Type: value in NODE present at the point of intersection
                 or -1 if no common point.

    Contributed By: Nagendra Jha

    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }
'''


# Function to find intersection point in Y shaped Linked Lists.
def reverseLL(head):
    if head is None or head.next is None:
        return head, head
    sh, st = reverseLL(head.next)
    st.next = head
    st = st.next
    st.next = None
    return sh, st


# Function to find intersection point in Y shaped Linked Lists.
def intersetPoint(head1, head2):
    # using hashset
    s = set()
    while head1 is not None:
        s.add(head1)
        head1 = head1.next
    while head2 is not None:
        if head2 in s:
            return head2.data
        head2 = head2.next


def length(head):
    c = 0
    while head:
        c += 1
        head = head.next
    return c


def intersectPoint2(head1, head2):
    l1, l2 = length(head1), length(head2)
    if l2 > l1:
        c = l2 - l1
        while c != 0:
            head2 = head2.next
            c -= 1
    else:
        c = l1 - l2
        while c != 0:
            head1 = head1.next
            c -= 1
    while head1 != head2:
        head1 = head1.next
        head2 = head2.next
    if head1 is not None:
        return head1.data
    return -1


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


class LinkedList:
    def __init__(self):
        self.head = None
        temp = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.temp = self.head
            return
        else:
            self.temp.next = new_node
            self.temp = self.temp.next


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        x, y, z = map(int, input().strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        b = LinkedList()  # create a new linked list 'b'.
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        nodes_common = list(map(int, input().strip().split()))

        for x in nodes_a:
            node = Node(x)
            a.append(node)  # add to the end of the list

        for x in nodes_b:
            node = Node(x)
            b.append(node)  # add to the end of the list

        for i in range(len(nodes_common)):
            node = Node(nodes_common[i])
            a.append(node)  # add to the end of the list a
            if i == 0:
                b.append(node)  # add to the end of the list b, only the intersection

        print(intersetPoint(a.head, b.head))

# } Driver Code Ends
