class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class Doubly:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def prepend(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def print_fw(self):
        if not self.head:
            print('empty')
            return
        Current = self.head
        while Current:
            print(Current.data)
            Current = Current.next
    def print_bw(self):
        current = self.tail
        while current:
            print(current.data,'-->', end='')
            current = current.prev



