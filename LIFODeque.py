from collections import deque

class LIFODeque:
    def __init__(self):
        self.deque = deque()

    def push(self, value):
        self.deque.appendleft(value)

    def pop(self):
        if not self.deque:
            raise RuntimeError("Deque is empty")
        return self.deque.popleft()

    def is_empty(self):
        return not self.deque

# Example usage
if __name__ == "__main__":
    stack = LIFODeque()
    
    # Push elements to deque
    stack.push(5)
    stack.push(8)
    stack.push(11)
    
    # Pop elements from deque
    while not stack.is_empty():
        print(stack.pop())
