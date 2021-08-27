class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

def appendarray(bt,array):
    if bt == None:
        return 

    appendarray(bt.left,array)
    
    array.append(bt.data)
    
    appendarray(bt.right,array)

def count_nodes(bt):
    if bt is None:
        return 0

    return count_nodes(bt.left) + count_nodes(bt.right) + 1

def array_to_tree(array,bst):
    if bst is None:
        return

    array_to_tree(array,bst.left)

    bst.data = array[0]
    array.pop(0)

    array_to_tree(array,bst.right)

def bt_to_bst(bt):
    if bt is None:
        return

    arr = []

    n = count_nodes(bt)

    appendarray(bt,arr)
    
    arr.sort

    array_to_tree(arr,bt)

def inorder(bst):
    if bst is None:
        return

    inorder(bst.left)
    print(bst.data, end=' ')
    inorder(bst.left)
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(30)
    root.right = Node(15)
    root.left.left = Node(20)
    root.right.right = Node(5)

    bt_to_bst(root)

    inorder(root)