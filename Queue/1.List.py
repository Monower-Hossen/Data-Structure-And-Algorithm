queue = []

queue.append('a')
queue.append('b')
queue.append('c')

print("Initial queue: ", queue)

print("\nElements dequeued from queue")
print(queue.pop())
print(queue.pop())
print(queue.pop())

print("\nQueue after removing elements")
print(queue)
