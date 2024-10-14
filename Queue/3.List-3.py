# Initialize an empty queue
queue = []

# Enqueue (Add elements to the end of the queue)
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue after enqueuing: ", queue)

# Dequeue (Remove the first element from the queue)
if queue:  # Ensure the queue is not empty before trying to dequeue
    element = queue.pop(0)
    print("Dequeued element: ", element)
else:
    print("Queue is empty, cannot dequeue")

# Peek (View the front element without removing it)
if queue:  # Ensure the queue is not empty before trying to peek
    frontElement = queue[0]
    print("Front element (Peek): ", frontElement)
else:
    print("Queue is empty, cannot peek")

# isEmpty (Check if the queue is empty)
isEmpty = not bool(queue)
print("Is the queue empty? ", isEmpty)

# Size (Get the size of the queue)
print("Queue size: ", len(queue))
