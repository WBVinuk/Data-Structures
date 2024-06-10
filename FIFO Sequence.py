from collections import deque

class FIFOSequence:
    def __init__(self):
        self.queue = deque()

    def add(self, value):
        self.queue.append(value)

    def remove(self):
        if self.is_empty():
            raise RuntimeError("Queue is empty")
        return self.queue.popleft()

    def is_empty(self):
        return len(self.queue) == 0

# Example usage
if __name__ == "__main__":
    queue = FIFOSequence()
    
    # Add elements to queue
    queue.add(3)
    queue.add(5)
    queue.add(7)
    
    # Remove elements from queue
    while not queue.is_empty():
        print(queue.remove())
