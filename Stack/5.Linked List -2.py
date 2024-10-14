class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"  # Could also raise an exception here
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"  # Could also raise an exception here
        return self.head.value

    def isEmpty(self):
        return self.size == 0

    def stackSize(self):
        return self.size


# Create and manipulate the stack
myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')

# Test the stack methods
print("Pop: ", myStack.pop())  # Should print 'C'
print("Peek: ", myStack.peek())  # Should print 'B'
print("isEmpty: ", myStack.isEmpty())  # Should print False
print("Size: ", myStack.stackSize())  # Should print 2
