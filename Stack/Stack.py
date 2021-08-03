# =============================================================================
# #list
# =============================================================================
stack  = []

#push
stack.append(23)
stack.append(33)
stack.append(44)
stack.append(55)
stack.append(66)

#pop
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()

print(stack)

# =============================================================================
# #collections.deque
# =============================================================================
'''
deque provides an O(1) time complexity for append and pop operations as 
compared to list which provides O(n) time complexity.
'''
from collections import deque

stack  = deque()

#push
stack.append(23)
stack.append(33)
stack.append(44)
stack.append(55)
stack.append(66)

#pop
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()

# =============================================================================
# #Implementation using queue module
# =============================================================================
'''
Queue using put() function and get() takes data out from the Queue. 
'''
from queue import LifoQueue

stack = LifoQueue(maxsize = 3)

print(stack.qsize()) #numbers of the elements

#push
stack.put('a')
stack.put('b')
stack.put('c')

print("Full: ", stack.full())
print("Size: ", stack.qsize())

print('\nElements poped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())
 
print("\nEmpty: ", stack.empty())
















