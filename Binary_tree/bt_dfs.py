class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def inorder(tree):
    if tree == None:
        return
    
    inorder(tree.left)
    print(tree.data, end=' ')
    inorder(tree.right)

def preorder(tree):
    if tree == None:
        return
    
    print(tree.data, end=' ')
    inorder(tree.left)
    inorder(tree.right)
    
def postorder(tree):
    if tree == None:
        return
    
    
    inorder(tree.left)
    inorder(tree.right)
    print(tree.data, end=' ')

if __name__ == '__main__':
    tree = Node(23)
    lft = Node(22)
    rgt = Node(33)
    
    tree.left = lft
    tree.right = rgt
    
    postorder(tree)