class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.right = None
        self.left = None

def Insert(tree,data):
    if tree == None:
        return Node(data)

    else:
        if tree.data == data:
            return tree

        elif tree.data > data:
            tree.left =  Insert(tree.left,data)
        else:
            tree.right = Insert(tree.right,data)

    return tree

def Search(tree,data):
    #base case
    if tree == None or tree.data == data:
        return tree
    if tree.data < data:
        return Search(tree.right,data)
    return Search(tree.left,data)

def Inorder(tree):
    #base case
    if tree == None:
        return 0

    Inorder(tree.left)
    print(tree.data, end = ' ')
    Inorder(tree.right)
    


if __name__ == '__main__':
    r = Node(50)
    r = Insert(r, 20)
    r = Insert(r, 40)
    r = Insert(r, 70)
    r = Insert(r, 30)
    r = Insert(r, 60)
    r = Insert(r, 80)

    Search(r,50)