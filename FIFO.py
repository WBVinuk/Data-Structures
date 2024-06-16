class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.data

    def is_empty(self):
        return self.front is None

    def peek(self):
        if self.front is None:
            return None
        return self.front.data

# Example Usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
print(queue.dequeue())  # Output: 10
print(queue.peek())     # Output: 20
print(queue.is_empty()) # Output: False
