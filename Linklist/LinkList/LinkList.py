class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        
    
class LinkList():
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
     
    def delnode(self,data):
        
        '''
        Parameters
        ----------
        data : int,str,char,decimal...
            Delete Node using data.

        Returns
        -------
        None.

        '''
        
        temp = self.head
        
        if (temp is not None):
            if (temp.data == data):
                self.head = temp.next
                temp = None
                return
        
        while (temp is not None):
            if (temp.data == data):
                break
            prev = temp
            temp = temp.next
        
        if (temp is None):
            return
        
        prev.next = temp.next
        temp = None

    def delnodeposi(self,position):
        '''
        

        Parameters
        ----------
        position : int
            Position of node which wanted to be removed from the LinkList.

        Returns
        -------
        None.

        '''
        temp = self.head
        
        if temp==None:
            return
        
        if position == 0:
            self.head = temp.next
            return
        
        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break
            
        if temp is None:
            return
        if temp.next is None:
            return
        
        next = temp.next.next
        temp.next = None
        temp.next = next
    
    def dellist(self):
        '''
        Returns
        -------
        Delete Data of LinkList.In python garbage collection happens. therefore, only self.head = None
        would also delete the link list

        '''
        temp = self.head
        
        while temp:
            next = temp.next        
            del temp.data
            temp = next
            
    def getcount(self):
        '''
        Returns
        -------
        Numbers of Nodes in a LinkList.
        '''
        temp = self.head
        count = 0
        while temp:
            count+=1
            temp = temp.next
        return count       

        
    def get_count_from(self,node):
        '''
        

        Parameters
        ----------
        node : str
            name of the node from where the count starts.

        Returns
        -------
        TYPE
            count of the nodes the linklist have from given node.

        '''
        
        if node is None:
            return 0
        else:
            return 1+ self.get_count_from(node.next)
        
    def get_count(self):
        '''
        return the number of nodes in link list
        '''
        
        return self.get_count_from(self.head)
    
    def search(self,x):
        '''
        searches for the data in the link list, return True if the data is in
        any node of the linklist.
        '''
        
        temp = self.head
        
        while temp:
            if temp.data == x:
                return True
            else:
                temp = temp.next
        return 'input data is not in the linklist'
    
    def getNth(self,index):
        temp = self.head
        count = 0
        
        while temp:
            if int(index) == count:
                return temp.data
            temp = temp.next
            count+=1
        
        return 'index out of bound'

    def getNthh(self,node,index):
        index = int(index)
        temp = node
        count = 0
        if node is None:
            return 0
        if index == count:
            return temp.data
        else:
            return self.getNthh(temp.next,index-1)
    
        return 'index out of bound'        
        
    def get_n_back(self,n):
        '''
        n the location of the node from the last node of the link list
        '''
        n = int(n)
        count = 0
        ptr1 = self.head
        ptr2 = self.head
        
        if self.head is not None:
            while count < n:
                if ptr2 is None:
                    return 'n is out of bound'
                
                ptr2 = ptr2.next
                count+=1
            
            
        if ptr2 is None:
            self.head = self.head.next 
            if self.head is not None:
                print(f'{n} no.node from the end of the link list contains {ptr1.data}')
            
        else:
            while ptr2 is not None:
                ptr1 = ptr1.next
                ptr2 = ptr2.next 
                
            print(f'{n} no.node from the end of the link list contains {ptr1.data}')
    
    
    def swapnode(self,x,y):
        '''
        swap node x and y without changing data
        '''
        if x == y:
            return
        
        tempx = self.head 
        while tempx is not None and tempx!=x:
            prex = tempx 
            tempx = tempx.next 

        tempy = self.head 
        while tempy is not None and tempy!=y:
            prey = tempy
            tempy = tempy.next

        if tempy and tempx is None:
            return
        
        if prex!=None:
            prex.next = tempy 
        else:
            self.head = tempy 
            
        if prey!=None:
            prey.next = tempx 
        else:
            self.head = tempx
        
        temp = tempx.next
        tempx.next = tempy.next    
        tempy.next = temp
        
        return self.printlist()
        
    def palindrome(self):
        
        #a word, phrase, or sequence that reads the same backwards as forwards
        
        '''
        check whether the link list is a palindarome or not. return True if it
        is a palindrome
        
        '''
        stack = []
        
        temp = self.head 
        while temp:
            stack.append(temp.data)
            temp= temp.next
        
        temp = self.head
        while temp:
            if stack.pop() == temp.data:
                temp = temp.next
            else:
                return False
        return True

    def detectloop(self):
        '''
        detect if the link list has a loop of a nodes, using hash table(set)
        to store the nodes and return True if the link list is has a loop
        '''
        hashh = set()
        
        temp = self.head 
        
        while temp:
            if temp in hashh:
                return True
            
            temp = temp.next 
            hashh.add(temp)    
        return True
        



if __name__ == "__main__":   
     
    obj = LinkList()
    
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(1)
    
    obj.head = one
    one.next = two
    two.next = three
    three.next = four
    four.next = five
    
    obj.printlist()
    obj.push('pineapple')
    obj.insertin(three, 'catfish')
    obj.append('fish')
    obj.delnode('cat')
    obj.delnodeposi(2)
    obj.printlist()
    obj.getcount()
    
    obj.palindrome()