class dllnode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class dequeue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, x):
        newnode = dllnode(x)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode

    def appendLeft(self, x):
        newnode = dllnode(x)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            self.head.prev = newnode
            newnode.next = self.head
            self.head = newnode

    def pop(self):
        d = self.tail.data
        self.tail = self.tail.prev
        self.tail.next = None
        return d

    def popLeft(self):
        d = self.head.data
        self.head = self.head.next
        self.head.prev = None
        return d


d = dequeue()
d.append(1)
d.append(2)
d.appendLeft(3)
