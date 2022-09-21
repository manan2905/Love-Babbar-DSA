# User function Template for python3
'''
    Your task is to check if given linkedlist
    is a pallindrome or not.

    Function Arguments: head (reference to head of the linked list)
    Return Type: boolean , no need to print just return True or False.

    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }

    Contributed By: Nagendra Jha
'''
from sys import setrecursionlimit

setrecursionlimit(10 ** 6)


# Function to check whether the list is palindrome.
class Solution:
    def reverse(self, head):
        if head is None or head.next is None:
            return head, head
        sh, st = self.reverse(head.next)
        st.next = head
        st = st.next
        st.next = None
        return sh, st

    def length(self, head):
        c = 0
        while head is not None:
            c += 1
            head = head.next
        return c

    def isPalindrome(self, head):
        # code here
        if head is None or head.next is None:
            return 1
        c = self.length(head)
        prev = None
        curr = head
        i = 0
        while i < (c + 1) // 2:
            prev = curr
            curr = curr.next
            i += 1
        prev.next = None
        sh, st = self.reverse(curr)
        while head is not None and sh is not None:
            if head.data != sh.data:
                return 0
            head = head.next
            sh = sh.next
        return 1


# {
#  Driver Code Starts
# Initial Template for Python 3
# Contributed by : Nagendra Jha

import atexit
import io
import sys


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


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList()  # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list

        if Solution().isPalindrome(a.head):
            print(1)
        else:
            print(0)
# } Driver Code Ends
