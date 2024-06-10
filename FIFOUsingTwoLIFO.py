class FIFOUsingTwoLIFO:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def add(self, value):
        self.stack1.append(value)

    def remove(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise RuntimeError("Queue is empty")
        return self.stack2.pop()

# Example usage
if __name__ == "__main__":
    queue = FIFOUsingTwoLIFO()
    queue.add(3)
    queue.add(5)
    queue.add(7)

    while queue.stack1 or queue.stack2:
        print(queue.remove())
