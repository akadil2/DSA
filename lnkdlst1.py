class Node:
    def __init__(self,data):
        self.data=data
        self.ref= None
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n=self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    def prepend(self,data):
        new_node = Node(data)
        new_node.ref=self.head
        self.head = new_node

    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print('no node')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def add_before(self,data,x):
        if self.head is None:
            print('no ll')
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print('no node')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def print_ll(self):
        if self.head is None:
            print('emptylist')
        else:
            n=self.head
            while n is not None:
                print(n.data, '-->',end=' ')
                n=n.ref
    
    def del_byvalue(self,x):
        if self.head is None:
            print('empty list')
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        n= self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n=n.ref
        if n.ref is None:
            print('nonode')
        else:
            n.ref = n.ref.ref
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next 
            current.next = prev       
            prev = current           
            current = next_node       
        self.head = prev 

    def mid(self):
        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def delete_duplicates(self):
        current = self.head
        while current:
            runner = current
            while runner.next:
                if runner.next.data == current.data:
                    runner.next = runner.next.next 
                else:
                    runner = runner.next
            current = current.next

LL = Linkedlist()
LL.prepend(10)
LL.prepend(20)
LL.prepend(30)
LL.add_after(25,20)
LL.print_ll()

