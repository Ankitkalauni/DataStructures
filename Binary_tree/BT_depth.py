class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def depthofNode(tree,data):
    #base case to stop recurssion
    if tree == None:
        return -1

    temp = -1

    if tree.data == data:
        return temp+1
    
    distance = depthofNode(tree.left,data)

    if distance >=0:
        return distance+1

    distance = depthofNode(tree.right,data)

    if distance >=0:
        return distance+1
    return distance

if __name__ == '__main__':
    tree = Node(2)
    tree.left = Node(22)
    tree.right = Node(33)
    tree.left.left = Node(222)
    tree.right.right =Node(333)
    tree.left.right = Node(2)
    tree.right.left = Node(6)
    tree.left.left.right = Node(44)
    
    depthofNode(tree,44)  
