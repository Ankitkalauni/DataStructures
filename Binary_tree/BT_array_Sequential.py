class BT_array:
    def __init__(self,n):
        self.array = [None] * n 
        self.n = n

    def root(self,root_):
        if self.array[0] != None:
            return 'tree already has tree root'
        else:
            self.array[0] = root_
    
    def set_left(self,data,parent):
        if self.array[parent] == None:
            return 'given parent node empty'
        else:
            self.array[(parent*2) +1] = data

    def set_right(self,data,parent):
        if self.array[parent] == None:
            return 'given parent node empty'
        else:
            self.array[(parent*2) +2] = data
    
    def print_tree(self):
      for index,i in enumerate(range(self.n)):
          if self.array[i] != None:
              print('Value: ',self.array[i],f'index: {index}', end=" ")
          else:
              print("-", end="")
      print()

if __name__ == '__main__':
    pedh = BT_array(n=5)
    pedh.root(22)
    pedh.print_tree()
    pedh.array[0]
    pedh.set_left(22,0)
    pedh.set_right(33,0)