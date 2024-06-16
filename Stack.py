class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        return temp.data

    def is_empty(self):
        return self.top is None

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

# Example Usage
stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop())      # Output: 20
print(stack.peek())     # Output: 10
print(stack.is_empty()) # Output: False
