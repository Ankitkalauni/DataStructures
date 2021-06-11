class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Linklist():
    def __init__(self):
        self.head = None
    
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

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

            
if __name__ == '__main__':
    
    #initializing
    obj = Linklist()
    obj.head = Node('apple')
    sec = Node('banana')
    third = Node('cat')
    
    #linking
    obj.head.next = sec
    sec.next = third
    
    #pushing new data(Node)
    obj.push('dog')
    
    #inserting new data after given node
    obj.insertin(sec,'elephant')
    
    obj.append('fish')
    
    #printing linklist
    obj.printlist()
