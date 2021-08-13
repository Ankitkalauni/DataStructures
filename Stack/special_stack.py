'''
Design a Data Structure SpecialStack that supports all the stack operations 
like push(), pop(), isEmpty(), isFull() and an additional operation getMin() 
which should return minimum element from the SpecialStack. All these 
operations of SpecialStack must be O(1). To implement SpecialStack, you 
should only use standard Stack data structure and no other data structure like
 arrays, list, . etc
'''

class Stack:
    def __init__(self):
        self.stack = []
        self.temp = int() #stores minimum value in a stack
        self.size = -1
        self.max = 100
        
    def isFull(self):
        if self.size == self.max-1:
            return True
        else:
            return False
    
    def printStack(self):
        return self.stack
        
    def push(self,data):
        if self.size == self.max-1:
            return 'stack overflow'
        
        self.stack.append(data)
        self.size+=1
        
        if self.temp > data:
            self.temp = data
        elif self.temp == 0:
            self.temp = data
        
    def pop(self):
        if self.size == -1:
            return 'stack underflow'
        
        self.stack.pop()
        self.size-=1
        
    def isEmpty(self):
        if self.size == -1:
            return True
        else:
            return False
        
    def getMin(self):
        return self.temp

    
if __name__ ==  '__main__':        
    s = Stack()
    
    s.push(23)
    s.push(222)
    s.push(53)
    s.push(2)
    s.push(233)        
            
    s.printStack() 
    
    s.getMin()       
        