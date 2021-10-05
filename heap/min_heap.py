from heapq import heapify, heappush, heappop #libraries

'''
heappop - pop and return the smallest element from heap
heappush - push the value item onto the heap, maintaining
            heap invarient
heapify - transform list into heap, in place, in linear time

'''

class MinHeap:
    '''
    parent: returns the parent of the node in min heap

    insert: insert new value into min heap using heappush

    decreasekey: decrease the given key and new value in min heap and it also sort the value
    after comparing its value with its parent value

    deleteKey: delete key, first it changes its value with negative infinty value and then pop out
    that value from the heap using extractMin

    extractMin: extract(pop) Minimum value from the min heap i.e root node

    getMin: it returns the value of the root node of the min heap(minimum value)
    '''
    def __init__(self):
        self.heap = list()

    def parent(self,i):
        return int((i-1) / 2)

    def insert(self,data):
        heappush(self.heap,data)

    def decreaseKey(self,i,new_val):
        self.heap[i] = new_val

        while(i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            self.heap[i], self.heap[self.parent(i)] = (self.heap[self.parent(i)], self.heap[i])

    def deleteKey(self, i):
        self.decreaseKey(i, float("-inf"))
        self.extractMin()
    
    def extractMin(self):
        return heappop(self.heap)


    # Get the minimum element from the heap
    def getMin(self):
        return self.heap[0]


if __name__ == '__main__':
    heapObj = MinHeap()
    heapObj.insert(3)
    heapObj.insert(2)
    heapObj.deleteKey(1)
    heapObj.insert(15)
    heapObj.insert(5)
    heapObj.insert(4)
    heapObj.insert(45)
    
    print(heapObj.extractMin())
    print(heapObj.getMin())
    heapObj.decreaseKey(2, 1)
    print(heapObj.getMin())
    print(heapObj.heap)
