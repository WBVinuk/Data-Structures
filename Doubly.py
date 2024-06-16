class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete_node(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return

        current = self.head
        while current and current.data != data:
            current = current.next

        if current:
            if current.next:
                current.next.prev = current.prev
            if current.prev:
                current.prev.next = current.next
            if current == self.tail:
                self.tail = current.prev

    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" -> ")
            current = current.prev
        print("None")

# Example Usage
dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_beginning(5)
dll.traverse_forward()  # Output: 5 -> 10 -> 20 -> None
dll.traverse_backward()  # Output: 20 -> 10 -> 5 -> None
dll.delete_node(10)
dll.traverse_forward()  # Output: 5 -> 20 -> None
