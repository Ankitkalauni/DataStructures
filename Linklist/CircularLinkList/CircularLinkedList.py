class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.flag = None
        
class Circularlinklist():
    
    def __init__(self):
        self.head = None
    
    def push(self,data):
        '''
        inserting new data as the head node in circular linklist
        
        
        '''
        
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
        '''
        prints the circular linklist
        '''
        
        temp = self.head
        print (temp.data, end = ' ')
        temp = temp.next
        while(temp != self.head):
            print (temp.data, end = ' ')
            temp = temp.next

    def insert(self,data):
        '''
        insert new data in circular linklist at the end        
        '''
        
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
        '''
        insert new data in the given posi inside the circular linklist. posi
        is the index after which new data will be inserted.
        '''
        count = 0
        temp = self.head
        new = Node(data)
        while(True):
            if count == posi:
                temp.next = new
                new.next = temp.next.next
                
    
    def split(self,head1,head2):
        '''
        split circular linklist into 2 seprate circular linklist.
        '''
        
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
        slow_ptr.next = self.head()
        
    def sorted_insert(self,data):
        '''
        insert the given data into the circular linklist in non-decreasing order
        '''
        new_data = Node(data)
        
        current = self.head 
        
        if current is None:
            new_data.next = new_data
            self.head = new_data

        elif (current.data >= new_data.data):
            while current.next != self.head:
                current = current.next
                
            current.next = new_data
            new_data.next = self.head 
            self.head = new_data
                
        else:
            while current.next != self.head and \
                new_data.data > current.next.data:
                current = current.next
            
            new_data.next = current.next
            current.next = new_data
        


cll= Circularlinklist()

cll.push(23)
cll.push(22)
cll.push(55)
cll.push(1)
cll.push(25)

cll.printlist()

arr = [x for x in input().split(' ')]



