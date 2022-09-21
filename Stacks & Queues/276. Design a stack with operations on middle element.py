# class DLLNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None
#
#
# class stack:
#     def __init__(self):
#         self.head = None
#         self.mid = None
#         self.count = 0
#
#     def push(self, data):
#         newnode = DLLNode(data)
#         newnode.next = self.head
#         if self.head is not None:
#             self.head.prev = newnode
#         self.head = newnode
#         self.count += 1
#         if self.count == 1:
#             self.mid = self.head
#         if self.count % 2 == 0:
#             self.mid = self.mid.prev
#
#     def pop(self):
#         if self.count == 0:
#             return -1
#         self.head = self.head.next
#         self.head.prev = None
#         self.mid = self.mid.next
#         self.count -= 1
#
#     def deleteMiddle(self):
#         d = self.mid.data
#         temp = self.mid.next
#         self.mid.next = self.mid.prev
#         self.mid.prev = temp
#         self.count -= 1
#         return d
#
#     def middle(self):
#         return self.mid.data
#
#
# s = stack()
# s.push(1)
# s.push(2)
# s.push(3)
#
# print(s.count)
# print(s.deleteMiddle())
# print(s.count)
# print(s.middle())
# print(s.deleteMiddle())
# print(s.middle())

class DLLnode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Stack:
    def __init__(self):
        self.count = 0
        self.head = None
        self.middle = None

    def push(self, data):
        node = DLLnode(data)
        if self.head is None:
            self.head = node
            self.middle = node
            self.count += 1
        else:
            node.prev = self.head
            self.head.next = node
            self.head = self.head.next
            self.count += 1
            if self.count % 2 == 0:
                self.middle = self.middle.next

    def pop(self):
        if self.count == 0:
            return -1
        elif self.count % 2 == 0:
            self.middle = self.middle.prev
        data = self.head.data
        self.head = self.head.prev
        self.count -= 1
        return data

    def findMiddle(self):
        if self.count != 0:
            return self.middle.data
        return -1

    def deleteMiddle(self):
        if self.count == 0:
            return -1
        elif self.count <= 2 and self.middle == self.head:
            self.count -= 1
            d = self.middle.data
            self.middle = self.middle.prev
            self.head = self.middle
            return d
        else:
            d = self.middle.data
            if self.count % 2 == 0:
                curr = self.middle.prev
            else:
                curr = self.middle.next
            self.middle.next.prev = self.middle.prev
            self.middle.prev.next = self.middle.next
            self.middle = curr
            self.count -= 1

            return d


s = Stack()
s.push(1)
s.push(2)
s.push(3)
