''' Binary Trees  '''

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def preorder(root):
    if root is None:
        return 
    print( root.data,end=" ")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root!=None:
        inorder(root.left)
        print( root.data,end = " ")
        inorder(root.right)

def postorder(root):
    if root!=None:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end= " ")

def createbt(arr,i,n):
    if i>=n:
        return 
    root = TreeNode(arr[i])
    root.left = createbt(arr,2*i+1,n)
    root.right = createbt(arr,2*i+2,n)
    return root

def levelorder(root):
    if root is None:
        return
    q = [root]
    while q:
        node = q.pop(0)
        print(node.data,end = " ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

def s_preorder(root,val):
    if not root:
        return False
    if root.data == val:
        return True
    return s_preorder(root.left,val) or s_preorder(root.right,val)
        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Inorder:")
inorder(root)
print()

print("\nPreorder:")
preorder(root)
print()

print("\nPostorder:")
postorder(root)
print()

print("\nLevel order:")
levelorder(root)
print()

arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
created_root = createbt(arr, 0, n)
print(f"\nBinary Tree Created from List {arr} (Level Order Traversal):")
levelorder(created_root)
print()

print("Search result:",s_preorder(root,4))


 