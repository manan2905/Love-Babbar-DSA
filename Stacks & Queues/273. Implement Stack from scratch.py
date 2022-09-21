# Stack Using Array
class stack:
    def __init__(self):
        self.s = []

    def push(self, data):
        self.s.append(data)

    def pop(self):
        if self.isEmpty():
            return "Stack Empty"
        return self.s.pop()

    def top(self):
        if self.isEmpty():
            return "Stack Empty"
        return self.s[-1]

    def isEmpty(self):
        return self.getsize() == 0

    def getsize(self):
        return len(self.s)


# Stack using Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class stackLL:
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.count += 1

    def top(self):
        return self.head.data

    def pop(self):
        if self.count != 0:
            data = self.head.data
            self.head = self.head.next
            self.count -= 1
            return data
        return -1

    def getSize(self):
        return self.count

    def isEmpty(self):
        return self.count == 0


s = stackLL()

s2 = stack()
