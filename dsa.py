# arr = [1,3,5,7,9]
# #True or False
# def find(arr,target):
#     low = 0
#     high = len(arr)-1
#     while low<=high:
#         mid = (low+high)//2
#         if arr[mid]==target:
#             return True
#         elif arr[mid]<=target:
#             low =mid+1
#         else:
#             high = mid-1
#     return False
# print(find(arr,7))



class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LiknkedList:
    def __init__(self):
        self.head = None

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delet(self):
        if not self.head or not self.head.next:
            return
        
        slow = self.head
        fast = self.head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next

    def print_ll(self):
        if self.head is None:
            print('empty')
        else:
            current = self.head
            while current is not None:
                print(current.data, '-->',end='')
                current = current.next
     

LL = LiknkedList()
LL.prepend(50)
LL.prepend(40)
LL.prepend(30)
LL.prepend(20)
LL.prepend(10)
LL.delet()
LL.print_ll()
        

    
 