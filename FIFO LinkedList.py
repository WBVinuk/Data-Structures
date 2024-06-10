from collections import deque

class FIFOLinkedList:
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
    queue = FIFOLinkedList()
    
    # Add elements to queue
    queue.add(2)
    queue.add(4)
    queue.add(6)
    
    # Remove elements from queue
    while not queue.is_empty():
        print(queue.remove())
