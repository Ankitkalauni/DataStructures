class Node:
   def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def BreadthSearch(tree):
        h = height(tree) #height of a tree
        for i in range(1,h+1):
            printlevel(tree,i)
            
def printlevel(node,level):
    if node is None:
        return
    if level ==1:
        print(node.data,end=' ')
    elif level >1:
        printlevel(node.left,level-1)
        printlevel(node.right,level-1)

def height(node):
    if node is None:
        return 0
    else :
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)
 
        #Use the larger one
        if lheight > rheight :
            return lheight+1
        else:
            return rheight+1               

if __name__ == '__main__':
        tree = Node(23)
        l1 = Node(2)
        l2 = Node(3)

        l11 = Node(22)
        l21 = Node(33)

        tree.left = l1
        tree.right = l2

        l1.left = l11
        l2.right = l21

        BreadthSearch(tree)


