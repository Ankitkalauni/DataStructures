class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.front,self.rear = None,None

    def enqueue(self,data):
        new_data = Node(data)
        if self.rear == None:
            self.front,self.rear = new_data, new_data
            return
        self.rear.next = new_data
        self.rear = new_data

    def dequeue(self):
        if self.front == None:
            return None
        elif self.front == self.rear:
            self.front, self.rear = None, None
            return
        temp = self.front.next
        self.front = temp

    def printll(self):
        if self.front is not None:
            temp = self.front
            while temp:
                print(temp.data, end= ' ')
                temp = temp.next
    
    def isnull(self):
        if self.rear is None:
            return True

if __name__ ==  '__main__':
    q = Queue()
    q.enqueue(33)
    
    q.dequeue()
    
    q.printll()


