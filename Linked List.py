class Node:
    def __init__(self, data):
        self.data = data [cite: 15]
        self.next = None [cite: 15]

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data): [cite: 19]
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self): [cite: 20]
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, data): [cite: 21]
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False