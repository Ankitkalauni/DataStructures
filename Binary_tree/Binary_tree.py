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

def deleteDeepest(root,d_node):
    q = []
    q.append(root)
    while(len(q)):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)
  
# function to delete element in binary tree
def deletion(root, key):
    if root == None :
        return None
    if root.left == None and root.right == None:
        if root.key == key :
            return None
        else :
            return root
    key_node = None
    q = []
    q.append(root)
    while(len(q)):
        temp = q.pop(0)
        if temp.data == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if key_node :
        x = temp.data
        deleteDeepest(root,temp)
        key_node.data = x
    return inorder(tree)

if __name__ == '__main__':
    tree = Node(23)
    tree.left = Node(33)
    tree.right = Node(334)
    
    insert(tree, 66)
    inorder(tree)
    
    deletion(tree, 33)
    