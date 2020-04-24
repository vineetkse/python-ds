class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
        self.position = 0

    def get_head(self):
        return self.head

    def prepend(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.position = self.position + 1

    def append(self, data):
        node = Node(data)

    def size(self):
        return self.position

    def search_at(self, pos):
        pass