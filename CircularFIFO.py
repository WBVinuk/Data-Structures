class CircularFIFOQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = item
            self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            item = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            return self.queue[self.front]

    def get_size(self):
        return self.size

# Example usage
if __name__ == "__main__":
    queue = CircularFIFOQueue(3)

    queue.enqueue(6)
    queue.enqueue(4)
    queue.enqueue(2)

    print("Dequeued:", queue.dequeue())  # Output: 6
    print("Peek:", queue.peek())  # Output: 4
    queue.enqueue(8)

    print("Dequeued:", queue.dequeue())  # Output: 4
    print("Dequeued:", queue.dequeue())  # Output: 2
    print("Dequeued:", queue.dequeue())  # Output: 8

    print("Is empty:", queue.is_empty())  # Output: True
