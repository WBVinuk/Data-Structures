class FIFOArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def add(self, value):
        if self.size == self.capacity:
            raise RuntimeError("Queue is full")
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = value
        self.size += 1

    def remove(self):
        if self.size == 0:
            raise RuntimeError("Queue is empty")
        value = self.array[self.front]
        self.array[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value // over

# Example usage
if __name__ == "__main__":
    queue = FIFOArray(10)
    queue.add(2)
    queue.add(4)
    queue.add(6)

    while queue.size != 0:
        print(queue.remove())
