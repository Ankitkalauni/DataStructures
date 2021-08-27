class Node:
    def __init__(self,data):
        self.data = data
        self.count = 1
        self.left = None
        self.right = None

def insert(tree,data):
    if tree == None:
        new_data = Node(data)
        tree = new_data
    
    if data > tree.data:
        insert(tree.right,data)
    elif data < tree.data:
        insert(tree.left,data)
    else:
        if data == tree.data:
            tree.data = data
            tree.count+=1
    return tree

def minvaluenode(tree):
    cur = tree

    while tree != None:
        cur = cur.left
    return tree

def deleteNode(tree,data):
    if tree == None:
        return tree
    if data > tree.data:
        deleteNode(tree.right,data)
    elif data < tree.data:
        deleteNode(tree.left,data)
    else:
        if tree.count > 1:
            tree.count-=1
            return tree



        if tree.left == None:
            tree = tree.right
            return tree
        elif tree.right == None:
            tree = tree.data
            return tree

        minval = minvaluenode(tree.right)

        tree.data = minval.data

        tree.right = deleteNode(tree.right,minval.data)
    return tree

def inorder(tree):
    #base case
    if tree == None:
        return
    
    inorder(tree.left)
    print(tree.data, end = ' ')
    inorder(tree.right)

if __name__ == '__main__':

    root = None
    root = insert(root, 12)
    root = insert(root, 10)
    root = insert(root, 20)
    root = insert(root, 9)
    root = insert(root, 11)
    root = insert(root, 10)
    root = insert(root, 12)
    root = insert(root, 12)
 
    print("Inorder traversal of the given tree")
    inorder(root)
    print()
     
    print("Delete 20")
    root = deleteNode(root, 20)
    print("Inorder traversal of the modified tree")
    inorder(root)
    print()
 
    print("Delete 12")
    root = deleteNode(root, 12)
    print("Inorder traversal of the modified tree")
    inorder(root)
    print()
 
    print("Delete 9")
    root = deleteNode(root, 9)
    print("Inorder traversal of the modified tree")
    inorder(root)
