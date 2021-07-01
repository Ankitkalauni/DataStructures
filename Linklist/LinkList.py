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

if __name__ == "__main__":   
     
    obj = LinkList()
    
    one = Node('apple')
    two = Node('ball')
    three = Node('cat')
    four = Node('dog')
    five = Node('elephant')
    
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