# User function Template for python3
'''
    Your task is to merge the given k sorted
    linked lists into one list and return
    the the new formed linked list class.

    Function Arguments:
        arr is a list containing the n linkedlist head pointers
        n is an integer value

    node class:

class Node:
    def __init__(self,x):
        self.data = x
        self.nxt = None
'''


class Solution:
    # Function to merge K sorted linked list.
    def mergeK(self, h1, h2):
        nh, nt = None, None
        while h1 and h2:
            if h1.data < h2.data:
                if nh is None:
                    nh, nt = h1, h1
                else:
                    nt.next = h1
                    nt = nt.next
                h1 = h1.next
            else:
                if nh is None:
                    nh, nt = h2, h2
                else:
                    nt.next = h2
                    nt = nt.next
                h2 = h2.next
        if h1:
            nt.next = h1
        if h2:
            nt.next = h2
        return nh

    def mergeKLists(self, arr, K):
        # code here
        # return head of merged list
        if len(arr) == 1:
            return arr[0]
        nh = self.mergeK(arr[0], arr[1])
        for i in range(2, len(arr)):
            nh = self.mergeK(nh, arr[i])
        return nh


# {
#  Driver Code Starts
# Initial Template for Python 3

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, x):
        if self.head is None:
            self.head = Node(x)
            self.tail = self.head
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next


def printList(head):
    walk = head
    while walk:
        print(walk.data, end=' ')
        walk = walk.next
    print()


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        line = [int(x) for x in input().strip().split()]

        heads = []
        index = 0

        for i in range(n):
            size = line[index]
            index += 1

            newList = LinkedList()

            for _ in range(size):
                newList.add(line[index])
                index += 1

            heads.append(newList.head)

        merged_list = Solution().mergeKLists(heads, n)
        printList(merged_list)

# } Driver Code Ends