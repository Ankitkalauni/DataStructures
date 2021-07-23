class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Circularlinklist():
    def __init__(self):
        self.head = None
    
    def push(self,data):
        ptr = Node(data)
        temp = self.head
        ptr.next = self.head
        
        if (self.head is not None):
            while (temp.next != self.head):
                temp = temp.next
            temp.next = ptr
        else:
            ptr.next = ptr
        self.head = ptr
        
    def printlist(self):
        temp = self.head
        
        if self.head is not None:
                
            while(True):
                print(temp.data, end = ' ')
                temp = temp.next
                if (temp == self.head):
                    break

    def insert(self,data):
        ins = Node(data)
        temp = self.head
        if self.head is not None:
            while(True):
                if temp.next != self.head:
                    temp = temp.next
                elif temp.next == self.head:
                    temp.next = ins
                    ins.next = self.head
                    break
      
    def put(self,posi,data):
        count = 0
        temp = self.head
        new = Node(data)
        while(True):
            if count == posi:
                temp.next = new
                new.next = temp.next.next
                
    
    def split(self,head1,head2):
        fast_ptr = self.head
        slow_ptr = self.head
        
        if self.head == None:
            return
        
        while(fast_ptr.next != self.head and \
              fast_ptr.next.next != self.head):
                fast_ptr = fast_ptr.next.next
                slow_ptr =  slow_ptr.next
        
        if (fast_ptr.next.next == self.head):
            fast_ptr = fast_ptr.next
        
        head1.head = self.head
        head2.head = slow_ptr.next
        
        fast_ptr.next = slow_ptr.next
        slow_ptr.next = self.head
        
if __name__ == '__main__':               
    cllist = Circularlinklist()
     
    cllist.push(12)
    cllist.push(56)
    cllist.push(2)
    cllist.push(11)
    cllist.insert(222)
    
    h1 = Circularlinklist()
    h2 = Circularlinklist()
        
    cllist.split(h1,h2)
    
    cllist.printlist()
    
    h1.printlist()
    h2.printlist()