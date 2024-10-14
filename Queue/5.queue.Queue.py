from queue import Queue

q = Queue(maxsize = 3)

print(q.qsize())

q.put(1)
q.put(2)
q.put(3)

print("\nFull: ", q.full())
print("\nElements dequeued from the queue:")

print(q.get())
print(q.get())
print(q.get())

print("\nEmpty: ", q.empty())

q.put(1)

print("\nEmpty: ", q.empty())
print("\nFull: ", q.full())
