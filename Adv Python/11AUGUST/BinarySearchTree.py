

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right=None
def createbt(root,val):
    if not root:
        root = Node(val)
    else:
        if root.data == val:
            return root
        elif root.data < val:
            root.right = createbt(root.right,val)
        else:
            root.left = createbt(root.left,val)
        return root
        
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data,end = " ")
    inorder(root.right)

root= None
root = createbt(root,10)
root = createbt(root,4)
root = createbt(root,15)
root = createbt(root,1)
root = createbt(root,8)
root = createbt(root,22)

inorder(root)
print()