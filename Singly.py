class SinglyLinkedList:
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
            self.tail = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete_node(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return

        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next:
            current.next = current.next.next
            if not current.next:
                self.tail = current

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example Usage
sll = SinglyLinkedList()
sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_beginning(5)
sll.traverse()  # Output: 5 -> 10 -> 20 -> None
sll.delete_node(10)
sll.traverse()  # Output: 5 -> 20 -> None
