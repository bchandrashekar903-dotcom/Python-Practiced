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

        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print("Inorder")
print(inorder(root))
print("Preorder")
print(preorder(root))
print("Postorder")
print(postorder(root))
print("Level order")
print(levelorder(root))

 