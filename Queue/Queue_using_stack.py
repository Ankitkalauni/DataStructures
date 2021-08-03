class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def printQueue(self):
        for i in self.s1:
            print(i)
    
    def enqueue(self,data):
        
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
            
        if len(self.s1) == 0:    
            self.s1.append(data)    
        
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()
    
    def dequeue(self):
        if len(self.s1) == 0:
            return "queue is empty"
        
        return self.s1.pop()
        
            
q = Queue()

q.enqueue(23)
q.enqueue(3)
q.enqueue(33)
q.dequeue()
q.printQueue()