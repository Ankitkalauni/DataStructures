'''
doubly link list
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class Dlinklist:
    def __init__(self):
        self.head = None
        
    def insert(self,data):
        '''
        insert new data as a head of the doubly link list
        '''
        
        new_nd = Node(data)
        
        if self.head is None:
            self.head = new_nd
        else:
            temp = self.head
            temp.prev = new_nd
            new_nd.next = temp
            
            self.head = new_nd
        return self.printlist()
        
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
        
    def append(self,data):
        '''
        appending the new data into double link list at the end
        '''
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            new_nd = Node(data)
            
            temp.next = new_nd
            new_nd.prev = temp
        self.printlist()
            
    def insert_into(self,data,index):
        index = int(index)
        temp = self.head
        count = 0
        if self.head == None:
            self.insert(data)
            
            return self.printlist()
            
        while(temp):
            if index == count:
                temp2 = temp.next
                
                new_nd = Node(data)
                
                new_nd.prev = temp
                temp.next = new_nd
                
                new_nd.next = temp2
                temp2.prev = new_nd
                return self.printlist()
            temp = temp.next
            count+=1
        
        if temp==None:
            return 'index out of bound'
        
    def insert_after(self,data,prev_node):
        if self.head is None:
            self.head = Node(data)
            
            return self.printlist()
        
        if prev_node.next is None:
            self.append(data)
        new_nd = Node(data)
        temp = prev_node.next
        
        temp.prev = new_nd
        new_nd.next = temp
        
        new_nd.prev = prev_node
        prev_node.next = new_nd
        
        return self.printlist()
    
    def insert_before(self,data,after_node):
        if self.head is None:
            self.head = Node(data)
            
            return self.printlist()
        
        if after_node.next is None:
            return 'cannnot insert before the node bcoz the given node is null'
        
        temp = after_node.prev
        
        new_nd = data
        
        after_node.prev = new_nd
        new_nd.next = after_node
        
        temp.next = new_nd
        new_nd.prev = temp
        
        return self.printlist()
    
    
'''
Insertion 
A node can be added in four ways 
1) At the front of the DLL 
2) After a given node. 
3) At the end of the DLL 
4) Before a given node.
'''

head = Dlinklist()

head.insert('23')
head.insert('33')
head.append('55')
head.insert_into('69', 1)
head.printlist()

