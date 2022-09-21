# User function Template for python3

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''


class Solution:
    def reverseLL(self, head):
        if head is None or head.next is None:
            return head, head
        sh, st = self.reverseLL(head.next)
        st.next = head
        st = st.next
        st.next = None
        return sh, st

    # Idea is to reverse the linked list and then add 2 to the starting element and use the carry method
    def addOne(self, head):
        # Returns new head of linked List.
        sh, st = self.reverseLL(head)
        curr = sh
        carry = 1
        while curr is not None:
            if carry != 0:
                curr.data += carry
                carry = curr.data // 10
                curr.data %= 10
                if curr.next is None and carry != 0:
                    curr.next = Node(carry)
                    break
                curr = curr.next
            else:
                break
        fh, ft = self.reverseLL(sh)
        return fh

    # def helper(self, head):
    #     if head is None:
    #         # return Node, carry
    #         return head, 1
    #     sh, carry = self.helper(head.next)
    #     head.next = sh
    #     if carry != 0:
    #         head.data += carry
    #         carry = head.data // 10
    #         head.data %= 10
    #         if carry != 0:
    #             newnode = Node(carry)
    #             newnode.next = head
    #             return newnode, carry
    #
    #     return head, carry
    #
    # def addOne2(self, head):
    #     return self.helper(head)[0]


# {
#  Driver Code Starts
# Initial Template for Python 3

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
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next


def PrintList(head):
    while head:
        print(head.data, end='')
        head = head.next


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        num = input()
        ll = LinkedList()  # create a new linked list 'll1'.
        for digit in num:
            ll.insert(int(digit))  # add to the end of the list

        resHead = Solution().addOne(ll.head)
        PrintList(resHead)
        print()

# } Driver Code Ends
