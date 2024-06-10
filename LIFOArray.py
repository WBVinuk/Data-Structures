class LIFOArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.top = -1

    def push(self, value):
        if self.top == self.capacity - 1:
            raise RuntimeError("Stack is full")
        self.top += 1
        self.array[self.top] = value

    def pop(self):
        if self.top == -1:
            raise RuntimeError("Stack is empty")
        value = self.array[self.top]
        self.array[self.top] = None
        self.top -= 1
        return value

# Example usage
if __name__ == "__main__":
    stack = LIFOArray(10)
    stack.push(4)
    stack.push(7)
    stack.push(10)

    while stack.top != -1:
        print(stack.pop())
