class Node:
   def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def inorder(tree):
    '''

    Parameters
    ----------
    tree : binary tree for inoder traversal
        inorder(Depth First Traversals) travers into the binary tree.
        and prints out the values of the nodes

    Returns
    -------
    None.

    '''
    if not tree:
        return
    
    inorder(tree.left)
    print(tree.data,end = ' ')
    inorder(tree.right)
    
def insert(tree,data): 
    if not tree:
        root = Node(data)
        return
    q = []
    q.append(tree)
 
    # Do level order traversal until we find
    # an empty place.
    while (len(q)):
        tree = q[0]
        q.pop(0)
 
        if (not tree.left):
            tree.left = Node(data)
            break
        else:
            q.append(tree.left)
 
        if (not tree.right):
            tree.right = Node(data)
            break
        else:
            q.append(tree.right)    

if __name__ == '__main__':
    tree = Node(23)
    tree.left = Node(33)
    tree.right = Node(334)
    
    insert(tree, 66)
    inorder(tree)
    
    
    