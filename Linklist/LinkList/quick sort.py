class Node:
    def __init__(self,data):
        self.data =data
        self.next = None

class Linklist:
    def __init__(self):
        self.head = None
    
    def printlist(self):
        '''
        Returns
        -------
        returns LinkList.

        '''
        temp = self.head
        
        while(temp):
            print(temp.data,'-->', end = ' ')
            temp = temp.next
        print('Null\n')
    
    def push(self,data):
        '''
        

        Parameters
        ----------
        data : New Data to set as head of LinkList
            Add New head data into LinkList.

        Returns
        -------
        None.

        '''
        new_data = Node(data)
        new_data.next = self.head
        self.head = new_data        

    def insertin(self,pre_node,newdata):
        '''
        Parameters
        ----------
        pre_node : Name of Node
            Name of Previous Node.
        newdata : int,str,char,decimal...
            Add NewData after pre_node into LinkList.

        Returns
        -------
        None.

        '''
        if pre_node == None:
            print('enter the previous node to insert new node after that')
        newnode = Node(newdata)
        newnode.next = pre_node.next
        pre_node.next = newnode
    
    def append(self,new_data):
        '''
        

        Parameters
        ----------
        new_data : int,str,char,decimal...
            Append data into LinkList.

        Returns
        -------
        None.

        '''
        
        new_node = Node(new_data)
        
        if self.head == None:
            self.head = new_node
        
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node
    
    
class Quicksort:
    def sortList(self, head: Node) -> Node:
            def partition(start, end):
                node = start.next.next
                pivotPrev = start.next
                pivotPrev.next = end
                pivotPost = pivotPrev
                while node != end:
                    temp = node.next
                    if node.data > pivotPrev.data:
                        node.next = pivotPost.next
                        pivotPost.next = node
                    elif node.data < pivotPrev.data:
                        node.next = start.next
                        start.next = node
                    else:
                        node.next = pivotPost.next
                        pivotPost.next = node
                        pivotPost = pivotPost.next
                    node = temp
                return [pivotPrev, pivotPost]
            
            def quicksort(start, end):
                if start.next != end:
                    prev, post = partition(start, end)
                    quicksort(start, prev)
                    quicksort(post, end)

            newHead = Node(0)
            newHead.next = head
            quicksort(newHead, None)
            return newHead.next
            
first = Node(4)
sec = Node(2)
third = Node(5)
fourth = Node(1)

first.next = sec
sec.next = third
third.next = fourth


obj = Linklist()
obj.head = first

llist = Quicksort()
obj.head = llist.sortList(obj.head)
obj.printlist()