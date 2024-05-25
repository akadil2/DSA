class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
    
    def prepend(self,data):
        new_node=Node(data)
        new_node.next = self.head
        self.head=new_node

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def merge(self,list1,list2):
        current = list1
        while current.next:
            current = current.next
        current.next = list2
        return list1
    
    def print_ll(self):
        if self.head is None:
            print('empty')
        else:
            current = self.head
            while current is not None:
                print(current.data,'-->',end='')
                current = current.next

LL1 = linkedList()
ll2 = linkedList()
LL1.prepend(10)
LL1.prepend(15)
LL1.append(20)
ll2.append(5)
ll2.append(6)
ll2.append(7)
LL1.print_ll()
ll2.print_ll()

mrg_lst = linkedList()
mrg_lst.head = mrg_lst.merge(LL1.head,ll2.head)
mrg_lst.print_ll()
