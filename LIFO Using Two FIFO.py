from collections import deque

class LIFOUsingTwoFIFO:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, value):
        self.queue2.append(value)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        if not self.queue1:
            raise RuntimeError("Stack is empty")
        return self.queue1.popleft()

# Example usage
if __name__ == "__main__":
    stack = LIFOUsingTwoFIFO()
    stack.push(5)
    stack.push(8)
    stack.push(11)

    while stack.queue1:
        print(stack.pop())
