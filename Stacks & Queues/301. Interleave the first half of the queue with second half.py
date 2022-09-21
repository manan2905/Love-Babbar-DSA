import queue

q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)

print(q.qsize())
# print(q.get())
q.queue.appendleft(10)
print(q.queue)

