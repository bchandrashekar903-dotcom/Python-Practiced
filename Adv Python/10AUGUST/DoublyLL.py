'''           Converting List to Doubly LinkedList            '''

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.prev = None

# def createDLL(arr):
#     head = None 
#     temp = None
#     for data in arr:
#         new = Node(data)    
#         if head is None:
#             head = new
#             temp = head
#         else:
#             temp.next = new
#             new.prev = temp
#             temp= temp.next 
#     return head
    
# def printll(head):  #forward traversal
#     temp = head 
#     tail = None 
#     while temp:
#         print(temp.data,end = "<->")
#         if temp.next is None:
#             tail = temp
#         temp = temp.next
#     print("None")        
#     return tail
    
# def printdll(tail): #backward
#     temp = tail
#     while temp:
#         print(temp.data,end = "<->")
#         temp = temp.prev
#     print("None")    

# arr = [1,2,3,4,5]
# head = createDLL(arr)
# tail = head
# while tail.next:
#     tail = tail.next
# printll(head)
# printdll(tail)
 

'''           Converting Circular Doubly Linked List            '''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def createCLL(arr):
    if not arr:
        return None
    head = None 
    temp = None
    for data in arr:
        new = Node(data)    
        if head is None:
            head = new
            temp = head
        else:
            temp.next = new
            new.prev = temp  # Link prev pointer of new node
            temp = temp.next 
    # Connect last node (temp) with first node (head) circularly
    temp.next = head
    head.prev = temp
    return head
    
def printll(head):  # forward traversal
    if not head:
        print("Empty List")
        return
    temp = head 
    while True:
        print(temp.data, end=" <-> ")
        temp = temp.next
        if temp == head:
            break
    print("(Back to Head)")        
    
def printdll(tail): # backward traversal
    if not tail:
        print("Empty List")
        return
    temp = tail
    while True:
        print(temp.data, end=" <-> ")
        temp = temp.prev
        if temp == tail:
            break
    print("(Back to Tail)")    

arr = [1, 2, 3, 4, 5]
head = createCLL(arr)

# In a Circular Doubly Linked List, tail is head.prev
tail = head.prev if head else None

print("Forward Traversal:")
printll(head)

print("Backward Traversal:")
printdll(tail)

 

