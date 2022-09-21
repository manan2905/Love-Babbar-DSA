# User function Template for python3

'''
class Node:
    def __init__(self):
        self.data = None
        self.next = None
'''


class Solution:
    def length(self, head):
        c = 0
        curr = head
        while curr is not None:
            curr = curr.next
            c += 1
            if curr == head:
                break
        return c

    def splitList(self, head, head1, head2):
        # code here
        i = 1
        c = self.length(head)
        slow = head
        fast = head
        while i < c // 2:
            slow = slow.next
            i += 1
        head2 = slow.next
        slow.next = head
        head1 = head
        i = 1
        while i < c:
            fast = fast.next
            i += 1
        fast.next = head2

        # this is to emulate pass by reference in python please don't delete below line.
        return head1, head2


# {
#  Driver Code Starts
# Initial Template for Python 3


class Node:
    def __init__(self):
        self.data = None
        self.next = None


def printCircularLinkedList(head):
    tmp = head
    while True:
        print(tmp.data, end=" ")
        tmp = tmp.next
        if tmp == head:
            break
    print()


if __name__ == "__main__":
    for i in range(int(input())):
        head = Node()
        head1 = Node()
        head2 = Node()
        tmp = head
        n = int(input())
        for i in input().split():
            tmp.next = Node()
            tmp = tmp.next
            tmp.data = int(i)
        head = head.next
        tmp.next = head
        obj = Solution()
        head1, head2 = obj.splitList(head, head1, head2)
        printCircularLinkedList(head1)
        printCircularLinkedList(head2)

# } Driver Code Ends
