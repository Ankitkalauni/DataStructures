class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        
    
class LinkList():
    def __init__(self):
        self.head = None
    
    def printlist(self):
        temp = self.head
        
        while(temp):
            print(temp.data,'-->', end = ' ')
            temp = temp.next
        print('Null\n')
    
    def push(self,data):
        new_data = Node(data)
        new_data.next = self.head
        self.head = new_data        

    def insertin(self,pre_node,newdata):
        if pre_node == None:
            print('enter the previous node to insert new node after that')
        newnode = Node(newdata)
        newnode.next = pre_node.next
        pre_node.next = newnode
    
    def append(self,new_data):
        
        new_node = Node(new_data)
        
        if self.head == None:
            self.head = new_node
        
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node            
     
    def delnode(self,data):
        
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
obj.printlist()