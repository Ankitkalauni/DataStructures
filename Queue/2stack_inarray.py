'''
Create a data structure twoStacks that represents two stacks. Implementation of twoStacks should use only one array, i.e., both stacks should use the same array for storing elements. Following functions must be supported by twoStacks.
push1(int x) –> pushes x to first stack 
push2(int x) –> pushes x to second stack
pop1() –> pops an element from first stack and return the popped element 
pop2() –> pops an element from second stack and return the popped element
Implementation of twoStack should be space efficient.
'''

class two_Stack_inarray:
    def __init__(self,n):
        self.size = n
        self.array = [None] * n
        self.top1 = -1 #first stack top
        self.top2 = self.size #secound stack top
        
    
    def printarray(self):
        for i in self.array:
            print(i, end=' ')
    
    def push1(self,data):
        if self.top1 < self.top2-1:
            self.top1 = self.top1 + 1 
            self.array[self.top1] = data
            
        else:
            return 'stack overflow'
            
    def push2(self,data):
        if self.top1 < self.top2-1:
            self.top2-=1
            self.array[self.top2] = data
            
        else:
            return 'stack overflow'
        
    def pop1(self):
        if self.top1 >=0:
            data = self.array[self.top1]
            self.array[self.top1] = None
            self.top1-=1
            return data
        else:
            return 'stack underflow'
        
    def pop2(self):
        if self.top2 <self.size:
            data = self.array[self.top2]
            self.array[self.top2] = None
            self.top2+=1
            return data
        else:
            return 'stack underflow'
        
if __name__ == '__main__':
    s = two_Stack_inarray(6)
    
    s.push1(2)
    s.push2(3)
    
    s.pop1()
    s.pop2()
    s.printarray()
    