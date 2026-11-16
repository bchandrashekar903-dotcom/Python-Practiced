'''           Converting List to LinkedList            '''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def createLL(arr):
    head = None 
    curr = None
    for data in arr:
        new = Node(data)
        if head is None:
            head = new
            curr = head
        else:
            curr.next = new
            curr = curr.next
    return head
    
def printll(head):
    curr = head
    while curr is not None:
        print(curr.data,end = "->")
        curr = curr.next
    print("None")        
    

arr = [1,2,3,4,5]
head = createLL(arr)
printll(head)
 

