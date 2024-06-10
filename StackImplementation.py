class StackImplementation:
    def __init__(self):
        self.lifo_queue = []

    def push(self, value):
        self.lifo_queue.append(value)

    def pop(self):
        if not self.lifo_queue:
            raise RuntimeError("Stack is empty")
        return self.lifo_queue.pop()

    def peek(self):
        if not self.lifo_queue:
            raise RuntimeError("Stack is empty")
        return self.lifo_queue[-1]

    def is_empty(self):
        return len(self.lifo_queue) == 0

# Example usage
if __name__ == "__main__":
    stack = StackImplementation()

    # Push elements to the stack
    stack.push(4)
    stack.push(7)
    stack.push(10)

    # Pop element
    print("Popped:", stack.pop())

    # Peek element
    print("Peek:", stack.peek())

    # Pop another element
    print("Popped:", stack.pop())

    # Check if the stack is empty
    print("Is empty:", stack.is_empty())

    # Pop last element
    print("Popped:", stack.pop())

    # Check if the stack is empty again
    print("Is empty:", stack.is_empty())
