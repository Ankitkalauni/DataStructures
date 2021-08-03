class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def printll(self):
        temp= self.head 
        while temp:
            print(temp.data)
            temp = temp.next 
            
            
    def push(self,data):
        '''
        push new data into stack
        '''
        if self.head is None:
            self.head = Node(data)
            self.size+=1
        else:
            temp = self.head
            new_node = Node(data)
            new_node.next = temp
            self.head = new_node
            self.size+=1
    
    def pop(self):
        '''
        remove(pop) data from the head of the linklist
        i.e from the top of the stack
        '''
        if self.head is None:
            return 'stack empty'
        else:
            self.head = self.head.next
            self.size-=1
            
    def getSize(self):
        '''
        returns the size of the stack
        '''
        return self.size
    
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
        
    def peek(self):
        if self.size == 0:
           return "stack is empty"
        else:
           return self.head.data

stack = Stack()

stack.push(66)
stack.push(44)
stack.push(2223)
stack.pop()      

stack.printll()

stack.peek()
        
        