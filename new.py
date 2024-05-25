class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class lList:
    def __init__(self):
        self.head = None
      
    def prep(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def merge(self,lst1,lst2):
        current = lst1
        while current.next:
            current = current.next
        current.next = lst2
        return lst1

    def rev(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev    
    
    def deld(self):
        current = self.head
        while current:
            temp = current
            while temp.next:
                if temp.next.data == current.data:
                    temp.next = temp.next.next
                else:
                    temp = temp.next
            current = current.next
    
    def delmidv(self):
        prev = None
        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next

    def print_l(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next



ll = lList()
ll.prep(30)
ll.prep(20)
ll.prep(10)
ll.prep(5)
ll.prep(1)
ll.delmidv()
ll.print_l()






    
   
    